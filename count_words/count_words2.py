#!/usr/bin/env python3
import operator
import sys
import time

from count_words.tools import new_print_func
from count_words.tools import str_tools as name1


def timing_decorator(count_words):
    def wrapper(*args, **kwargs):
        before = time.time()
        print("Время до - ", before)
        new_func = count_words(*args, **kwargs)
        after = time.time()
        delta = str((after - before))
        print("Время после - ", after)
        print("Время выполнения - ", delta)
        return new_func
    return wrapper


@timing_decorator
def count_words(file_in, file_out):
    all_words = {}
    print(file_in, file_out)
    with open(file_in) as fin:
        for line in fin:
            #print(line)
            words = name1.get_words2(line)
            #print(words)
            for word in words:
                if word=='':
                    continue
                if word in all_words:
                    all_words[word] += 1
                else:
                    all_words[word] = 1
    all_words_srt = sorted(all_words.items(), key=operator.itemgetter(1))
    with open(file_out, "a") as fout:
        for word in all_words_srt:
            line = str(word)
            fout.write(line + '\n')


def main():
    count_words(sys.argv[1],sys.argv[2])
    string1= name1.variable
    new_print_func(string1)


if __name__ == '__main__':
    main()