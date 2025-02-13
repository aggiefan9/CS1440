# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

*   A detailed written description of the problem this program aims to solve.
*   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.

This program needs to search through an immense amount of data finding lines that contain certain and specific criteria (fips codes in this case)
and compile the statistics of the other fields present on the lines meeting the criteria, put them into a report, and print that report to std.output

A good solution, will quickly (as possible) parse through a data file given, find the lines needed, create the report, and print it out without errors.
* Things already known:
  * Opening a file (crashing if not able)
  * Searching for a key value within a string
    * Have an idea for only searching the beginning of a string instead of throughout the whole string
  * Keeping a running total of certain statistics/numbers
  * Adding the contents of a file in a list
    * will be applied using a set/dictionary for optimization
* Forseen Challenges
  * correctly assigning and updating each variable in the report (rn its just a little confusing)
  * not using readline (for parsing through the file)



## Phase 1: System Analysis *(10%)*

**Deliver:**

*   List all of the data that is used by the program, making note of where it comes from.
*   Explain what form the output will take.
*   Describe what algorithms and formulae will be used (but don't write them yet).

Data Used
* Name of a directory containing the 2020.annual.singlefile.csv and area_titles.csv files (from the command line)
* The aforementioned files (paths will be hardcoded into the program)
  * within 2020.annual.singlefile.csv we will need the following fields
    * Field 0 - area_fips
    * Field 1 - own_code
    * Field 2 - industry_code
    * Field 8 - annual_avg_estabs
    * Field 9 - annual_avg_emplvl
    * Field 10 - total_annual_wages
  * Within the area_titles.csv file we will slurp the contents into a dictionary containing the following fields
    * Key - Fips code
    * Value - English-friendly name of area

Output
* The output will take the form of a report printed to std.output (or redirected to a file IF specified by the user) that follows the form in Report.py

Formulae/Algorithms
* Function to determine if a Directory Path is given, and if not, print a usage message and exit
* Function to open the DIRECTORY/area_titles.csv file (where DIRECTORY is the path provided by the user from the command line) and slurp fields (after calling the .split() method) into a dictionary, then close the file
  * Within the function, use an algorithm for each line checking to see if the first field meets certain criteria (Doesn't begin with a letter or the numbers 57, the last three digits are not 000)
* Function to open the DIRECTORY/2020.annual.singlefile.csv file (where DIRECTORY is the path provided by the user from the command line)
  * Within the function, use an algorithm for each line checking to see if the first field meets certain criteria (found within the dictionary)
    * For each line that meets the criteria, take the abovementioned fields, 1 and 2, and check to see if it belongs within the desired industries (ie. field 1 is either 0, or 5, and field 2 is 10, and 5112 respectively)
      * for each line that meets the criteria, take the remaining fields; 8, 9, and 10; and aggregate them to the appropriate running totals, as well as checking to see if they are the maximum recorded value (if yes, save both the value and the fips code)
        * fill out report with the running totals, the max for each category, as well as the corresponding area


## Phase 2: Design *(30%)*

**Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.


Directory Checking Function
    parameters(None)
    output(usage message, or None) - str or None
    If the length of sys.argv is less than 2, print the following message and exit
        """
        2020 Report Usage
        =================
        main.py FILENAME
        """

Area titles to dictionary function
    parameters(directoryPath) - str
    output(dictionary) - dict
    open a file object with the name directoryPath/area_titles.csv
    create a dictionary, dict
    for each line in the file
        if int(line.split(",")[0][0]) is a digit and line.split(",")[0] is not "57000" and int(line.split(",")[0][2:]) is > 0
            dict[int(line.split(",")[0])] = line.split(",")[1]

Processing 2020 annual single file function
    parameters(directoryPath, dictionary, report) - str, dict, rpt class object
    output(report) - rpt class object
    open a file object with the name directoryPath/area_titles.csv
    dict = dictionary
    rpt = rpt
    for each line in the file
        if int(line.split(",")[0]) is in dict
            if int(line.split(",")[1]) is 0 and int(line.split(",")[2]) is 10
                rpt.all.num_areas += 1
                rpt.all.total_annual_wages += int(line.split(",")[10])
                rpt.all.total_estab += int(line.split(",")[8])
                rpt.all.total_empl += int(line.split(",")[9])
                if int(line.split(",")[10]) > rpt.all.max_annual_wage[1]
                    set rpt.all.max_annual_wage = [dict[int(line.split(",")[0])], int(line.split(",")[10])]
                if int(line.split(",")[8]) > rpt.all.max_estab[1]
                    set rpt.all.max_estab = [dict[int(line.split(",")[0])], int(line.split(",")[8])]
                if int(line.split(",")[9]) > rpt.all.max_empl[1]
                    set rpt.all.max_empl = [dict[int(line.split(",")[0])], int(line.split(",")[9])]
            else-if int(line.split(",")[1]) is 5 and int(line.split(",")[2]) is 5112
                rpt.soft.num_areas += 1
                rpt.soft.total_annual_wages += int(line.split(",")[10])
                rpt.soft.total_estab += int(line.split(",")[8])
                rpt.soft.total_empl += int(line.split(",")[9])
                if int(line.split(",")[10]) > rpt.soft.max_annual_wage[1]
                    set rpt.soft.max_annual_wage = [dict[int(line.split(",")[0])], int(line.split(",")[10])]
                if int(line.split(",")[8]) > rpt.soft.max_estab[1]
                    set rpt.soft.max_estab = [dict[int(line.split(",")[0])], int(line.split(",")[8])]
                if int(line.split(",")[9]) > rpt.soft.max_empl[1]
                    set rpt.soft.max_empl = [dict[int(line.split(",")[0])], int(line.split(",")[9])]



## Phase 3: Implementation *(15%)*

**Deliver:**

* (More or less) working Python code.
* Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan

* I decided to not do functions, and instead wrote the code in the main body.
* I realized in both of the files, the fips codes are strings, so I didn't int() them to avoid more work
* I had to strip off the "" and the \n characters for the area titles dictionary
* (This one wasn't really a hindrance, I just wasted like 20 minutes because in my check whether the line should go into rpt.all or rpt.soft I was checking the own code twice instead of the industry code)


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


I am going to use test cases that utilize the data sets provided to us (**_all_industries, **_combined, **_reversed, **_software_industry, for CT, DC, ND, RI, UT, and WY states)
it is therefore assumed you have access to the directories of the corresponding names with the appropriate data sets as well as the output files

The following tests are run from the console with the cwd as the root directory for this project:
1) run python src/main.py DOESNTEXIST (provided the aforementioned directory does not actually exist)
   1) expected outcome: the program exits via python's open() error message
2) run python src/main.py
   1) expected outcome: the program displays a usage message, informing the user a second directory path needs to be provided, and exits
