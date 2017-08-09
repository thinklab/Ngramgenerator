#!/usr/bin/env python3
import sys
import re
import operator

WORDS_RE = re.compile('\w+', re.UNICODE)
ALL_WORDS = {}


def get_words(line):
    line = line.rstrip("\n")
    return WORDS_RE.findall(line)


for line in sys.stdin.buffer:
    line = line.decode("utf-8", errors="replace")
    words = get_words(line)
    for word in words:
        #print("".join# (word).lower())
        if word in ALL_WORDS:
            ALL_WORDS[word] +=1
        else:
            ALL_WORDS[word] = 1


ALL_WORDS_srt = {}
ALL_WORDS_srt = sorted(ALL_WORDS.items(), key=operator.itemgetter(1))

for word in ALL_WORDS_srt:
    line = str(word)
    sys.stdout.write(line+'\n')






