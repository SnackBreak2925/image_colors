from PIL import Image
import colorsys
from colormap import rgb2hex

class Handler(object):
    @staticmethod
    def Handler(img,input_name):
        output_width = 900
        wpercent = (output_width / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((output_width, hsize), Image.Resampling.LANCZOS)
        # в jpg из png
        rgb_im=img.convert('RGB')
        resize_name = 'resize_' + input_name# новое имя: resize+старое имя
        return rgb_im,resize_name


    @staticmethod
    def ColorsInHex(input):
        hexes = []
        for i in input[0]:
            hexes.append(rgb2hex(i[0][0], i[0][1], i[0][2]))
        return hexes
