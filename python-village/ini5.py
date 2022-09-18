with open('ini5-dataset.txt') as f:
    for i, line in enumerate(f.readlines()):
        if (i + 1) % 2 == 0:
            print(line.strip())
