#!/usr/bin/python

import urllib
import re


PIRO_EXPR = re.compile(r'.*class="Text">([^<]+)', re.DOTALL|re.MULTILINE)

def get_message():
    piro = urllib.urlopen('http://www.perashki.ru/Piro/Random/').read()
    match = PIRO_EXPR.match(piro)
    return match.group(1)


def test():
    print get_message()


if __name__ == '__main__':
    test()