from common import parse_integer_list

with open('ini2-dataset.txt') as f:
    a, b = parse_integer_list(f.readline())

print(a**2 + b**2)
