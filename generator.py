#!/usr/bin/env python3
"""
Generate new fictional names from real ones
"""

import random
import sys
import collections


class Generator:
    def __init__(self):
        self.frequencies = collections.Counter()
        self.probabilities = []
        self.all_words = set()
        self.n_length = 3
        for line in sys.stdin:
            words = ["<^>"] + line.rstrip("\n").split(" ") + ["<$>"]
            self.all_words.update(words)
            for i in range(self.n_length):
                for ngram in self._ngrams(words, i + 1):
                    self.frequencies[ngram] += 1
        self.all_words = sorted(self.all_words)

    def _pick(self, weights):
        cumulative_weights = []
        sum_ = 0.
        for weight in weights:
            sum_ += weight
            cumulative_weights.append(sum_)
        random_func = random.random()
        prev = 0
        for cumulative_weight, item in zip(cumulative_weights, self.all_words):
            if prev < random_func < cumulative_weight:
                return item
            prev = cumulative_weight
        raise ValueError()

    def _conditional_probability(self, word, context):
        numerator = context + (word,)
        denominator = context
        try:
            prob = self.frequencies[numerator] * 1. \
                   / self.frequencies[denominator]
        except ZeroDivisionError:
            return 1
        return prob

    @staticmethod
    def _ngrams(words_, count):
        lists = []
        for i in range(count):
            gram = len(words_) - (count - i - 1)
            lists.append(words_[i:gram])
        return zip(*lists)

    def _generate_word(self, words):
        context = words[-2:]
        probs = []
        for word in self.all_words:
            probs.append(self._conditional_probability(word, context))
        return self._pick(probs)

    def generate(self):
        words = ('<^>',)
        while not words or words[-1] != "<$>":
            words += (self._generate_word(words),)
        return words


def main():
    gen = Generator()
    for _ in range(100):
        print(''.join(gen.generate()[1:-1]))


if __name__ == '__main__':
    main()
