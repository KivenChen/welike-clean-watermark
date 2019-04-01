from PIL import Image, ImageDraw
from .config import *


def modify(name, img):
    draw = ImageDraw.Draw(img)
    mode = config[name]
    for op in mode:
        draw.__getattr__(op['name'])(**op['kwargs'])
    del draw
    img.save('filename')
    return filename



