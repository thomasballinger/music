import yaml
import sys
import re

English2Lol = yaml.load(open('tranzlator.yml'))
English2Lol['someone\'s'] = 'some1\'s'
print English2Lol['a'].__repr__()

def translate(s):
    """Super-basic translator"""
    print s
    words = s.split()
    output = []
    for word in words:
        title = True if word.title() == word else False
        m = re.match(r"(\W*)([\w']+)(\W*)", word)
        print m.groups()
        preceeding, just_word, trailing = m.groups()
        lower = just_word.lower()
        if lower in English2Lol:
            output_part = English2Lol[lower]
        else:
            output_part = lower
        if title:
            output_part = output_part.title()
        output.append(preceeding + output_part)
    return ' '.join(output)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print translate(' '.join(sys.argv[1:]))
    else:
        print translate(u"Someone's cat likes to eat bananas!")