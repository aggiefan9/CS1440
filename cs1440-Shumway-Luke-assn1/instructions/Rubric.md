# CS 1440 Assignment 1 Rubric

| Points | Criteria
|:------:|--------------------------------------------------------------------------------
| 10     | Software Development Plan is comprehensive and well-written<br/>Follows DuckieCorp project conventions. Other required documentation is filled out as well.
| 15     | User interface/CLI meets client's requirements.
| 10     | Error reporting meets client's requirements<br/>Errors that can reasonably be detected by your code are reported with `usage()`<br/> others are left as Python exceptions.
| 50     | Tools are implemented according to the specification<br/>Program produces output which matches the examples.

**Total points: 85**


## Penalties

Refer to the 'How to Submit Assignments" page in the DuckieCorp Employee Handbook to ensure your project is submitted properly.

*   If your program unexpectedly crashes due to a serious flaw on your part, the highest score you can possibly receive is 50% of the total points.
*   Other crashes may receive a lesser penalty, if your program otherwise runs correctly.

0.  **10 point penalty** submitted project is not a clone of the starter code repository.
1.  **10 point penalty** a module fails to import due to misspelling or incorrect capitalization.
2.  **10 point penalty** program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration.
3.  **10 point penalty** program contains hard-coded paths or otherwise does not function when run from *any* CWD.  (Note: names of modules in `import` statements do not count as "hard-coded").
4.  **10 point penalty** data files are not closed after being processed in *ordinary* situations.  In the event of an error your program will display an error message and immediately exit; in such cases you do not need to take special measures to close files because they will automatically be closed as your program exits.
5.  **10 point penalty** if `eval()` is present in your program.  Remember, kids, [`eval()` is evil](https://thepythonguru.com/python-builtin-functions/eval/#evil-eval).
6.  **10 point penalty** functionality occurs outside of the appropriate module.  (i.e. text tool functions are defined in `tt.py` instead of their own module).
7.  **10 point penalty** program interactively prompts user for input.  All input to this program comes from command-line arguments or from files.
8.  **85 point penalty** external programs are called upon to do the work.  Our customer has hired you to create a pure-Python solution, not a shell script that relies on external programs.
9.  **85 point penalty** if your program imports any modules **except**:
    *   `sys`
    *   Modules provided in the starter code
    *   Modules that you wrote yourself
    *   I want you to have the experience of solving these puzzles for yourself and not to leverage code written by others, no matter how "real-world" it would be to do so.
