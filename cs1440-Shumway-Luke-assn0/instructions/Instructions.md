# CS 1440 Assignment 0 Instructions

## Description

Your ultimate goal is to complete `src/duckieDecrypter.py`. This program decrypts data encoded in DuckieCrypt from a user-specified text file.  One of our previous interns started this project but abandoned it just before reaching the "Implementation" phase.  To help you have more success we have created lessons to assist you in learning the Python skills necessary to complete this project.

0.  Begin by reading the core README's of this repository.
1.  Then read `doc/Plan.md`.  This is your Software Development Plan, and will
    serve as your guide to completing your task.  You will update this file as
    you work on the project.
3.  After studying the Plan, work through the lessons in the `lsn` directory in
    order.  Each lesson equips you with a new Python tool to enable you to
    complete the DuckieDecrypter.
4.  Finish reading the rest of this document and craft the DuckieDecrypter.



## Previous Semester Assignment Statistics

Statistic                        | Value
--------------------------------:|:---------------
Average Hours Spent              | 9.76
Average Score % (Grade)          | 86.76% (B)
% students thought this was Easy | 33.33%
... Medium                       | 54.61%
... Hard                         | 7.80%
... Too Hard/Did not complete    | 4.26%



## Running the DuckieDecrypter program

When a user runs `duckieDecrypter.py` they are prompted for a **relative path** to a file to decrypt.  This path is relative to where the program was ran.

**Relative paths** are discussed in `lsn/2-FileOperations`.

```
$ python src/duckieDecrypter.py
Please select a text file to decrypt:
>>> data/msg1.txt
Welcome to DuckieCorp! We sure are glad to have you working with us. In your
tenure here, we hope you will learn many new techniques to enhance your computer
science and problem solving skills. We're excited to get started!
- DuckieCorp Management
```

Please note that `$` denotes a command in the shell, and `>>>` denotes input in Python.


## Understanding DuckieCrypt

DuckieCrypt is based on ASCII values, which are discussed in depth in the lesson
`lsn/0-ASCIIChars`.

*   A DuckieCrypt character is comprised of two parts: the `[flag]` and the `[character_code]`.
*   There is no space between the `[flag]` and the `[character_code]`.
*   Examples of valid DuckieCrypt characters are `_0`, `^9`, `_19`, `+A4`, and `+C2`.
    - DC character `_0` has a `[flag]` of `_` and a `[character_code]` of `0`.
    - DC character `^9` has a `[flag]` of `^` and a `[character_code]` of `9`.
    - DC character `_19` has a `[flag]` of `_` and a `[character_code]` of `19`.
    - DC character `+A4` has a `[flag]` of `+` and a `[character_code]` of `A4`.
    - DC character `+C2` has a `[flag]` of `+` and a `[character_code]` of `C2`.
*   A DuckieCrypt message is a space-separated sequence of DuckieCrypt characters

"Hello World!" in DuckieCrypt looks like this:

```
^7 _4 _11 _11 _14 +A0 ^22 _14 _17 _11 _3 +A1
```


### DuckieCrypt Flags

DuckieCrypt flags are *always* one character.  The three valid flags are `^`, `_`, and `+`.

*   `^` denotes that the translated character is **uppercase**.
*   `_` denotes that the translated character is **lowercase**.
*   `+` denotes that the translation will result in a special character: one
    that is printable but is not alphabetic.
*   Any other character used as a flag is an invalid DuckieCrypt character.
    If your program encounters an invalid DuckieCrypt character, skip over it
    without printing anything.


### DuckieCrypt Character Codes

A `[character_code]` follows a flag and determines which *ASCII* character to
translate the DuckieCrypt character to.

*   For the lowercase and uppercase characters, the `[character_code]` is an
    integer.
*   For special characters a `[character_code]` is composed of two parts:
    *   an alphabetic character
    *   an integer
*   The alphabetic character determines which of the 3 special character groups
    the DuckieCrypt character translates to, while the integer that follows
    denotes which ASCII character it is.
*   If your program encounters an invalid DuckieCrypt character code, skip over
    it without printing anything.


## Character Tables

The following tables are provided to assist you in translating DuckieCrypt back
into plain-text.  


### Uppercase Characters

| Character      | DuckieCrypt Translation
| :------------- | :---------------------
| `A`            | `^0`
| `B`            | `^1`
| `C`            | `^2`
| `D`            | `^3`
| `E`            | `^4`
| `F`            | `^5`
| `G`            | `^6`
| `H`            | `^7`
| `I`            | `^8`
| `J`            | `^9`
| `K`            | `^10`
| `L`            | `^11`
| `M`            | `^12`
| `N`            | `^13`
| `O`            | `^14`
| `P`            | `^15`
| `Q`            | `^16`
| `R`            | `^17`
| `S`            | `^18`
| `T`            | `^19`
| `U`            | `^20`
| `V`            | `^21`
| `W`            | `^22`
| `X`            | `^23`
| `Y`            | `^24`
| `Z`            | `^25`


### Lowercase Characters

| Character      | DuckieCrypt Translation
| :------------- | :---------------------
| `a`            | `_0`
| `b`            | `_1`
| `c`            | `_2`
| `d`            | `_3`
| `e`            | `_4`
| `f`            | `_5`
| `g`            | `_6`
| `h`            | `_7`
| `i`            | `_8`
| `j`            | `_9`
| `k`            | `_10`
| `l`            | `_11`
| `m`            | `_12`
| `n`            | `_13`
| `o`            | `_14`
| `p`            | `_15`
| `q`            | `_16`
| `r`            | `_17`
| `s`            | `_18`
| `t`            | `_19`
| `u`            | `_20`
| `v`            | `_21`
| `w`            | `_22`
| `x`            | `_23`
| `y`            | `_24`
| `z`            | `_25`


### Special Characters

#### Group A
| Character      | DuckieCrypt Translation
| :------------- | :---------------------
| ` `            | `+A0`
| `!`            | `+A1`
| `"`            | `+A2`
| `#`            | `+A3`
| `$`            | `+A4`
| `%`            | `+A5`
| `&`            | `+A6`
| `'`            | `+A7`
| `(`            | `+A8`
| `)`            | `+A9`
| `*`            | `+A10`
| `+`            | `+A11`
| `,`            | `+A12`
| `-`            | `+A13`
| `.`            | `+A14`
| `/`            | `+A15`
| `0`            | `+A16`
| `1`            | `+A17`
| `2`            | `+A18`
| `3`            | `+A19`
| `4`            | `+A20`
| `5`            | `+A21`
| `6`            | `+A22`
| `7`            | `+A23`
| `8`            | `+A24`
| `9`            | `+A25`
| `:`            | `+A26`
| `;`            | `+A27`
| `<`            | `+A28`
| `=`            | `+A29`
| `>`            | `+A30`
| `?`            | `+A31`
| `@`            | `+A32`

#### Group B

| Character      | DuckieCrypt Translation
| :------------- | :---------------------
| `[`            | `+B0`
| `\`            | `+B1`
| `]`            | `+B2`
| `^`            | `+B3`
| `_`            | `+B4`
| `` ` ``        | `+B5`

#### Group C

| Character      | DuckieCrypt Translation
| :------------- | :---------------------
| `{`            | `+C0`
| `\|`           | `+C1`
| `}`            | `+C2`
| `~`            | `+C3`
