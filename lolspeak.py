#!/usr/bin/env python
"""Lolcat translator, requires lolcat.yaml file"""
import yaml
import sys
import re

English2Lol = yaml.load(open('tranzlator.yml'))

# some monkeypatching for good luck
English2Lol['someone\'s'] = 'some1\'s'

def translate(s):
    """Super-basic english to lolcat translator"""
    words = s.split()
    output = []
    for word in words:
        title = True if word.title() == word else False
        try:
            m = re.match(r"(\W*)([\w']+)(\W*)", word)
            preceeding, just_word, trailing = m.groups()
        except:
            return word
        lower = just_word.lower()
        if lower in English2Lol:
            output_part = English2Lol[lower]
        else:
            output_part = lower
        if title:
            output_part = output_part.title()
        output.append(preceeding + output_part + trailing)
    return ' '.join([o.upper() for o in output if o])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print translate(' '.join(sys.argv[1:]))
    else:
        print translate(u"Someone's cat likes to eat bananas!")
        print translate(u"You really got a hold on me (US Stereo Mix)")
