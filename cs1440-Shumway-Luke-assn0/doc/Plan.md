*Adapted from https://htdp.org/2020-5-6/Book/part_preface.html*

# 0.  From Problem Analysis to Data Definitions

The program needs to take a file path input from the user, check to see if its valid, create a file object from valid inputs,
    and read the contents of said file, converting special DuckieEncrypted characters into plain-text.

The required information needed is the file path, "filename" (string); "data/msg1.txt";
    and the file object, "file"(file, or _io.TextIOWrapper); <_io.TextIOWrapper name='data\\msg1.txt' mode='r' encoding='cp1252'>;
    with the following information as temporary information needed:
        lines of text in the file object, "line" (string); "+A2 +A1 +A0 _17 +A19 +A32 _11 +A17 _24 +A0 _22 +A10 _13 _19 +A0 ..." (line was too long to actually put in here);
        DuckieCrypt characters (string); "+A1";
        decrypted DuckieCrypt characters (string (or char)); "!";
        and finally, constructed lines of plain-text comprised of decrypted DuckieCrypt characters, "newlines" (string); ""! r3@l1y w*nt [o push th!$ t# !t'$ l!m(t ...." (same as before, too long);


# 1.  System Analysis

function requirements
    convert DuckieCrypt to a lowercase letter
        Input: DuckieCrypt chatacter (string beginning with "_") [from other function]
        Output: plain-text lowercase letter (string) [output file created]
    convert DuckieCrypt to an uppercase letter 
        Input: DuckieCrypt character (string beginning with "^") [from other function]
        Output: plain-text uppercase letter (string) [output file created]
    convert DuckieCrypt to special character
        Input: DuckieCrypt character (string beginning with "+") [from other function]
        Output: plain-text special character (strings such as punctuation, etc.) [output file created]
    obtain and open a file specified by the user
        Input: File path (string) [via interactive prompt] {data is incorporated from the os (the cwd)}
        Function: check to see if filepath is valid via os.access()
        Output: file object (file, or _io.TextIOWrapper) [output file created]
    decrypt DuckieCrypt character by character
        Input: DuckieCrypt character (string) [from other function]
        Function: Call specific function based on DuckieCrypt flag
        Output: plain-text character (string) [output file created]
    decrypt DuckieCrypt line by line
        Input: Line of text (string) [from other function]
        Function: For each character, call the function to decrypt it and add it to another string variable
        Output: Line of text (the string variable mentioned above (string)) [output file created]


# 2.  Functional Examples

function to obtain input from the user
    print to the command line the current working directory
    prompt the user for the path of a file to parse
    verify the existence and readability (permissions) of the given file path using os.access()
        if the file does, indeed, exist, and is able to be parsed, open the file and create a file object for it
            eg. "data/msg1.txt" from within the cs-1440-lastName-firstName-assn0 directory
        if not, call the error function with the message "The file either does not exist, or you do not have the required permissions to access it"
            eg. "datta/msg1.txt" from within the aforementioned directory, or "badFile/pathing.png" (assuming the file does not exist)

function to decrypt line of DuckieCrypt
    obtain actual parameter "line" from function caller
    create a list variable for the "old line" of text from the parameter using the str.split() method to separate the DuckieCrypt characters
    iterate through each item in the list and call the function to decrypt said character
        concatenate the output of said function to a "new line" string variable
    return the "new line" string variable

function to decrypt character of DuckieCrypt
    obtain actual parameter "character" from function caller
    check the first character of the "old character" parameter
        if the first character is "^", call the function to decrypt an uppercase letter
        else-if the first character is "_" call the function to decrypt a lowercase letter
        else-if the first character is "+" call the function to decrypt a special character
    return the output of the function called above

function to decrypt lowercase letter
    obtain actual parameter "character" from function caller
    slice the first character of the string (the flag) off and convert the remainder to an integer
    return the result of chr() with the integer value obtained above plus 97 as the parameter

function to decrypt uppercase letter
    obtain actual parameter "character" from function caller
    slice the first character of the string (the flag) off and convert the remainder to an integer
    return the result of chr() with the integer value obtained above plus 65 as the parameter

function to decrpyt special character
    obtain actual parameter "character" from function caller 
    slice the first character of the string (the flag) off and test the second (now first) character of the remaining string
    if the first character is A, return the result of chr() with the integer value obtained above plus 32 as the parameter
    else-if the first character is B, return the result of chr() with the integer value obtained above plus 91 as the parameter
    else-if the first character is C, return the result of chr() with the integer value obtained above plus 123  as the parameter


# 3.  Function Template

function to obtain input from the user
    print("Your current working directory is: " + os.getcwd())
    textFile = input("Please select a text file to parse: ")
    if os.access(textFile, os.R_OK) == True:
        file = open(textFile)
        return file
    else:
        sendError("The file you selected does not exist, or you do not have the required permissions to access it.")

function to decrypt line of DuckieCrypt
        output = ""
    lst = line.split()
    for i in list:
        output += decryptCharacter(i)
    return output

function to decrypt character of DuckieCrypt
    if character[0] == "^":
        return convertToUpper(character[1:])
    elif character[0] == "_":
        return convertToLower(character[1:])
    elif character[0] == "+":
        return convertToSpecialChar(character[1:])

function to decrypt lowercase letter
    return chr(int(charCode) + 97)

function to decrypt uppercase letter
    return chr(int(charCode) + 65)

function to decrpyt special character
    if charCode[0] == "A":
        return chr(int(charCode[1:]) + 32)
    elif charCode[0] == "B":
        return chr(int(charCode[1:]) + 91)
    elif charCode[0] == "C":
        return chr(int(charCode[1:]) + 123)


# 4.  Implementation

See duckieDecrypter.py


# 5.  Testing

Testing
    It is assumed that you either have access to a pre-encrypted text file, or the duckieEncrypter.py program
        assuming you do not have a pre-encrypted text file, take a plain-text text file and encrypt it using the duckieEncrypter.py program
    Now that you have access to an encrypted file, run the duckieDecrypter.py program (via whatever method you choose, this example will use the command line with cs-1440-lastName-firstName-assn0 as the cwd)
        It is also assumed you know the relative pathing of the file chosen to decrypt relative to the aforementioned cwd
        EXAMPLE OF HOW TO RUN PROGRAM
            assuming you have the code for this program in your desktop directory
            open your command line and cd into desktop\cs-1440-lastName-firstName-assn0 (the first and last names will be replaced with whoever's code you have (mine is shumway-luke))
            from the cwd run 'python src\duckieDecrypter.py'
            you will notice that your cwd is displayed, and the program asks you to select a file to parse. here's where the journey begins
    First let us test the bad example (as it is shorter)
        when prompted, enter a bad pathing of the desired file, or the pathing of any nonexistent file
        you should be confronted with the appropriate error message informing you that the selected file does not exist or cannot be read
        BONUS POINTS: if you know the pathing for a file that does exist, but that you cannot edit, a similar error will be thrown
        NOTE: entering the pathing of a directory instead of a file will result in a "permission denied" error
    Now lets test a good example (for a file path, don't worry, there will be one more bad example)
        when prompted, enter the correct pathing of the file you with to decrypt
        you should see the correct plain-text output of the file as you had before encrypting it
    Now for another bad example
        before running the program, only encrypt every other word of the document (or every other letter if you so desire)
            this will produce characters the duckieDecrypter will not recognize
        Alternatively, if you possess the data directory in this project, you can run any of the invalid*.txt files under the test directory
        follow the good example above and enter the correct pathing for your semi-encrypted file
        you should see only the decrypted DuckieCrypt characters (the plain-text present is simply ignored)
        NOTE: this accounts for any modified DuckieCrypt characters with bad flags
    because of the simplicity of the program, the only things to test for are bad flags in the characters and plain-text characters, so this testing session was fairly short. But don't worry, we can only go up from here ;)