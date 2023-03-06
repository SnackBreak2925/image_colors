import os
from resizeimage import resizeimage
from PIL import Image
import webcolors
from colorthief import ColorThief


def bgr_to_hex(bgr):
    rgb = list(bgr)
    rgb.reverse()
    return webcolors.rgb_to_hex(tuple(rgb))


def FindColors(image):
    color_hex = []
    for i in image:
        for j in i:
            j = list(j)
            color_hex.append(bgr_to_hex(tuple(j)))
    return set(color_hex)


def main():
    image = Image.open(r'./dog.jpg')
    color_list = FindColors(image.palette)
    print(color_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
