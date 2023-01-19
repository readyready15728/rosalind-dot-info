with open('ini5-dataset.txt') as f:
    lines = [line.strip() for line in f.readlines()]

for i, line in enumerate(lines):
    if (i + 1) % 2 == 0:
        print(line)
