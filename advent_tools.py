
def read_lines(filename):

    file1 = open(filename, 'r')
    lines = file1.readlines()

    stripped_lines = []
    for line in lines:
        stripped_line = line.strip()
        stripped_lines.append(stripped_line)

    return stripped_lines
