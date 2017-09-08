#!/usr/bin/env python3
"""
Generate some War&Peace lookalike words.


"""
from __future__ import print_function
import sys
import collections

FREQ = collections.defaultdict(int)
ALL_WORDS = set()
#n of gramm(length)
N = 3


def frequency(ngram):
    return FREQ[ngram]


def pick(weights, items):
    cumulative_weights = []
    sum = 0.
    for weight in weights:
        sum += weight
        cumulative_weights.append(sum)
    import random
    f = random.random()
    # print(f)
    # for cumulative_weight, item in zip(cumulative_weights, items):
    #    print('--', item, cumulative_weight)
    prev = 0
    for cumulative_weight, item in zip(cumulative_weights, items):
        if prev < f < cumulative_weight:
            return item
        prev = cumulative_weight
    raise ValueError()


def conditional_probability(word, context):
    numerator = context + (word,)
    denomenator = context
    p = frequency(numerator) * 1. / frequency(denomenator)
    # print('P', p, context, word, numerator, denomenator, frequency(numerator), frequency(denomenator))
    return p


def ngrams(words, n):
    lists = []
    for i in range(n):
        g = len(words) - (n - i - 1)
        lists.append(words[i:g])
    return zip(*lists)


def generate_word(words):
    context = words[-n:]
    probs = []
    for word in ALL_WORDS:
        probs.append(conditional_probability(word, context))
    word = pick(probs, ALL_WORDS)
    return word


def generate():
    words = ('<^>',)
    while not words or words[-1] != "<$>":
        words += (generate_word(words),)
    return words


"""
        input: file with tokenized (one line one word, space between all letters)
        output: print generated words
"""
for line in sys.stdin:
    words = ["<^>"] + line.rstrip("\n").split(" ") + ["<$>"]
    ALL_WORDS.update(words)
    for n in range(N):
        for ngram in ngrams(words, n + 1):
            FREQ[ngram] += 1
ALL_WORDS = sorted(ALL_WORDS)
print('* Generating')
for i in range(10000):
    print(''.join(generate()[1:-1]))


