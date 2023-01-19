from common import parse_integer_list

with open('ini3-dataset.txt') as f:
    mess = f.readline().strip()
    a, b, c, d = parse_integer_list(f.readline())

print(' '.join([mess[a:b + 1], mess[c:d + 1]]))
