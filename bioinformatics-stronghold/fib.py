from common import parse_integer_list

with open('fib-dataset.txt') as f:
    n, k = parse_integer_list(f.readline())

def rabbits(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rabbits(n - 1, k) + k * rabbits(n - 2, k)

print(rabbits(n, k))
