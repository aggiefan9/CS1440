# Feel free to start from scratch, or repurpose any of these suggested functions! The world is yours.
#   Well, maybe that was a bit of an over exaggeration. The world isn't only *yours*, but this text file sure is. 

import sys
# TODO:
# import the os module to get access to os.access and os.R_OK
import os

def sendError(string=""):
    '''
Exits the program after displaying `string` as an error message. If no string
input is provided, the default message is "Error! An error was encountered, so
the program is quitting."
    '''
    # Dear Future Dev,
    # The code below is fine. Your work is not needed on `sendError`.
    # You are more than welcome to edit the string literal, especially to make
    # a more vocal and unique quack.
    if string == "":
        string = "Error! An error was encountered, so the program is quitting."
    print(f"""\
!!!QUACK!!!
================================================================================
{string}
================================================================================
!!!QUACK!!!
""")
    sys.exit(1)


def convertToLower(charCode):
    '''
Convert the given character code to a single plain-text lowercase character.
Returns a single character.
    '''
    if 0 <= eval(charCode) <= 25:
        return chr(int(charCode) + 97)
    else:
        return ""


def convertToUpper(charCode):
    '''
Convert the given character code to a single plain-text uppercase character.
Returns a single character.
    '''
    if 0 <= eval(charCode) <= 25:
        return chr(int(charCode) + 65)
    else:
        return ""


def convertToSpecialChar(charCode):
    '''
Convert the given character code to a single plain-text special character.
Returns a single character.
    '''
    if charCode[0] == "A" and len(charCode) >= 2 and 0 <= eval(charCode[1:]) <= 32:
        return chr(int(charCode[1:]) + 32)
    elif charCode[0] == "B" and len(charCode) >= 2 and 0 <= eval(charCode[1:]) <= 5:
        return chr(int(charCode[1:]) + 91)
    elif charCode[0] == "C" and len(charCode) >= 2 and 0 <= eval(charCode[1:]) <= 3:
        return chr(int(charCode[1:]) + 123)
    else:
        return ""


def getFile():
    '''
Prompt the user for the text file. Verify the file's existence.
Open the file and return the opened file object if the input is valid.
    '''
    print("Your current working directory is: " + os.getcwd())
    textFile = input("Please select a text file to parse: ")
    if os.access(textFile, os.R_OK) == True:
        file = open(textFile)
        return file
    else:
        sendError("The file you selected does not exist, or you do not have the required permissions to access it.")


def decryptCharacter(character):
    '''
Decrypts a single DuckieCrypt character. Returns a single character
    '''
    if character[0] == "^":
        return convertToUpper(character[1:])
    elif character[0] == "_":
        return convertToLower(character[1:])
    elif character[0] == "+":
        return convertToSpecialChar(character[1:])
    else:
        return ""


def decryptLine(line):
    '''
Decrypt a single line of DuckieCrypt. Returns a built string
    '''

    output = ""
    lst = line.split()
    for i in lst:
        output += str(decryptCharacter(i))
    return output

# DEV NOTES:
# I'm not sure what to do next... Maybe I should consult doc/Plan.md?
if __name__ == '__main__':
    file = getFile()
    for line in file.readlines():
        print(decryptLine(line))
    file.close()