3) run python src/main.py data/CT_all_industries
   1) expected outcome: the program informs the user it is reading the databases, and a report is generated. Only the first section of the report has nonzero results, and when compared to the appropriate output.txt file the values will be identical
4) run python src/main.py data/CT_software_industry
   1) expected outcome: The opposite of the _all_industries command, the first section is blank, and the second section of the report should be filled out with values identical to the corresponding output.txt file
5) run python src/main.py data/CT_combined
   1) expected outcome: very similar results to above, with the first section of the report being identical to the above test, however the second section is now filled out and also identical to the appropriate output.txt file
   2) NOTE: the first section should be identical to the _all_industries data and the second section should be identical to the _software_industry data
6) run two commands: "python src/main.py data/CT_combined" and "python src/main.py data/CT_reversed"
   1) expected outcome: the two commands should produce identical results, and both are identical to the corresponding output.txt files

NOTE: The above test cases can be repeated with all the state data sets, as well as the USA_full data set

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
    *   What parts of your program are sloppily written and hard to understand? - Maybe the iteration through 2020.annual.singlefile.csv
        *   Are there parts of your program which you aren't quite sure how/why they work? - not really. I mean I still don't understand the magic behind dictionaries and how they find things so quickly, but other than that no.
        *   If a bug is reported in a few months, how long would it take you to find the cause? - given that I don't have a great memory, maybe like 15 minutes (the program itself is fairly straightforward, so there aren't a lot of places it can break).
    *   Will your documentation make sense to
        *   anybody besides yourself? - probably. (if they know what the format of the two files(area_titles and 2020.annual.singlefile) is, then yes)
        *   yourself in six month's time? - definitely.
    *   How easy will it be to add a new feature to this program in a year? - depends on the feature, but it should be pretty easy.
    *   Will your program continue to work after upgrading
        *   your computer's hardware? - yes? I don't know what that would change, but it should work.
        *   the operating system? - yes
        *   to the next version of Python? - yes? again, I don't know what changes, but I didn't use any python hacks (that I know of) that could possibly get removed/changed, so it should definitely work.
