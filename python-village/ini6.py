from collections import Counter
from common import parse_word_list

with open('ini6-dataset.txt') as f:
    words = parse_word_list(f.readline())
    tally = Counter()

    for word in words:
        tally[word] += 1

    for k, v in tally.items():
        print(f'{k} {v}')
