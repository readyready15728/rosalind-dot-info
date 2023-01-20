from collections import Counter
from common import parse_fasta_lines

nucleotides = ('A', 'C', 'G', 'T')

def generate_profile_matrix(strings):
    matrix = {}

    for nucleotide in nucleotides:
        matrix[nucleotide] = [0] * len(strings[0])

    for string in strings:
        for i, nucleotide in enumerate(string):
            matrix[nucleotide][i] += 1

    return matrix

def generate_consensus_string(matrix):
    most_common_nucleotides = [Counter() for _ in range(len(matrix[nucleotides[0]]))]

    for nucleotide in nucleotides:
        for i in range(len(matrix[nucleotide])):
            most_common_nucleotides[i][nucleotide] += matrix[nucleotide][i]

    consensus_string = ''

    for counter in most_common_nucleotides:
        consensus_string += counter.most_common(1)[0][0]

    return consensus_string

with open('cons-dataset.txt') as f:
    fasta_dict = parse_fasta_lines(f.readlines())

profile_matrix = generate_profile_matrix(list(fasta_dict.values()))
print(generate_consensus_string(profile_matrix))
