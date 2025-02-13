def wc(files):
    """print newline, word, and byte counts for each file"""
    totalLines = 0
    totalWords = 0
    totalBytes = 0
    for f in files:
        file = open(f)
        lines = 0
        words = 0
        bytes = 0
        fileLines = file.readlines()
        lines += len(fileLines)
        fileWords = []
        for l in fileLines:
            bytes += len(l)
            fileWords.append(l.split())
        for i in fileWords:
            words += len(i)
        totalLines += lines
        totalWords += words
        totalBytes += bytes
        print(format(lines, ">8"), end=" ")
        print(format(words, ">8"), end=" ")
        print(format(bytes, ">8"), end="  ")
        print(file.name)
    if len(files) > 1:
        print(format(totalLines, ">8"), end=" ")
        print(format(totalWords, ">8"), end=" ")
        print(format(totalBytes, ">8"), end="  ")
        print("total")
