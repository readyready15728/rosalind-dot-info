from common import parse_integer_list

with open('ini4-dataset.txt') as f:
    a, b = parse_integer_list(f.readline())
    total = 0

    for i in range(a, b + 1):
        if i % 2 == 1:
            total += i

    print(total)
