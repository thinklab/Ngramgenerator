from __future__ import print_function
import sys
import collections
FREQ = collections.defaultdict(int)
ALL_WORDS = set()
N = 4

def generate():
	words = ('<^>')
	while not words or words[-1]!
		pass

for line in sys.stdin: #в
	words = ["<^>"] + line.rstrip("\n").split(" ")+["<$>"]
	ALL_WORDS.update(words)
	for n in range(N):
		for ngram in ngrams(words,n+1):
			FREQ[ngram]+=1

ALL_WORDS = sorted(ALL_WORDS)

print('* Generating')
for i in range(10000):
	print(''.join(generate()[1:-1]))
