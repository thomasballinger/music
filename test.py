#!/usr/bin/env python

from pyechonest import artist
import lolspeak


def plottest():
    from matplotlib import pyplot as pt


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

def songstest(name):
    a = artist.Artist(name)
    songs = a.get_songs()
    print [s.title for s in songs]
    print [lolspeak.translate(s.title) for s in songs]


if __name__ == '__main__':
    # Idea: for a given artist, 
    #  -get their most popular songs, lol-ify
    #  -get a nice picture, paste lol'd song names
    #
    #
    # Idea: Use lyrics for a song to look for pictures to do with it.
    songstest('Just4Kicks')
