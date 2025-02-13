# CS 1440 Assignment 0 Hints

## Students' advice from last semester

*   Make sure you have the whole GitLab thing working from the day the assignment is due that way you won't stress about it the last day.
*   I would give the advice for them to practice function implementation and planning to prepare for nested functions. Calling a bunch of functions from the main function as a lot of people do just isn't an option for this assignment. 
*   One major setback was trying to use Git. I couldn't figure out how to push my code or make commits. I struggled quite a bit with figuring that out, but now I think I understand it a lot better. I still am not super proficient in the Git world and commits especially confuse me, but I'll keep learning.
*   Start early and break it down piece by piece. You don't have to do a lot in a day just a little piece will help a ton.
*   Give yourself enough time to write the `Plan.md` out fully and take advantage of it while coding.
*   Start early, like 'day one' early. Allot an hour a day and stick to it.
*   I made sure to fully read through all of the directions and then take time to make a plan (both writing it down and mentally going over what I wanted to do).
*   I figured out the encryption table on my own using the DuckieEncrypter because I forgot it was posted on the instructions. But figuring it out myself and writing down a basic table for it helped me understand it better and it was easy to write the program.
*   When I was implementing my code, I had another test program open which I would use to test random different things without dealing with all of the functions and code in the actual program.
*   I carefully examined the flow of information throughout the program which better helped me to understand errors.
*   Using the REPL to debug my functions was helpful.
*   Follow the Plan.md document.  It really makes a difference.  This was the first time that I planned the code that in depth.  Most of the time I spent planning.  I only spent around an hour and a half coding.  The rest of the time was spent planning and testing.  I also only spent a couple minutes debugging out the final problems.
*   I wish I had planned for more test cases as I designed my algorithms because I later found out that there were a lot of things I hadn't accounted for when I ran my code and experienced a lot of bugs.
*   After you think your code is complete, run ALL the tests. If you test 3 of the files and they all work, don't think you're completely done. There's probably something you're missing that would allow you to pass a different test. Make sure you go through all of them and know exactly what the assignment is asking of you.
*   I forgot about the `.isnumerical()` method and so that set me back a lot. More setbacks were caused when I ran the invalid texts and realized that my program didn't react properly to those, and so when I thought I was done I really wasn't. 
*   I didn't completely understand what `pass` does in Python, and was expecting it to do something different when evaluating invalid characters.  In Python, `pass` literally does nothing.  By the time it was finished I had deleted all of them from my program.



## Erik's Hints

0. Familiarize yourself with the `demo/duckieEncrypter.py` file to assist you in understanding DuckieCrypt. When invoking the file, add the optional argument `-h` or `--help` for a detailed usage message.
1. ASCII characters were of significant importance in the creation of DuckieCrypt. In fact, the mapping of the integer portions of the character codes follow similar patterns as the mapping of ASCII characters. While trying to create the DuckieDecrypter and learning how to handle DuckieCrypt, keep your ASCII character table handy!
2. An average implementation of the DuckieDecrypter can be done in a relatively short amount of code (100-200 lines, or less). Don't over think the assignment and write redundant code that can be accomplished by Python's built in tools.
3. Familiarize yourself with these key functions, which are integral to completing the DuckieDecrypter, as well as completion of the learning exercises associated with this assignment.
    * `chr()`
    * `ord()`
    * `int()`
    * `len()`
    * `open()`
    * `close()`
    * `os.R_OK`
    * `os.access()`
    * `print()`
    * `str.split()`
    * and many more!
4.  Run `help([function_name])` in the REPL to learn more about the functions you will use:
    ```
    $ python -i
    >>> help(print)
    Help on built-in function print in module builtins:

    print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    ...

    >>> help(str.split)

    Help on method_descriptor:
    split(self, /, sep=None, maxsplit=-1)
    Return a list of the words in the string, using sep as the delimiter string.
    ...
    ```
5. After you develop the logic looks at the flags to  determine the type of each DuckieCrypt character, how much different will it be to recognize the special characters group?
6. Be sure to test the DuckieDecrypter against invalid characters!  Run your program with the files `data/test/invalid0.txt`, `data/test/invalid1.txt`, and `data/test/invalid2.txt`. 
