# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

* A detailed written description of the problem this program aims to solve.
* Describe what a *good* solution looks like.
    * List what you already know how to do.
    * Point out any challenges that you can foresee.
    
This program needs to create a user interface that takes input from the user and uses said input to create a deck of bingo cards with the desired specifics
* (the ui will create a menu and fill it with menuoption objects, which will then create a deck object and fill it with card variables, which are filled with numbers from a numberset object)
* A good solution will be a very user-friendly interface which prompts the user seamlessly to specify a set of parameters to create a deck with a specific number of cards, each with a specific size, and each with numbers between a specific range

## Phase 1: System Analysis *(10%)*

**Deliver:**

*   List all of the data that is used by the program, making note of where it comes from.
*   Explain what form the output will take.
*   Describe what algorithms and formulae will be used (but don't write them yet).

Data used:
* card size - input from user
* max number - input from user
* number of cards - input from user
* menu option selections - input from user
* deck object - created by program
* card objects - created by program
* file name - input from user

Output:
* Menu(with options) - string printed to stdout
* Deck - collection of card objects
* Card - string printed to stdout
* Saved deck - string printed to the file provided by the user

function to create a menu and fill it with options
function to display the menu and get input from the user
function to create a deck of bingo cards
function to create a bingo card
function to get a number set, randomize it, and fill out a bingo card
function to print a bingo card
function to print the entire bingo deck

## Phase 2: Design *(30%)*

**Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.


function to create a deck of bingo cards
    if the user selects option "C" (on line 19 of UserInterfacy.py), call the __createDeck() method
    prompt the user for the following using the __getIntegerInput() method:
        the number of cards (int between 2 and 8192),
        the size of the bingo cards (int between 3 and 16),
        the max number shown on the card (int between roughly twice the size^2 and 4 times the size^2)
    using these inputs, create a Deck object instance and pass those inputs as the parameters
        using the parameters from the function caller,
        create a numberset object instance passing the max number shown on card as the parameter
        for i in range(number of cards):
            create a card with i, the card size, and numberset object instance as parameters
    call the __deckMenu() method to display the deck menu options
function to create a bingo card
    obtain actual parameters from function caller
    set self.__idnum (i from above) equal to the idnum parameter
    set self.__size equal to the size parameter
    create another variable, self.__squares, which is a list consisting of self.__size sublists
    randomize the number set
    for i in range (size)
        for j in range (size)
            if size % 2 == 1 and size // 2 == i and i == j:
                append the string "FREE" to self.__numbers[i]
            else:
                append numberset(the object).getNext() to self.__numbers[i]
function to get a number set, randomize it, and fill out a bingo card
    obtain actual parameters from function caller
    create a blank list, self.__numbers
    for i in range(1, size + 1)
        append i to self.__numbers
    to randomize, call random.shuffle(self.__numbers)
    to getNext, call self.__numbers.pop()
function to print a bingo card
    prompt the index of the card who will be printed
    call the print() method of the deck object with the index as a parameter
    in the print method, the print() method of the card will be called ## this line is already written
    Print the card with the following format:
    +------+------+------+
    |   1  |   2  |   3  |
    +------+------+------+
    |   4  | FREE |   5  |
    +------+------+------+
    |   6  |   7  |   8  |
    +------+------+------+
    the numbers will be replaced with the getSquare method
        for i in range(size)
            print("+", end="")
            print("------+" * size)
            for k in range(size)
                print("|", end="")
                print(format(self.getSquare(i, j), "^6"), end="")
        print("+", end="")
        print("------+" * size)

## Phase 3: Implementation *(15%)*

**Deliver:**

* (More or less) working Python code.
* Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan

I handled the NumberSet differently than I think the unit tests do, so I had to fix that
  * (I have each card possess its own unique numberset instead of the same numberset to avoid running out of numbers using the getNext method)
  * I don't know if we're supposed to use the .pop() method on the numbersets, but that's the way I avoided assigning duplicate numbers on the same card
    * (can't asign a number that isn't there (; )

## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


Since there are already some lovely tests, to assess the general functionality of the program, run "python src/runTests.py" from the console to ensure all tests pass
The unit tests contained within the runTests.py (and also found in the Testing directory) test the following functionality
* testCard.py tests the creation and handling of a single bingo card. It tests specifically for the following:
  * The Id number of each card is as expected
  * The Size is handled correctly (produces a square card with N rows and columns)
  * The number assignment is correct (each number on a card only shows up once (note that not ecery number shows up on each card))
  * The number storage is handled correctly (each square is stored at the proper address (row and column))
  * The Free space is handled correctly (on cards with an odd size (ie. 5 x 5) the middle square (in the case of a 5 x 5 card, the square in the 3rd row and 3rd column) is "FREE" instead of a number)
    * For cards with an even size (ie. 4 x 4) there is no free space ):
* testDeck.py tests the creation and handling of a deck of bingo cards. It tests specifically for the following:
  * The deck contains the correct number of cards
  * The cards can be accessed by their ID number from within the deck
* testNumberSet.py tests the creation and handling of a NumberSet (not seen from the outside, but used to determine which numbers are shown on each bingo card). It tests specifically for the following:
  * The size of the number set is as expected (ie. a NumberSet supposedly containing numbers 1 through 18 actually contains numbers 1 through 18)
  * The indexing is graceful (ie, if you try to get the 19th number of the abovementioned set (only 1 - 18) None is returned instead of crashing)
  * The getNext method is handled gracefully (which results in the lack of duplicate numbers on a bingo card)
    * when used repeatedly, will eventually return all the numbers in the numberSet, after which None is returned (ie. you can call this as many times as you want and will never get an error)
* testMenu.py tests the User Interface (in a way). It tests specifically for the following:
  * The addition of a menu option (if it didn't previously exist, create it. if it did, do nothing)
  * The accessing of menu options from the menu (they can be printed and followed (with the proper command of course))
  * The Header works as expeted
  * The number of options is handled correctly (a menu claiming to have 5 options actually has 5 options)


For all the input specific errors (entering a string when a number is expected, entering an invalid number, entering a bad file path, etc) that might be encountered, please refer to the User Manual (Manual.md in the doc directory)


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
    *   What parts of your program are sloppily written and hard to understand? - maybe the Card.py document (mostly the printing, because that's a lil' challenging)
        *   Are there parts of your program which you aren't quite sure how/why they work? - Not really. maybe the UserInterface/Menu/MenuOption classes (I get how the work, I just don't know why they're all necessary)
        *   If a bug is reported in a few months, how long would it take you to find the cause? - pretty quickly. there isn't a lot of overlap between the different functionalities, so I'd just look at the part of the program where the error was reported
    *   Will your documentation make sense to
        *   anybody besides yourself? - hopefully. I don't think it's too bad
        *   yourself in six month's time? - definitely
    *   How easy will it be to add a new feature to this program in a year? - Depending on the feature. but it should be pretty easy
    *   Will your program continue to work after upgrading
        *   your computer's hardware? - Yes
        *   the operating system? - Yes
        *   to the next version of Python? - Yes (unless for some reason the way printing works (with * x printing the same thing multiple times) changes)
