complement_table = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

with open('revc-dataset.txt') as f:
    dna = f.readline().strip()
    complement = dna[::-1]
    complement = ''.join(complement_table[nucleotide] for nucleotide in complement)
    print(complement)
