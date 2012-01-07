#!/usr/bin/env python
"""Basic captioning"""

# based on code at 
# http://www.linuxquestions.org/questions/programming-9/python-can-you-add-text-to-an-image-in-python-632773/
#
# BrianK
# Senior Member
# 
# Registered: Mar 2002
# Location: Los Angeles, CA
# Distribution: Debian, Ubuntu
# Posts: 1,330
#
#



import tempfile
import shutil
import Image, ImageDraw, ImageFont
import re
from os import chdir, path
import os

def pasteTextOntoImage(image, text=None, show=False, bg="#ffffff", fg="#000000",  font_size=20):
    """Puts a caption on an image, returning the resultant image file"""
    if not text:
        text = ['test text']
    font_dir = "/usr/share/fonts/truetype/freefont/"
    font="FreeSansBold.ttf"
    fnt = ImageFont.truetype(font_dir+font, font_size)
    lineWidth = 25
    img = Image.open(image)
    draw = ImageDraw.Draw(img)                     # setup to draw on the main image
    for i, line in enumerate(text):
        draw.text((10,lineWidth*i), line, font=fnt)      # add some text to the main
    if show:
        img.show()
    else:
        print image
        base, extension = re.search(r'(.*)([.]\w+$)', image).groups()
        outname = base+'-fixed'+extension
        print outname
        tempdir = tempfile.mktemp()
        img.save(os.path.join(tempdir, outname), "JPEG", quality=100)
        return open(os.path.join(tempdir, outname), 'rb')

if __name__ == '__main__':
    txt2img('/home/tomb/Downloads/3604.jpg', ["This is a really weird image", "doncha know", 'you betcha', '.','.','.','.','.','.','.','.','.','.','.','.'])
