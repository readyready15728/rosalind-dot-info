def parse_integer_list(line):
    return list(map(int, line.strip().split(' ')))

def parse_word_list(line):
    return line.strip().split(' ')

def parse_fasta_lines(lines):
    fasta_dict = {}
    current_label = None

    for line in lines:
        if line[0] == '>':
            current_label = line.strip()[1:]
            fasta_dict[current_label] = ''
        else:
            fasta_dict[current_label] += line.strip()

    return fasta_dict
