def hamming_distance(s, t):
    if len(s) != len(t):
        raise ValueError('Sequences must have equal lengths')

    distance = 0

    for i in range(len(s)):
        if s[i] != t[i]:
            distance += 1

    return distance

with open('hamm-dataset.txt') as f:
    s = f.readline().strip()
    t = f.readline().strip()

print(hamming_distance(s, t))
