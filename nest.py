#!/usr/bin/env python

import re
import urllib
import random
import tempfile
import os

import Image
from pyechonest import artist

import lolspeak
import caption

def songstest(name):
    a = artist.Artist(name)
    songs = a.get_songs()
    titles = [s.title for s in songs]
    titles.sort(key=lambda x: len(x) if len(x) < 50 else 0)
    print titles
    print [len(s) for s in titles]
    return [lolspeak.translate(s) for s in titles]

def pictest(name):
    a = artist.Artist(name)
    pics = a.get_images()
    url = random.choice(pics)['url']
    print url
    f = urllib.urlopen(url)
    extension = re.search(r'([.]\w+)$', url).group(1)
    temp_dir = tempfile.mkdtemp()
    local_f = open(os.path.join(temp_dir, 'temp'+extension), 'wb')
    local_f.write(f.read())
    local_f.close()
    return local_f.name

if __name__ == '__main__':

    import sys
    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = 'cascada'
    string = songstest(name)
    fname = pictest(name)
    caption.txt2img(fname, string)
