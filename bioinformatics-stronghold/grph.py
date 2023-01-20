from itertools import combinations
from common import parse_fasta_lines

k = 3

with open('grph-dataset.txt') as f:
    fasta_dict = parse_fasta_lines(f.readlines())

for s, t in combinations(fasta_dict.keys(), 2):
    if fasta_dict[s][-k:] == fasta_dict[t][:k]:
        print(f'{s} {t}')
    if fasta_dict[t][-k:] == fasta_dict[s][:k]:
        print(f'{t} {s}')
