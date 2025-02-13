# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

*   A detailed written description of the problem this program aims to solve.
*   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.

This program strives to solve the problem of keeping track of links on a webpage, and visiting each and every link on a page, whilst not revisiting any duplicates, through recursion.
A good solution will implement the 3rd party libraries to save time and successfully visit each and every link from a root URL, keeping track of each link visited, and the time taken to do so. Preserving the functionality of the starter code, with the exception of added recursion and visitation of each link.

Things I know how to do:
* Check the validity of the URL input from user using urlparse
* Recursively call the function crawl() for each link
* Append visited links to a set
* Check the depth and return if max depth has been exceeded
* Pretty much everything else done in the starter code (ie. retain functionality of finding urls, creating absoute urls from urljoin, etc.)

Challenges I forsee:
* Specific error handling without crashing the program (I have a vague idea how to do it, but the specifics are unclear as of yet)
* I've never done anything with KeyboardInterrupt, so I honestly don't know how fun it will be to work with (the challenges are possibly capturing only Ctrl-C as opposed to other key presses)
* NOTE: I just re-read the instructions/README.md again and now I'm pretty sure I know how to handle the error handling, but I'm going to leave that first note in there
* Specific urls that cause problems (the fact that it was put in the README means there will probably be some, and I do not know what urls they are yet and I do not like unknowns)

## Phase 1: System Analysis *(10%)*

**Deliver:**

*   List all of the data that is used by the program, making note of where it comes from.
*   Explain what form the output will take.
*   Describe what algorithms and formulae will be used (but don't write them yet).

Data used in the program:
* root url - string from sys.argv
* max depth - int from sys.argv (OPTIONAL)
* list of visited urls - set of strings - starts empty, and is added to with each call
* current depth - int - starts 0 and is incremented with each recursive call
* urls - passed as parameters with each recursive call, and also obtained from the html tags at each url
* Exceptions - possibly thrown by the crawl(), strings that are printed, without stopping the programs functionality
* total links visited - int - starts as zero, and updated with each new url visited

output:
* any error messages will be printed to the console
* With each new url visited, the url itself will be printed out with increasing indentation (depending on the depth)
* Upon completion (or termination via Ctrl-C) the number of total links visited is displayed, along with the time taken

algorithms/formulae:
* determine the validity of starting url (using urlparse to ensure all the essential pieces of an absolute url are present)
* compare the current depth to the max depth (return if current > max)
* find each url within each webpage (via anchor tags and href attributes)
* determine if each url found has been visited before (whether or not it is in the set of visited links)
* exception handling (if caught, print the message and return out of the current call of crawl())

## Phase 2: Design *(30%)*

**Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.

NOTE: I don't really know how much to do here, because the README.md in instructions is almost literally exactly what is asked for in this section

main()
* Parameters: sys.argv
* if the length of sys.argv is less than 2, quit with an error message informing the user no url was supplied
* otherwise, check the url supplied and ensure it is an absolute url. if not, quit with an error message informing the user the url was not an absolute url
* if a max depth was supplied, save it, otherwise continue as normal (the crawl() function will have a default value)
* save the start time
* call the crawl() function, catching a KeyboardInterrupt exception
* after the crawl() function returns, save the end time, and report it to the user
* report the total number of urls visited

crawl()
* Parameters: url(string), depth(int), maxdepth(int, constant), visited(set of strings)
* if depth > maxdepth, return immediately
* print the url parameter with indentation (4 spaces for each depth level)
* fetch the url via the requests library and save as response
* check the response, and if not ok, print the status code and reason, and return immediately
* save the response text and find all anchor tags
* for each anchor tag, check if the tag also has the href attribute
  * if it doesnt start with http, throw it out
  * split the url on the '#' character, and only preserve the [0] index (this discards the fragment portion)
  * join this url with the current url (the parameter of this call) to get the absolute url
  * check if the url is present in the visited set, if not:
    * add this url to the visited set
    * call the crawl() function with parameters(this url, depth plus 1, maxdepth, visited)
* at the end of the for loop of all html tags, return from this call of crawl()

again, I tried writing this in my own words, but if it sounds eerily like the instructions/README.md, it's because it is.

## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working Python code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan

The KeyboardInterrupt exception was actually significantly easier to handle than I expected. There also weren't any urls that I found that specifically caused problems,
however returning the count of visited urls proved a bit more of a challenge, and I ended up just creating the visited set outside the crawl() function.

## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.

NOTE: I couldn't find anywhere that mentioned writing unit tests for this program, so I did not do that, but here are some CLI tests I ran and their expected outcome

run `python src/crawler.py` without any arguments. The expected outcome will be the program quitting with an error message informing the user an absolute URL needs to be supplied
run `python src/crawler.py google.com` The expected outcom will be the program quitting with an error message informing the user the url supplied is invalid, and to provide an absolute URL
run `python src/crawler.py https://google.com` The expected output should be a list of successive URLs visited by the program, with increasing indentation (up to four levels (including the initial google.com)). There should be roughly 300 links visited, in approximately 200 seconds. (runtime may differ if your computer is faster than mine) (the links may also differ depending on when the call is run)
run the above command, but sometime while the program is running, press `Ctrl-C` on the keyboard. The expected output is the program stopping, informing the user of the number of links visited and the time taken to visit them, along with a final 'goodbye'
run `python src/crawler.py https://google.com 1` The expected output should be a list of successive URLs visited by the program, with increasing indentation (up to two levels (including the initial google.com)). There should be roughly 11 links visited, in approximately 7 seconds. (again, runtime and exact number of links visited may differ)
run `python src/crawler.py https://google.com 0` The expected output should be the initial URL supplied by the user output to the console. There should be exactly 1 link visited, in approximately 0.75 seconds. (again, runtime and exact number of links visited may differ) (with runtime, I got anywhere from 0.65 to 0.98 seconds)
run `python src/crawler.py https://google.com -2` The expected output will be the program quitting with an error message informing the user a positive, integer value must be supplied for a depth level.
run `python src/crawler.py https://google.com 1.7` The expected output will be the program quitting with an error message informing the user a positive, integer value must be supplied for a depth level.


NOTE: If you really want you can run the above commands with a depth of more than three, but it gets BIG FAST, so I would not advise that, unless you want to wait a long time.

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
    *   What parts of your program are sloppily written and hard to understand? - I do not think so
        *   Are there parts of your program which you aren't quite sure how/why they work? - Not really
        *   If a bug is reported in a few months, how long would it take you to find the cause? - Not long at all. the program is short, so maximum of 30 minutes (unless it has something to do with deep diving, then however long it takes the program to run will be added)
    *   Will your documentation make sense to
        *   anybody besides yourself? - I think so
        *   yourself in six month's time? - definitely
    *   How easy will it be to add a new feature to this program in a year? - not hard at all
    *   Will your program continue to work after upgrading
        *   your computer's hardware? - I think so
        *   the operating system? - I can't imagine why not
        *   to the next version of Python? - Yes
