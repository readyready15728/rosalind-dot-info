def find_all_substrings(s, subs):
    found_indices = []
    current_index = 0

    while current_index < len(s):
        try:
            found_index = s.index(subs, current_index)
            # Problem statement uses 1-based indexing
            found_indices.append(found_index + 1)
            current_index = found_index + 1
        except:
            break

    return found_indices

with open('subs-dataset.txt') as f:
    dna = f.readline().strip()
    motif = f.readline().strip()

print(' '.join(str(i) for i in find_all_substrings(dna, motif)))
