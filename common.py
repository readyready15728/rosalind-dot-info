def parse_integer_list(line):
    return list(map(int, line.strip().split(' ')))

def parse_word_list(line):
    return line.strip().split(' ')
