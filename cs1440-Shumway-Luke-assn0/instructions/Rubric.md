# CS 1440 Assignment 0 Rubric

| Points | Criteria
|:------:|--------------------------------------------------------------------------------
| 10     | Software Development Plan is comprehensive and well-written. Follows DuckieCorp project conventions. Other required documentation is filled out as well. Git repository is a clone of the starter code, and contains 5 *new* commits by the student
| 25     | Three lessons completed and associated tests pass
| 35     | DuckieCrypt Decrypter requirements are met

**Total points: 70**

## Penalties

Refer to the 'How to Submit Assignments" page in the DuckieCorp Employee Handbook to ensure your project is submitted properly.  

*   If your program unexpectedly crashes due to a serious flaw on your part, the highest score you can possibly receive is 50% of the total points.
*   Other crashes may receive a lesser penalty, if your program otherwise runs correctly.

In addition, this assignment is subject to the following penalties:

0.  **10 point penalty** submitted project is not a clone of the starter code repository.
1.  **10 point penalty** a module fails to import due to misspelling or incorrect capitalization.
2.  **10 point penalty** program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration.
3.  **10 point penalty** program contains hard-coded paths or otherwise does not function when run from *any* CWD.  (Note: names of modules in `import` statements do not count as "hard-coded").
4.  **10 point penalty** data files are not closed after being processed in *ordinary* situations.  In the event of an error your program will display an error message and immediately exit; in such cases you do not need to take special measures to close files because they will automatically be closed as your program exits.
5.  **70 point penalty** external programs are called upon to do the work.  Our customer has hired you to create a pure-Python solution, not a shell script that relies on external programs.
6.  **70 point penalty** if your program imports any modules **except**:
    *   `sys`
    *   `os`
    *   Modules provided in the starter code
    *   Modules that you wrote yourself
    *   I want you to have the experience of solving these puzzles for yourself and not to leverage code written by others, no matter how "real-world" it would be to do so.
