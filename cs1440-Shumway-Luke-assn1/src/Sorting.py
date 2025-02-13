def sort(files):
    """sort lines of text files"""
    fileList = []
    totalLines = []
    for f in files:
        file = open(f)
        fileList.append(file)
        for line in file.readlines():
            totalLines.append(line)
    totalLines.sort()
    for line in totalLines:
        print(line, end="")
