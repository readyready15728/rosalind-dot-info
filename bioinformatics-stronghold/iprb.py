import random
from common import parse_integer_list

with open('iprb-dataset.txt') as f:
    k, m, n = parse_integer_list(f.readline())

# In the following, "A" stands for a dominant allele and "a" stands for recessive
organisms = []

for _ in range(k):
    organisms.append(['A', 'A'])

for _ in range(m):
    organisms.append(['A', 'a'])

for _ in range(n):
    organisms.append(['a', 'a'])

runs = 1_000_000
has_dominant = 0

for _ in range(runs):
    parent_1, parent_2 = random.sample(organisms, 2)
    offspring = [random.choice(parent_1), random.choice(parent_2)]

    if 'A' in offspring:
        has_dominant += 1

print(has_dominant / runs)
