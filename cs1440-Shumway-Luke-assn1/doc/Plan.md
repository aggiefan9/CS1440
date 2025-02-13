# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

The function of this program is to imitate the unix-style text tools. This means there is a need to open files, read their contents, and print them to the screen in a number of different ways.
the following functions will accomplish this in the following ways.
*   cat: open and read the contents of a file and print it to the screen verbatim.
*   tac: open and read the contents of a file in reverse and print it to the screen reversed (with each line being normal)
*   cut: open and read the contents of a file and print it (minus some sections specified by the user) to the screen.
*   paste: open and read the contents of several files and print them (line by line(line 1 of file 1 then line 1 of file 2, then line 2 of file 1, etc.)) to the screen
*   grep: open and read the contents of a file and print the parts of it matching a certain pattern specified by the user to the screen.
*   head: open and read the contents of a file and print the first portion (length specified by the user) to the screen verbatim
*   tail: open and read the contents of a file and print the last portion (length specified by the user) to the screen
*   sort: open and read the contents of a file; sort the lines contained therein by a method (ascending, descending) specified by the user and print the lines in new order to the screen
*   wc: open and read the contents of a file; determine the number of newlines, words (separated by spaces) and bytes (characters) contained in said file and print it to the screen

A good solution will take the arguments entered by the user in the command line and call the appropriate function (tool), printing the appropriate output to the screen, leaving the file itself untouched
This will utilize:

Known Knowns:
* handling and reading sys.argv
* opening a file
* printing lines of a file
* sorting a list
* removing portions of a list (and/or a string(probably using the slice operator))
* finding an key within a list and/or string (in() function)
* utilizing (in this case printing) a certain number of items in a list and/or string (slice operator)

