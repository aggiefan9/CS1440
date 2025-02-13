# CS 1440 Assignment 3 Rubric

| Points | Criteria
|:------:|--------------------------------------------------------------------------------
| 10     | 1st draft UML class diagram describes supplied classes' relationships, data members and methods accurately
| 10     | 1st draft UML class diagram describes new classes' relationships, data members and methods
| 5      | 1st draft UML class diagram adheres to UML standards as far as these were explained in class
| 10     | 1st draft Users' Manual describes the program's User Interface<br/>Instructions are appropriate for the intended audience
| 10     | At least two peer reviews (at least 250 words each) are present<br/>Peer reviews written by your study buddies are also included
| 20     | Final code implements all features required by the Program Requirements Specification
| 10     | Final code matches the final draft UML class diagram and Software Development Plan
| 5      | Final draft User's Manual accurately describes user interface of the final product
| 20     | All supplied Unit Tests pass<br/>Unit Tests are meaningful; no trivial unit tests are present; suitable replacements are provided if your design invalidates any supplied tests

**Total points: 100**


## Penalties

Refer to the 'How to Submit Assignments" page in the DuckieCorp Employee Handbook to ensure your project is submitted properly.

*   If your program unexpectedly crashes due to a serious flaw on your part, the highest score you can possibly receive is 50% of the total points.
*   Other crashes may receive a lesser penalty, if your program otherwise runs correctly.

Additionally, this assignment is subject to the following penalties:

0.  **10 point penalty** submitted project is not a clone of the starter code repository.
1.  **10 point penalty** a module fails to import due to misspelling or incorrect capitalization.
2.  **10 point penalty** program attempts to import a module from the `src.` package; this is the result of a PyCharm misconfiguration.
3.  **10 point penalty** program contains hard-coded paths or otherwise does not function when run from *any* CWD.  (Note: names of modules in `import` statements do not count as "hard-coded").
4.  **10 point penalty** if `eval()` or a similar function is used by your program.  You should use `int()` instead.
5.  **10 point penalty** if any files are not closed after being processed in _ordinary_ situations.  In the event of an error your program will display an error message and immediately exit; in such cases you do not need to take special measures to close files because they are automatically closed as your program exits.
6.  **95 point penalty** if your program imports any modules **except**:
    *   `sys`
    *   `unittest`
    *   `random`
    *   `math`
    *   modules that are provided by the starter code
    *   or modules you wrote yourself
    *   This assignment is about the experience of solving this puzzle for yourself without leaning on code written by others, no matter how "real-world" it would be to do so.
7.  **15 point penalty**  if your UML diagram is unreadable.  Watch out for a transparent background (on Diagrams.net, click File -> Export as -> PNG..., then make sure that the option "Transparent background" is left unchecked).  Make sure that the background isn't black, as this obscures the lines connecting classes to each other.  Make sure that the file size is large enough to make the text legible, and that the colors of the diagram stand out in sharp contrast to the background.
8.  **10 point penalty** for each  _trivial_ unit test (i.e. a unit test which unconditionally passes without meaningfully testing some functionality)
