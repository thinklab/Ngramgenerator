import re
import time

WORDS_RE = re.compile('\w+', re.UNICODE)
variable = '1234asfer'


def get_words(line):
    line = line.rstrip("\n")
    return WORDS_RE.findall(line)


def clean(pattern, string):
    for i in pattern:
        string = string.replace(i, ' ')
    return string


def get_words2(line):
    pattern = {'.', '-', ';', '!', '?',}
    line = clean(pattern, line)
    return line.rstrip("\n").split(" ")


def new_print_func(string1):
    print(string1)
    print(time._STRUCT_TM_ITEMS)
    print(string1)