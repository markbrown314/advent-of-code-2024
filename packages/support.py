def load_split_list(filename, sep=' '):
    input_list = []
    with open(filename) as f:
        for line in f:
            input_list.append(line.split(sep))
    return input_list

def load_char_list(filename):
    with open(filename) as f:
        return list(f.read())
    
def load_string(filename):
    with open(filename) as f:
        return f.read()