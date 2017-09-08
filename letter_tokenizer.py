#!/usr/bin/env python3
import sys
import re

WORDS_RE = re.compile("\w+",re.UNICODE)


def get_words(line):
    line = line.rstrip("\n")
    return WORDS_RE.findall(line)


for line in sys.stdin.buffer:
    line = line.decode("utf-8",errors="replace")
    words = get_words(line)
    for word in words:
        print(" ".join(word).lower())
