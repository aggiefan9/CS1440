def cat(files):
    """concatenate files and print on the standard output"""
    for f in files:
        file = open(f)
        for line in file.readlines():
            print(line, end="")


def tac(files):
    """concatenate and print files in reverse"""
    for f in files:
        file = open(f)
        lines = file.readlines()
        for i in range(len(lines) - 1, -1, -1):
            print(lines[i], end="")