Known Unknowns: (kind of)
* inserting strings into another string (probably a couple slice operators and concatenation)
* counting the number of characters/strings that match a certain criteria within a string and/or list (probably in() and .split())
* determining whether an -optional argument has been used (right now I just don't know where to use it, within tt.py or the individual tools)

## Phase 1: System Analysis *(10%)*

**Deliver:**

*   List all of the data that is used by the program, making note of where it comes from.
*   Explain what form the output will take.
*   Describe what algorithms and formulae will be used (but don't write them yet).

The program will use data first that comes from the user in the form of a command line entry. This will come from the input, and will be stored in sys.argv.
From there, the program will use the sys.argv to call the correct function (the first argument after tt.py) and will use the remaining arguments as parameters for said function.
Then the program will use the appropriate parameter from the function call to open a file with the specified path, reading the contents of said file.

The output will always be something printed to the screen, and then discarded unless using > from the shell.

The following algorithms will be utilized.
find items within sys.argv that match certain criteria (the text tool function, any -optional parameters, file names)
printing each line of a file (forwards and backwards using for loops with the appropriate range)
printing the contents of a csv file without a column specified by the user (via the command line arguments)
searching for a substring within a string within an item of a list and printing said item (the line of the file containing the substring)
printing the first (or last) lines of a file using the slice operator
finding the length of a list, the length of each item within said list, and the number of spaces within each item
sorting the items of a list lexically.

## Phase 2: Design *(30%)*

**Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.

tt.py
determine which function (tool) to call
    if sys.argv[1] is equal to cat, call cat function with the remaining items in sys.argv as subsequent parameters
    else-if sys.argv[1] is equal to tac, call tac function with the remaining items in sys.argv as subsequent parameters
    else-if sys.argv[1] is equal to cut
        if sys.argv[2] is equal to -f, call cut function with first parameter as sys.argv[3] and the remaining items in sys.argv as subsequent parameters
        else call cut function with first parameter as 'None' and the remaining items in sys.argv as subsequent parameters
    else-if sys.argv[1] is equal to paste, call paste function with the remaining items in sys.argv as subsequent parameters
    else-if sys.argv[1] is equal to grep
        if sys.argv[2] is equal to -v, call grep function with first parameter as '-v' and the remaining items in sys.argv as subsequent parameters
        else call grep function with first parameter as 'None' and the remaining items in sys.argv as subsequent parameters
    else-if sys.argv[1] is equal to head
        if sys.argv[2] is equal to -n, call head function with first parameter as sys.argv[3] and the remaining items in sys.argv as subsequent parameters
        else call head function with first parameter as '10' and the remaining items in sys.argv as subsequent parameters
    else-if sys.argv[1] is equal to tail
        if sys.argv[2] is equal to -n, call tail function with first parameter as sys.argv[3] and the remaining items in sys.argv as subsequent parameters
        else call tail function with first parameter as '10' and the remaining items in sys.argv as subsequent parameters
    else-if sys.argv[1] is equal to sort, call sort function with the remaining items in sys.argv as subsequent parameters
    else-if sys.argv[1] is equal to wc, call wc function with the remaining items in sys.argv as subsequent parameters

cat function
    obtain parameters for file path(s) from function caller
    for each parameter,
        open file as a new file object (if not, crash using pythons errors)
        list = file.readlines
        for each line in list
            print line

tac funtion
    obtain parameters for file path(s) from function caller
    for each parameter,
        open file as a new file object (if not, crash using pythons errors)
        list = file.readlines
        for i in range(length(list) - 1, 0)
            print list[i]

cut function
    obtain parameters from function caller
    create empty list, extractedFields, to store the lines that will be extracted
    create another empty list, filelist, to store opened file objects
    for each parameter in parameter list (sys.argv?)
        if parameter isdigit
            append (parameter minus one) to extractedFields
        else, append a fileobject opened from parameter to filelist
    for each file in fileList
        create a list, originallines, and fill it with file.readlines
        create a list, templines, and fill it with a list of lists, where each sublist is a line from originallines, and each of the sublist items is the product of originallines.split with "," as the separator key
        for each line in templine
            for each field in extractedFields
                print the corresponding field from templine

paste function
    obtain parameters for file path(s) from function caller
    create blank list, filelist, to store opened file objects
    for each parameter,
        open file as a new file object
        append new file object to list
    for i in range(length of longest file)
        create empty string variable newline
        for j in range(length of filelist)
            if i is less than the length of filelist[j]
                add filelist[j].readlines[i] to newline
            if j is less than (the length of the file minus 1)
                add "," to newline
        print newline

grep function
    obtain parameters from function caller
    if option perameter is equal to "-v", set contains equal to False
    else, set contains equal to True
    if key parameter is not None, set a key variable equal to the key parameter
    else, call the usage function with the "Please provide a pattern and at least one filename" error and the "grep" tool
    if files is not none, 
        for each file parameter, open a new file and append it to a fileList variable.
    else, call the usage function with the "Please provide a pattern and at least one filename" error and the "grep" tool
    for each file in fileList
        append file.readlines to a searchLines list variable.
    for each line in searchLines
        if contains is True and key is in line, print the line
        else-if contains is False and key is not in line, print the line

head function
    obtain parameters from function caller
    set numLines equal to the option parameter
    for each file in the parameters, open a new file object and append it to a fileList variable
    for each file in fileList
        print the filename banner
        for i in range(numLines)
            if i is less than the length of file.readlines, print file.readlines[i]
    

tail function
    obtain parameters from function caller
    set numLines equal to the option parameter
    for each file in the parameters, open a new file object and append it to a fileList variable
    for each file in fileList
        print the filename banner
        for i in range(numLines)
            if i is less than the length of file.readlines, print file.readlines[-i] (length of readlines - i)


sort function
    obtain parameters from function caller
    for each file in parameters, open a new file object and append it to a fileList variable
    for each file in the fileList, append file.readlines to a totalLines variable
    sort totalLines using totalLines.sort()
    for line in totalLines
        print line

wc function
    obtain parameters from function caller
    for each file in parameter list, open a new file object and append it to a fileList variable
    create a variable, totalBytes, and set it equal to 0
    create a variable, totalWords, and set it equal to 0
    create a variable, totalLines, and set it equal to 0
    for each file in fileList
        set file.readlines() equal to a tmpLines variable
        create a variable, bytes, and set it equal to 0
        create a variable, words, and set it equal to 0
        create a variable, lines, and set it equal to the length of tmpLines
        add lines to totalLines
        for each line in tmpLines
            add the length of the line to the bytes variable
            set line.split equal to a tmpSplit variable and add the length of tmpSplit to the words variable
        add bytes to totalBytes
        add words to totalWords
        print the lines variable (end="    ")
        print the words variable (end="    ")
        print the bytes variable (end="    ")
        print the file path
    print the totalLines variable (end="    ")
    print the totalWords variable (end="    ")
    print the totalBytes variable (end="    ")
    print "total"
        
        



## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working Python code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.

tt.py test
    run from the command line in bash (or zshell or whatever) the following code (assuming you are in the main repository)
        python src/tt.py
    notice how the usage function will be called and will inform you of the functionality of the different tools (I wasn't responsible for this code but still it works, at least i didnt break it)


NOTE: from now on it is assumed you are in the root folder of this project
cat test
    run the following from the command line
        python src/tt.py cat
        notice how the "Too few arguments" error was produced and the cat|tac specific usage popped up
    now run the following
        python src/tt.py cat BADFILEPATH (this just means any file path that doesn't actually exist)
        notice how the program quit using python's filenotfound error
    now run the following (this is a good test)
        python src/tt.py cat data/complexity
        notice the contents of data/complexity were printed
    now run the following (to test multiple files (still good))
        python src/tt.py cat data/complexity data/debugging
        notice the contents of both files were printed without error
    now for the last test (a multiple files bad example )
        python src/tt.py cat data/complexity DOESNTEXIST data/debugging (the bad file path can be wherever, not just the middle)
        notice how the contents of the first file (or every good file preceding the bad one) are printed, but the program quits with python's filenotfound error and the contents of every file after the bad one are not printed

tac test
    the same tests are run (using the same files)
    test #1: python src/tt.py tac
        notice how the "Too few arguments" error was produced and the cat|tac specific usage popped up
    test #2: python src/tt.py tac BADFILEPATH
        notice how the program quit using python's filenotfound error
    test #3: python src/tt.py tac data/complexity
        notice how the contents were printed in reverse order without error
    test #4: python src/tt.py tac data/complexity data/debugging
        notice how the contents of both files were printed in reverse order without error
    test #5: python src/tt.py tac data/complexity DOESNTEXIST data/debugging
        notice how the contents of the first file (or every good file preceding the bad one) are printed, but the program quits with python's filenotfound error and the contents of every file after the bad one are not printed

paste
    the same tests are run (using the new files)
    test #1: python src/tt.py paste
        again, too few arguments and usage help documentation
    test #2: python src/tt.py paste BADFILEPATH
        again, quits using pythons error
    test #3: python src/tt.py paste data/ages8
        functions just like cat, where the contents are printed
    test #4: python src/tt.py paste data/ages8 data/colors8
        the first line printed is a combination of the first two lines, separated by a comma
    test #5: python src/tt.py paste data/ages8 DOESNTEXIST data/colors8
        the program quits using pythons errors without displaying anything
    test #6: python src/tt.py paste data/ages8 data/names10
        the program runs just as the good example above, but the last line contains a comma followed by only the last line in names10

cut
    similar tests are run using a new .csv file
    test #1: python src/tt.py cut
        again, too few arguments and usage help documentation
    test #2: python src/tt.py cut BADFILEPATH
        again, quits using pythons error
    test #3: python src/tt.py cut data/people.csv
        the first field in each line is printed
    test #4: python src/tt.py cut data/people.csv data/colors8
        the first field of people.csv is printed, then the same for colors8
    test #5: python src/tt.py cut data/ages8 DOESNTEXIST data/people.csv
        the program prints out the desired field of the first file, but quits using pythons error and the last file is not printed
    test #6: python src/tt.py cut -f data/people.csv
        the "A comma-separated field specification is required" error is produced
    test #7: python src/tt.py cut -f 4,2 data/people.csv
        the second and fourth fields are printed from each line, with the second first, and the fourth afterwards

head
    test #1: python src/tt.py head
        again, too few arguments and usage help documentation
    test #2: python src/tt.py head BADFILEPATH
        again, quits using pythons error
    test #3: python src/tt.py head data/ages8
        the first 10 lines are printed of each file
    test #4: python src/tt.py head data/ages8 DOESNTEXIST data/colors8
        the program quits using pythons errors without displaying anything

tail
    test #1: python src/tt.py tail
        again, too few arguments and usage help documentation
    test #2: python src/tt.py tail BADFILEPATH
        again, quits using pythons error
    test #3: python src/tt.py tail data/ages8
        the last 10 lines are printed of each file
    test #4: python src/tt.py tail data/ages8 DOESNTEXIST data/colors8
        the program quits using pythons errors without displaying anything

sort
    test #1: python src/tt.py sort
        again, too few arguments and usage help documentation
    test #2: python src/tt.py sort BADFILEPATH
        again, quits using pythons error
    test #3: python src/tt.py sort data/ages8
        the lines of both files are sorted lexically, so capitals preceed lowercase
    test #4: python src/tt.py sort data/ages8 DOESNTEXIST data/colors8
        the program quits using pythons errors without displaying anything


wc
    test #1: python src/tt.py wc
        again, too few arguments and usage help documentation
    test #2: python src/tt.py wc BADFILEPATH
        again, quits using pythons error
    test #3: python src/tt.py wc data/ages8
        functions just like cat, where the contents are printed
    test #4: python src/tt.py wc data/ages8 DOESNTEXIST data/colors8
        the program quits using pythons errors without displaying anything
    test #5: python src/tt.py wc data/ages8 data/names10
        the file name banners are printed, and each files line, word, and byte counts are printed, followed by the total



## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Review the project to ensure that all required files are present and in correct locations.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
    *   Run through your test cases to avoid nasty surprises.


## Phase 6: Maintenance

**Deliver:**

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to
        *   anybody besides yourself?
        *   yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading
        *   your computer's hardware?
        *   the operating system?
        *   to the next version of Python?
