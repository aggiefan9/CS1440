from Usage import usage
def cut(files, fields=[1]):
    """remove sections from each line of files"""
    error = True
    for i in fields:
        if int(i) > 0:
            error = False
    if error:
        usage("A comma-separated field specification is required", "cut")

    fields = [int(x) - 1 for x in fields if x > 0]
    fields.sort()
    for f in files:
        file = open(f)
        ogLines = file.readlines()
        splitLines = [x.split(",") for x in ogLines]
        for line in splitLines:
            for f in range(len(fields)):
                if f < len(fields) - 1:
                    print(line[fields[f]], end=",")
                elif fields[f] == len(line) - 1:
                    print(line[fields[f]], end="")
                else:
                    print(line[fields[f]])


def paste(files):
    """merge lines of files"""
    mergedLines = []
    for f in files:
        file = open(f)
        oldLines = file.readlines()
        if len(mergedLines) == 0:
            while len(mergedLines) < len(oldLines):
                mergedLines.append([])
        while len(mergedLines) < len(oldLines):
            mergedLines.append([""])
        for i in range(len(mergedLines)):
            while len(mergedLines[0]) > len(mergedLines[i]):
                mergedLines[i].append("")
        for i in range(len(oldLines)):
            mergedLines[i].append(oldLines[i][:-1])
        for i in range(len(mergedLines)):
            while len(mergedLines[0]) > len(mergedLines[i]):
                mergedLines[i].append("")
    for line in mergedLines:
        for i in range(len(line)):
            if i < len(line) - 1:
                print(line[i], end=",")
            else:
                print(line[i])
