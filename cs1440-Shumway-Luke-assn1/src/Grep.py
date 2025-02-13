def grep(pattern, files, match=True):
    """print lines that match patterns"""
    pattern = pattern
    match = match
    for f in files:
        file = open(f)
        for line in file.readlines():
            if match and pattern in line:
                print(line, end="")
            elif not match and pattern not in line:
                print(line, end="")
