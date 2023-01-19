from common import parse_fasta_lines

def gc_content(dna):
    gc_count = 0

    for nucleotide in dna:
        if nucleotide == 'G' or nucleotide == 'C':
            gc_count += 1

    return 100 * gc_count / len(dna)

with open('gc-dataset.txt') as f:
    fasta_dict = parse_fasta_lines(f.readlines())

gc_contents =  {k: gc_content(v) for k, v in fasta_dict.items()}
maximum_label = max(gc_contents, key=gc_contents.get)
print(maximum_label)
print(f'{gc_contents[maximum_label]:.6f}')
