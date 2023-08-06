import argparse
import numpy as np
import matplotlib.pyplot as plt
import mrcfile
import time
import sys
import multiprocessing
import cv2
from maskstackcreator import MaskStackCreator
import scipy.misc as sp
import image_reader

#from pyfft.cuda import Plan
#import pycuda.driver as cuda
#from pycuda.tools import make_default_context
#import pycuda.gpuarray as gpuarray

argparser = argparse.ArgumentParser(
    description='Enhances line images',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

argparser.add_argument(
    '-i',
    '--input',
    help='path to input file')

argparser.add_argument(
    '-d',
    '--downsamplesize',
    default=1024,
    type=int,
    help='mask size')

argparser.add_argument(
    '-f',
    '--filamentwidth',
    default=50,
    type=int,
    help='filament with after downsampling')

argparser.add_argument(
    '-m',
    '--maskwidth',
    default=100,
    type=int,
    help='mask width')

argparser.add_argument(
    '-a',
    '--angle_step',
    default=2,
    type=int,
    help='angle step size')

#cuda.init()
#context = make_default_context()
#stream = cuda.Stream()




def _main_():


    args = argparser.parse_args()

    '''
    LOAD IMAGE DATA AS EXAMPLE
    '''

    example_path = "/home/twagner/Projects/cryolo/data/Sabrina_Actin_Myosin_NM2C/two_mrcs_for_test/gammaADP-3251.mrc"
    if args.input is not None:
        example_path = args.input
    mask_size = args.downsamplesize
    filament_width = args.filamentwidth
    mask_width = args.maskwidth
    angleStep = args.angle_step
    example = image_reader.image_read(example_path)
    '''
    CREATE EXAMPLE: RESIZE IMAGE, REPEAT IT 12 TIMES (simulates 12 input images)
    '''
    example = sp.imresize(example, size=(args.downsamplesize, args.downsamplesize))
    example = example
    examples = np.repeat(example[:, :, np.newaxis], 12, axis=2)
    examples = np.moveaxis(examples, 2, 0)

    '''
    CREATE EXAMPLE WITH PATHS
    '''
    example_paths = [example_path]*12

    '''
    INIT MASK CREATOR
    '''
    mask_creator = MaskStackCreator(filament_width, mask_size, mask_width, angleStep, bright_background=True)
    mask_creator.init()

    '''
    DO ENHANCEMENT
    '''
    start = time.time()
    enhanced_images = enhance_images(example_paths, mask_creator)
    end = time.time()
    print "Enhancement of 12 images"
    print "Enhancement time per image (first run)", (end - start) / 12

    '''
    PLOT RESULT
    '''
    fig = plt.figure(figsize=(2, 2))
    fig.add_subplot(2,2,1)
    plt.imshow(enhanced_images[0]["max_value"])
    fig.add_subplot(2, 2, 2)
    plt.imshow(enhanced_images[0]["max_angle"])
    fig.add_subplot(2, 2, 3)
    plt.imshow(mask_creator.get_mask_stack()[0])
    fig.add_subplot(2, 2, 4)
    plt.imshow(mask_creator.get_mask_stack()[23])

    plt.show()
    np.savetxt("/home/twagner/Projects/cryolo/data/Sabrina_Actin_Myosin_NM2C/unit_test/enhanced.txt",enhanced_images[0]["max_angle"])


def enhance_images(input_images, maskcreator):
    is_path_list = isinstance(input_images,list)

    if not is_path_list:
        if input_images.shape[1] != maskcreator.get_mask_size() or input_images.shape[2] != maskcreator.get_mask_size():
            sys.exit("Mask and image dimensions are different. Stop")

    fft_masks = maskcreator.get_mask_fft_stack()
    global all_kernels
    all_kernels = fft_masks
    pool = multiprocessing.Pool()
    if is_path_list:
        enhanced_images = pool.map(wrapper_fourier_stack_paths, input_images)
    else:
        enhanced_images = pool.map(wrapper_fourier_stack, input_images)
    pool.close()
    pool.join()
    for img in enhanced_images:
        img["max_angle"] = img["max_angle"]*maskcreator.get_angle_step()

    return enhanced_images

def convolve(fft_image, fft_mask):

   # fft_mask = np.array(fft_mask)
    if len(fft_mask.shape) > 2:
        fft_image = np.expand_dims(fft_image, 2)
    result_fft = np.multiply(fft_mask, fft_image)
    result = np.fft.irfft2(result_fft, axes=(0, 1))
    result = np.fft.fftshift(result, axes=(0, 1))

    return result

all_kernels = None
def wrapper_fourier_stack(image):
    return enhance_image(fourier_kernel_stack=all_kernels, input_image=image)

def wrapper_fourier_stack_paths(image_paths):
    return enhance_image_by_path(fourier_kernel_stack=all_kernels, input_image_path=image_paths)

def enhance_image_by_path(fourier_kernel_stack, input_image_path):
    original_image = image_reader.image_read(input_image_path)

    # create square image with mask size
    height = original_image.shape[0]
    width = original_image.shape[1]
    max_dim = height if height > width else width
    scaling = 1.0*fourier_kernel_stack.shape[0]/max_dim
    original_image_resized = cv2.resize(original_image, dsize=(0,0), fx=scaling, fy=scaling)

    vertical_offset = (fourier_kernel_stack.shape[0]-original_image_resized.shape[0])
    top_offset = vertical_offset/2
    bottom_offset = top_offset + (0 if vertical_offset % 2 == 0 else 1)

    horizontal_offset = (fourier_kernel_stack.shape[0]-original_image_resized.shape[1])
    left_offset = horizontal_offset/2
    right_offset = left_offset + (0 if horizontal_offset % 2 == 0 else 1)

    fill_value = np.mean(original_image_resized)
    input_image = cv2.copyMakeBorder(src=original_image_resized,
                                     top=top_offset,
                                     bottom=bottom_offset,
                                     left=left_offset,
                                     right=right_offset,
                                     borderType=cv2.BORDER_CONSTANT,
                                     value=np.asscalar(fill_value))
    input_image_fft = np.fft.rfft2(input_image)

    number_kernels = fourier_kernel_stack.shape[2]
    result = convolve(input_image_fft, fourier_kernel_stack[:, :, 0])

    enhanced_images = np.empty((original_image_resized.shape[0], original_image_resized.shape[1], number_kernels))
    result_cropped = result[top_offset:(top_offset + original_image_resized.shape[0]),
                     left_offset:(left_offset + original_image_resized.shape[1])]
    enhanced_images[:, :, 0] = result_cropped
    for i in range(1,number_kernels):
        result = convolve(input_image_fft, fourier_kernel_stack[:, :, i])
        #crop result
        result_cropped = result[top_offset:(top_offset + original_image_resized.shape[0]),
                         left_offset:(left_offset + original_image_resized.shape[1])]

        enhanced_images[:, :, i] = result_cropped

    max = np.amax(enhanced_images, axis=2)
    maxID = np.argmax(enhanced_images, axis=2)
    return {"max_value": max, "max_angle": maxID}

def enhance_image(fourier_kernel_stack, input_image):
    input_image_fft = np.fft.rfft2(input_image)
    number_kernels = fourier_kernel_stack.shape[2]


    result = convolve(input_image_fft, fourier_kernel_stack[:, :, 0])
    enhanced_images = np.empty((result.shape[0], result.shape[1], number_kernels))
    enhanced_images[:, :, 0] = result
    for i in range(1,number_kernels):
        result = convolve(input_image_fft, fourier_kernel_stack[:, :, i])
        enhanced_images[:, :, i] = result

    max = np.amax(enhanced_images, axis=2)
    maxID = np.argmax(enhanced_images, axis=2)
    return {"max_value": max, "max_angle": maxID}


if __name__ == '__main__':
    _main_()