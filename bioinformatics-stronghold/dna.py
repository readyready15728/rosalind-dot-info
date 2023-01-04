from collections import Counter

with open('dna-dataset.txt') as f:
    dna = f.readline().strip()
    frequency = Counter()

    for nucleotide in dna:
        frequency[nucleotide] += 1

    print(f"{frequency['A']} {frequency['C']} {frequency['G']} {frequency['T']}")
