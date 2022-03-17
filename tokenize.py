#!/usr/bin/env python3

"""
Converts unicode book of Leo Tolstoy to little bits for generator
"""

import re
import fileinput

WORDS_RE = re.compile("\w+", re.UNICODE)


def get_words(text_line: str) -> list:
    text_line = text_line.rstrip("\n")
    return WORDS_RE.findall(text_line)


if __name__ == '__main__':
    for line in fileinput.input():
        for word in get_words(line):
            print(" ".join(word.lower()))
