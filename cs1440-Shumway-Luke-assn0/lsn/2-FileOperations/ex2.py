import os
import sys
from ex1 import getFileSafely
# If the above import is used, be sure *no additional output is printed* by
#   getFileSafely, otherwise the tests will fail.

def printContents1(file):
    '''
    This function will print the contents of a file object using one of the
    methods for reading the contents of files.

    `file` is an opened file object
    '''
    print(file.read(), end="")


def printContents2(file):
    '''
    This function will print the contents of a file object using one of the
    other methods for reading the contents of files.

    `file` is an opened file object
    '''
    tmp = file.readlines()
    file.seek(0)
    for i in range(len(tmp)):
        print(file.readline(), end="")

def printTwice(filename):
    ''' TODO:
        1:  Open the file object *safely*.
            * Why don't I reuse something I've made before?
    f = a file object
        2:  Print it the first time
    printContents1(f)
        3:  Rewind the file
        4:  Print the file a second time
    printContents2(f)
        5:  Close the file
    f.close()
    '''
    fileObj = getFileSafely(filename)
    printContents1(fileObj)
    fileObj.seek(0)
    printContents2(fileObj)
    fileObj.close()
    # Double check that there are no extra newline characters being printed!
    # If everything *seems* right but you're failing the test, printing an extra
    #   a new-line is most likely the culprit.
    # Hint: What does the print function output at the `end`?

    pass

if __name__ == '__main__':
    cwd = os.getcwd()
    print(f"Please enter a file path relative to {cwd}")
    filename = input("File Path: ")
    printTwice(filename)
