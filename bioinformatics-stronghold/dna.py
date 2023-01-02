from collections import Counter

with open('dna-dataset.txt') as f:
    dna_string = f.readline().strip()
    frequency = Counter()

    for nucleotide in dna_string:
        frequency[nucleotide] += 1

    print(f"{frequency['A']} {frequency['C']} {frequency['G']} {frequency['T']}")
