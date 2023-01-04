with open('rna-dataset.txt') as f:
    dna = f.readline().strip()
    rna = dna.replace('T', 'U')
    print(rna)
