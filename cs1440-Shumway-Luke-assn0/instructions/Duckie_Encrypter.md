# Duckie Encrypter

In the `demo` directory you will find `duckieEncrypter.py`. This file was
provided to assist you in understanding the conversion of plain text to
DuckieCrypt. It is a tool to create DuckieCrypt. When no arguments, are given,
the program will ask the user for text to crypt. When an argument is given, the
DuckieEncrypter will *encrypt* the text file, and output DuckieCrypt to the
screen.

This file is *not* part of the assignment, you do *not* need to change it, and
it will *not* be looked at during code review. Looking over the contents of the
file may assist you in creating the DuckieDecrypter.


## Usage

```
USAGE: $ python demo/duckieEncrypter.py [[FILE]]

[FILE] is an optional argument that is the path to a text file to encrypt.

If [FILE] is not given, the user is prompted to enter a single line of text
input to encrypt.  
```

From the root of the project run `$ python demo/duckieEncrypter.py` to encrypt a
single line of text.

From the root of the project run `$ python demo/duckieEncrypter.py
data/cryptMe1.txt` to encrypt the file `data/cryptMe1.txt`.
