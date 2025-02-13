import os

def getFileAsString(file):
    '''
    Returns the contents of a text file as a string from the beginning of the file. File is an opened file with write permissions. This tool does *not* close a file when it is finished.
    '''
    file.seek(0)
    return file.read()


def printContentsOfFile(fileName):
    # TODO:
    # 0) Open the file specified by `fileName`
    fileObj = open(fileName)
    # 1) Give the file to the `getFileAsString` function
    read = getFileAsString(fileObj)
    # 2) Print the string returned above
        # Double check that there are no extra newline characters being printed!
        # If everything *seems* right but you're failing the test, printing an extra
        #   a new-line is most likely the culprit.
        # Hint: What does the print function output at the `end`?
    print(read, end="")
    # 3) Close the file
    fileObj.close()

if __name__ == '__main__':
    # `os.getcwd()` returns the (C)urrent (W)orking (D)irectory as a string.
    # Synonymous to `pwd` in the shell
    cwd = os.getcwd()
    print(f"Please enter a file path relative to {cwd}")
    fileName = input("File Path: ")
    printContentsOfFile(fileName)
