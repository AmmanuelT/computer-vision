from PIL import Image
import numpy as np
import sys


def rgb(src: str):
    """
        given the source path of an image
        returns a np array of rgb values of pixels
    """

    img = Image.open(src)
    arr = np.array(img)
    return arr


def ycbcr(src: str):
    """
        Given source string
        return YcBcR representation
    """

    # taken from jpeg convertion from https://en.wikipedia.org/wiki/YCbCr
    arr = rgb(src)
    transform = np.array([[0.299, 0.587, 0.114],
                          [-0.169, -0.331, 0.5],
                          [0.5, -0.419, -0.081]])
    add = np.array([0, 128, 128])
    arr = arr @ transform.T
    arr = np.add(arr, add)
    return arr


if __name__ == '__main__':
    if len(sys.argv) > 1:
        src = sys.argv[1]
    else:
        src = '../images/colour-spaces/60.jpg'
    array = rgb(src)
    print(array.shape)
    print(array[0])

    array = ycbcr(src)
    print("Homemade: ")
    print(array.shape)
    print(array[:5])

    img = Image.open(src)
    img = img.convert('YCbCr')
    array = np.array(img)
    print("Using Pillow: ")
    print(array.shape)
    print(array[:5])
