def head(files, lines=10):
    """output the first part of files"""
    numLines = int(lines)
    files = [x for x in files]
    for f in files:
        file = open(f)
        totalLines = file.readlines()
        if len(files) > 1:
            print("==> " + file.name + " <==")
        for i in range(numLines):
            print(totalLines[i], end="")
        print()


def tail(files, lines=10):
    """output the last part of files"""
    numLines = int(lines)
    files = [x for x in files]
    for f in files:
        file = open(f)
        totalLines = file.readlines()
        if len(files) > 1:
            print("==> " + file.name + " <==")
        for i in range(numLines, 0, -1):
            if i <= len(totalLines):
                print(totalLines[len(totalLines) - i], end="")
        print()
