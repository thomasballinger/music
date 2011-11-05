#!/usr/bin/env python

from pyechonest import artist

from matplotlib import pyplot as pt

a = artist.Artist('Just4Kicks')
print a.get_similar()

hots = artist.top_hottt()
hotnesses = [a.hotttnesss for a in hots]
familiarities = [a.familiarity for a in hots]
names = [a.name for a in hots]

print names
print familiarities
print hotnesses

pt.plot(familiarities, hotnesses, 'r.')
pt.xlabel('hotttnesss')
pt.ylabel('familiarity')
for name, fam, hot in zip(names, hotnesses, familiarities):
    pt.annotate(name, (hot, fam))
pt.show()
