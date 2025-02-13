# Code Smells Report

## Instructions

Edit this file and include it in your submission.

For each instance of a code smell you find in the starter code report:

*	Where you found it (filename + line number)
*	Copy the offensive code
*	Explain why the smell is a problem
*	Describe how you fixed it

### These are some of the code smells you may find in the starter code:

0.  "Magic" numbers
    *   Numeric literals that appear in critical places but without any apparent meaning
    *   "When I see the number `214` here, does it have the same meaning as the `214` over there?"
1.  Global variables
    *   A global is being used to avoid passing a parameter into a function
    *   A global is being used to return an extra value from a function
2.  Poorly-named variables
    *   Variables with one-letter long names are okay to use in special contexts; otherwise, they should be avoided
        *   For example, a counter called `i` or `j` used in a `for` loop that is but a few lines long
        *   Variables from well-known math formulae should match the textbook (i.e. `a`, `b` and `c` are familiar in a quadratic or Pythagorean formula)
    *   Variables with really, really long names can make code *less* easy to read
    *   If a programmer is not careful, variables can accidentally override or "shadow" other identifiers in a program
        *   Builtin Python functions such as `input`, `len`, `list`, `max`,
            `min` and `sum` are especially susceptible to this
    *   Variable names should strike a good balance between brevity and descriptiveness
3.  Comments that share too much information
    *   A function or method is filled with many explanatory comments
    *   This is often done because the variable names and function names are poorly chose
    *   Rather, let the code speak for itself
4.  Comments that lie to you
    *   A comment which may have once been helpful, but no longer accurately describes the code
    *   A comment that is straight-up misleading, perhaps written by a developer without a clue
5.  Parameter list that is too long 
    *   More than three or four parameters for a method
    *   Parameters that are passed in but left unused
6.  Function/Method that is too long 
    *   A method contains too many lines of code
    *   Typically this happens because the method has too many different responsibilities
    *   Generally, any method longer than ten lines should make you ask the question "what if I split this into smaller, more focused pieces?"
7.  Overly complex decision trees
    *   Overly long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Are all of the branches possible to reach?
    *   Have all of the branches been tested?
8.  Spaghetti code
    *   Lots of meandering code without a clear goal
    *   Many functions/objects used in inconsistent ways
    *   All code is contained in one giant function/method with huge `if/else` branches
    *   "It would be easier to rewrite this than to understand it"
9.  Redundant code
    *   When you see a line of code that is repeated, ask whether it makes any difference to be run more than once.
10. Dead code
    *   A variable, parameter, field, method or class is no longer used (usually because it is obsolete)
    *   Big blocks of commented-out code that serve no purpose and clutter up the file

Other code smells may also be identified; list them as well.


## Smells

*TODO: write your report here*

* There is an instance of a comment that lies at `src/main.py`, line 12. ```# quit when too many arguments are given``` The opposite is true, the program quits when not enough arguments are provided. Since it is a comment, I will simply change it to reflect the true nature of the code it describes.
* There is an instance of a comment that lies at `src/main.py`, line 29. ```# Otherwise, quit with an error message to help the user learn how to run it``` This implies the program will quit with an error, but the code this comment describes actually continues on to run normally. Because it is a comment, I will simply change it to reflect the true nature of the code it describes.
* There is an instance of a comment that is confusing at `src/main.py`, line 19. ```# quite when one of the arguments isn't in the command line``` I think it's trying to say the program will quit if the command line argument is not an accepted fractal, but it doesn't make sense. Since it is a comment, I will simply change it to reflect the true nature of the code it describes.
* There is an instance of gross confusing code at `src/main.py`, lines 23-26. It can be replaced with the for loop found earlier in the file at lines 15-16 without changing the functionality of the program. 
```
all_of_the_fractals = JULIAS
all_of_the_fractals.extend(MBROTS)
for i in all_of_the_fractals:
    print(f"\t{i}")
```
can be changed to
```
for i in JULIAS + MBROTS:
    print(f"\t{i}")
```
* There is an instance of a comment that shares too much information at `src/main.py`, line 19. ```# fractal is the 1st argument after the program name``` This is unnecessary, and a comment so I will just delete it.
* There is an instance of unused import statements at `src/mbrot_fractal.py`, lines 7-18. Since they are all commented out, I will just delete them.
```
#from math import sqrt, cos, cosh, sin, sinh, remainder, acos, acosh, asin, asinh

# These are the imports that I usually import
# import turtle
# import os
# import os.path
# import sys
# import time
# import math

# this import caused problems on my Windows computer...
# import numpy
```
* There is an instance of convoluted code at `src/mbrot_fractal.py`, lines 20-23,25-27. Here some colors are defined and later used in the color palette list, but only 7 of the 111 colors are defined. I will instead not define the colors and used the color codes in the list for consistency.
```
GRAPEFRUIT_PINK = '#e8283f'
LEMON = '#fdff00'
LIME_GREEN = '#89ff00'
KUMQUAT = '#fac309'
POMELLO = '#2fff00'
TANGERINE = '#f7b604'
WHITE = '#ffffff'
```
* There is an instance of redundant code at `src/mbrot_fractal.py`, lines 24 & 65. ```MAX_ITERATIONS = -1``` This variable is defined, then later redefined ```MAX_ITERATIONS = len(palette)``` without ever being used (the first definition). It will not change the functionality of the program to delete this first definition, and I will do just that.
* There is an instance of dead code at `src/mbrot_fractal.py`, lines 28-44. It is a variation of the `palette` variable declared immediately afterwards that purportedly is incorrect. There is already a working version of the variable, so this copy can safely be deleted.
```
#palette = [LIME_GREEN, '#a8f71b', '#c0ef34', '#d2ea4c', '#dfe563', '#e2db78',
#        '#e0d28d', '#dfce9f', '#e0ceb1', '#e2d2c1', '#e5d9d0', '#eae1de',
#        '#efebea', '#f7f5f5', WHITE, '#f7f5f5', '#efebea', '#eae0de',
#        '#e5d6d0', '#e2cdc1', '#e0c5b1', '#dfbf9f', '#e0bc8d', '#e2bd78',
#        '#e5c163', '#eac94c', '#efd634', '#f7e81b', LEMON, '#f7e81b',
#        '#efd634', '#eac94c', '#e5c163', '#e2bd78', '#e0bc8d', '#dfbf9f',
#        '#e0c5b1', '#e2cdc1', '#e5d6d0', '#eae0de', '#efebea', '#f7f5f5',
#        WHITE, '#f6f5f5', '#efeaea', '#e9dfdd', '#e4d4d0', '#e1c9c1',
#        '#dfbfb0', '#deb69f', '#deae8c', '#e0a978', '#e2a563', '#e7a54c',
#        '#eca834', '#f3ae1b', TANGERINE, '#f3ae1b', '#eca834', '#e7a54c',
#        '#e2a563', '#e0a978', '#deae8c', '#deb69f', '#dfbfb0', '#e1c9c1',
#        '#e4d4d0', '#e9dfdd', '#efeaea', '#f6f5f5', WHITE, '#f6f6f5',
#        '#efefea', '#e5e9de', '#d5e3d1', '#c3dfca', '#b4ddd1', '#a3d2db',
#        '#91adda', '#857fdb', '#a66bdc', '#dc56df', '#e33f9d', WHITE,
#        '#f6f5f4', '#eeeee8', '#e2e7db', '#cedead', '#beefcc', '#abdbd9',
#        '#99beda', '#858cda', '#9c70dc', '#d159de', '#e341a4',
#        GRAPEFRUIT_PINK, ]
```
* There is an instance of a comment that lies at `src/mbrot_fractal.py`, line 46. ```# This color palette contains 100 color steps.``` The color palette that follows has 111 colors, which no one will take the time to count (unless you're me) but it could lead to some problems. Since it is a comment, I will simply change it to reflect the true nature of the code it describes.
* There is an instance of convoluted code at `src/mbrot_fractal.py`, lines 66-72. first z, it is defined here as 0 then globalized and redefined without using to `global z = complex(0, 0)` There is no reason to have it global, so I will delete that key word, along with the initial definition that is never used. seven and TWO are both only used in one place, so the numbers can be used there (for TWO at least. seven should never be used so it is safe to delete altogether). img, just like z is defined then globalized and redefined later without being used at the bottom of the file to `global img = PhotoImage(width=512, height=512)` It is safe to delete the initial definition because it is never used. mainWindowObject is never used, so it is safe to delete.
```
z = 0
seven = 7.0
TWO = 2

img = None

mainWindowObject = None
```
* There are 4 instances of global variables at `src/mbrot_fractal.py`, lines 76,79-80,85. The variables are `z` `MAX_ITERATIONS` `iter` and `TWO` All of which are only used in this one instance. They do not need to be global variables, so I will change that.
* There are 2 instances of bad variable names at `src/mbrot_fractal.py`, lines 80-82. `iter` and `len` both shadow built-in names, and in the case of `len` it is literally just another reference to MAX_ITERATIONS. `len` can be deleted altogether, and `iter` can be renamed to `i` even because it is just used in the for loop.
* There is an instance of spaghetti code at `src/mbrot_fractal.py`, lines 82-102. The first if statement is the only good one (looking only at the logic, not the variables). The second doesn't do anything except bypass the third, fourth, and fifth ones, all of which have no functionality. This could be rewritten using just the first if statement and the first return statement after the loop. The second one is unreachable because it lies after a return statement and can be deleted.
```
len = MAX_ITERATIONS
    for iter in range(len):
        z = z * z + c  # Get z1, z2, ...
        global TWO
        if abs(z) > TWO:
            z = float(TWO)
            return palette[iter]  # The sequence is unbounded
        elif abs(z) < TWO:
            continue
        elif abs(z) > seven:
            print("You should never see this message in production")
            continue
            break
        elif abs(z) < 0:
            print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}")
            sys.exit(1)
        else:
            pass
    # XXX: one of these return statements made the program crash...
    return palette[MAX_ITERATIONS - 1]   # Indicate a bounded sequence
    return palette[MAX_ITERATIONS]
```
* There is an instance of a bad variable at `src/mbrot_fractal.py`, line 105. ```window = None``` window is defined here as None, but later globalized and redefined without using the first definition on line 240 ```global window = Tk()``` this first definition can safely be deleted as it is never used.
* There are 2 more instances of global variables at `src/mbrot_fractal.py`, lines 111-112. ```palette``` and ```img``` both are previously defined, and neither need to be globalized, so it is safe to remove this globalization.
* There is an instance of a magic number at `src/mbrot_fractal.py`, line 124. `512` is used here as the width and height of a canvas. it is also used on the following lines: 130, 132, 134, 135, 139, 242, and `256` (half of 512) is used on line 126. It appears that this is the size (in pixels) of the canvas, and that appears to be the only use, but because it is used in so many places, it should be put into a variable, which is exactly what I will do.
* There are 2 instances of variables that appear to have no use at `src/mbrot_fractal.py`, lines 132-133. `portion` and `total_pixels` are both set to what appears to be arbitrary numbers, and never used again. So it should be safe to delete without changing the functionality of the program.
* There is an instance of dead code at `src/mbrot_fractal.py`, lines 143-170. The first function (pixelsWrittenSoFar) is never called, and the second is a commented out variation of the function `colorOfThePixel` that purportedly doesn't work. There is already a version of `colorOfThePixel` that does work, so this copy can safely be deleted. and the obsolete function can be deleted as well, because it has no use.
```
def pixelsWrittenSoFar(rows, cols):
    pixels = rows * cols
    print(f"{pixels} pixels have been output so far")
    return pixels


#def colorOfThePixel(c, colors):
#    """Return the color of the current pixel within the Mandelbrot set"""
#    global z
#    global MAX_ITERATIONS
#    global mainWindowObject
#    z0 = complex(0, 0)  # z0
#
#    for iter in range(MAX_ITERATIONS + 1):
#        z0 = z0 * z0 + c
#        # if the absolute value of z is less than TWO
#        # if abs(z) > TWO:
#        if abs(z) > 2.0:
#            if z == float(2.0):
#                return colors[iter-1]
#            elif abs(z) < z:
#                if abs(z) > TWO:
#                    return colors[iter]
#                else:
#                    return colors[iter+0]
#            else:
#                return colors[iter+1]
#    return colors[MAX_ITERATIONS]
```
* There is an instance of duplicate code at `src/mbrot_fractal.py`, lines 210-214. The spiral1 entry is duplicated in the images dictionary. It is an exact copy, so the second entry can safely be deleted.
```
'spiral1': {
'centerX': -0.747,
'centerY': 0.1075,
'axisLen': 0.002,
},
```
* There are 2 more instances of global variables at `src/mbrot_fractal.py`, lines 237 & 240. `img` and `window` are both previously defined, but here they are globalized and redefined without ever using the initial definition. They can both be passed through function calls and do not need to be globalized. It is safe to delete the first definition of each variable and to remove the globalization and instead pass the variables through the functions.
* There is an instance of unused imports at `src/julia_fractal.py`, lines 3-28. Only `sys` and `time` are used, so the rest can safely be deleted.
```
# These are the imports that I usually import
import turtle
import os
import os.path
import sys
import time

# These are imports people on StackOverflow use all the time.
# I've begun importing these just in case I need to borrow some code that I find online
# This way, whatever I paste is guaranteed to work without making more errors!
import functools
import itertools
import builtins
import pathlib
import pickle
import importlib
# these ones make my programs crash on some of my computers
# I'll just comment them out, just in case I need them, so I don't have to look up how to import them on SO
#import numpy
#from torch import Tensor
#import pandas
import unittest
import csv
import argparse
import asyncio
import http, html
```
* There is an instance of both a comment that shares too much and global variables at `src/julia_fractal.py`, lines 42-45. The comment admits guilt for globalizing variables, which is unneeded, and `grad` and `win` are always passed as a parameter through each function, so there is no need to have them globalized. It is safe to remove these lines.
```
# I feel bad about all of the global variables I'm using.
# There must be a better way...
global grad
global win
```
* There is another instance of a comment that lies at `src/julia_fractal.py`, line 47. ```# Here 76 refers to the number of colors in the palette``` The number used in the for loop immediately after is 78 (which I should note is also wrong. the correct number should be 96). Both the comment and the for loop can be changed to include the number 96 instead of 76 or 78. (in addition this appears to be a magic number, and should actually be a variable, which will be done in the refactoring).
* There are 2 instances of unreachable code at `src/julia_fractal.py`, lines 52 & 55. ```z += z + c``` and ```return grad[78]``` both come after return statements and can safely be deleted without changing any functionality.
* There is an instance of both bad function name and dead code at `src/julia_fractal.py`, lines 58-71. The function name is WAY TOO LONG and additionally isn't even used. It can safely be deleted and save everyone some heartache.
```
def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):
    """Make sure that the fractal configuration data repository dictionary
    contains a key by the name of 'name'

    When the key 'name' is present in the fractal configuration data repository
    dictionary, return its value.

    Return False otherwise
    """
    for key in dictionary:
        if key in dictionary:
            if key == name:
                value = dictionary[key]
                return key
```
* There is an instance of convoluted variables at `src/julia_fractal.py`, line 74. Here `tkPhotoImage` is set to None, but is later globalized and redefined without ever using this definition at line 246. This initial definition can safely be deleted.
* There is an instance of a bad function signature at `src/julia_fractal.py`, line 74. ```def makePictureOfFractal(f, i, e, w, g, p, W, s):``` First, all the parameters are only one letter, and there is both a w and a W. second, only `f`, `w`, `p`, `W`, `s` are used. The names could be expanded to better describe what is going on, `f` is the fractal dictionary, `w` is the window (Tk instance), `p` is the PhotoImage instance, `W` is the color code for black, and `s` is the size(512), which will be done in the refactor.
* There is an instance of bad comments at `src/julia_fractal.py`, lines 77-81. The size is actually 512, not 640, and the other two comments are confusing and honestly I don't understand what it's talking about. The first can be changed to reflect the true size, and the second will be deleted straight up.
```
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 640x640 pixels."""

    # Correlate the boundaries of the PhotoImage object to the complex
    # coordinates of the imaginary plane
```
* There is an instance of a comment that shares too much at `src/julia_fractal.py`, lines 89. ```# Squares are basically rectangles except the sides are equal instead of different``` This is unnecessary altogether, and will be deleted in the refactor.
* There is an instance of a bad variable name at `src/julia_fractal.py`, lines 94. ```tk_Interface_PhotoImage_canvas_pixel_object``` this is way too long and can be renamed to `canvas` because that is a better name.
* There is an instance of bad comments at `src/julia_fractal.py`, lines 102-103. I don't really know if the comments apply or are lying, so I will just delete them.
``` 
    # Create the TK PhotoImage object that backs the Canvas Objcet
    # This is what lets us draw individual pixels instead of drawing things like rectangles, squares, and quadrilaterals
```
* There is an instance of redundant code at `src/julia_fractal.py`, lines 104-107, 112-113. All four commands are duplicates, as the exact same command was run up in line 97. It is safe to delete all five of these lines, and it will not change the functionality.
```
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # This seems repetitive
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # But it is how Larry wrote it the tutorial
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Larry's a smart guy.  I'm sure he has his reasons.
...
    # pack the canvas object into its parent widget
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Does this even matter?
```
* There is an instance of both comments that share too much and an unused variable at `src/julia_fractal.py`, lines 109-110. The comment shares too much, and the variable is never used. Both can be deleted without changing the functionality.
```
    # Total number of pixels in the image, AKA the area of the image, in pixels
    area_in_pixels = 640 * 640
```
* There is an instance of a comment sharing too much at `src/julia_fractal.py`, lines 114-115. This comment feels unnecessary, and I will delete it to preserve simplicity.
```
    # At this scale, how much length and height of the
    # imaginary plane does one pixel cover?
```
* There is an instance of a comment sharing WAY TOO MUCH at `src/julia_fractal.py`, lines 124-153. the first comment is a paragraph and feels completely unnecessary, as it just explains the functionality of for loops. Pretty much every comment in this section is unnecessary, as it shares too much. I will delete them (the comments) entirely.
```
    # for r (where r means "row") in the range of the size of the square image,
    # but count backwards (that's what the -1 as the 3rd parameter to the range() function means - it's the "step"
    # You can actually put any number there that you want, because it defaults to "1" you usually don't have to
    # but I have to here because we're actually going BACKWARDS, which took me
    # a long time to figure out, so don't change it, or else the picture won't
    # come out right
    for r in range(s, 0, -1):
        # for c (c == column) in the range of pixels in a square of size s
        for c in range(s):
            # calculate the X value in the complex plane (I guess that's
            # actually the REAL number part, but we call it X because
            # GRAPHICS... whatev)
            x = min[0] + c * size
            y = 0
            # get the color of the pixel at this point in the complex plain
            c2 = getColorFromPalette(complex(x, y))
            # calculate the X value in the complex plane (but I know this is
            # really the IMAGINARY axis that we're talking about here...)
            y = min[1] + r * size
            # TODO: do I really need to call getColorFromPalette() more than once?
            #       It feels like that might be kinda slow...
            #       But, if it aint broken, don't repair it, right?
            # get the color of the pixel at this point in the complex plain
            c2 = getColorFromPalette(complex(x, y))
            # put the color c2 into the 
            p.put(c2, (c, s - r))
            # get the color of the pixel at this point in the complex plain
            c2 = getColorFromPalette(complex(x, y))  # does it matter if 
        w.update()  # display a row of pixels
        fraction_of_pixels_writtenSoFar += 640  # update the number of pixels output so far
```
* There is an instance of duplicate code, and bad variables at `src/julia_fractal.py`, lines 137-151. First `y` is set to zero, then used in `c2`, but `y` is redefined in line 142 and then reused in `c2` again before the first `c2` is used. Then `c2` is redefined AGAIN after the second version is used, and this third definition is never used. The first definition of `y` will be deleted, and `c2` will only be defined once.
```
            y = 0
            # get the color of the pixel at this point in the complex plain
            c2 = getColorFromPalette(complex(x, y))
            # calculate the X value in the complex plane (but I know this is
            # really the IMAGINARY axis that we're talking about here...)
            y = min[1] + r * size
            # TODO: do I really need to call getColorFromPalette() more than once?
            #       It feels like that might be kinda slow...
            #       But, if it aint broken, don't repair it, right?
            # get the color of the pixel at this point in the complex plain
            c2 = getColorFromPalette(complex(x, y))
            # put the color c2 into the 
            p.put(c2, (c, s - r))
            # get the color of the pixel at this point in the complex plain
            c2 = getColorFromPalette(complex(x, y))  # does it matter if 
```
* There is another instance of a comment sharing too much at `src/julia_fractal.py`, lines 156-160. The comment just talks about the problems with adding more colors to the palette, and is unnecessary and will be deleted.
```
# This is the color palette, which defines the palette that images are drawn
# in as well as limiting the number of iterations the escape-time algorithm uses
#
# TODO: It would be nice to add more or different colors to this list, but it's
# just so much work to calculate all of the in-between shades!
```
* There is yet another instance of a comment sharing too much at `src/julia_fractal.py`, lines 181-191. The comment shares about not having enough time and altogether is unnecessary and will be deleted.
```
# This dictionary contains the different views of the Julia set you can make
# with this program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'i'.
#
# TODO: Maybe it would be a good idea to incorporate the complex value `c` into
# this configuration dictionary instead of hardcoding it into this program.
# But I don't have time for this right now, too busy.  I'll just keep doing it
# the way I know how.
```
* There is another instance of comments sharing too much at `src/julia_fractal.py`, lines 193, 200, 207, 214, 223. All these comments are speculation by the author of the program and are completely unnecessary. they will all be deleted.
```
# The full julia set
# This one looks like an hourglass to me
# This fractal reminds me of lakes, but it might remind somebody else of something else
# My grandmother has lace curtains that look JUST LIKE THIS!
# This is how you write colors for computers
```
* There is an instance of convoluted variables at `src/julia_fractal.py`, lines 224-237. Here several color codes are defined, but never used. They will be deleted.
```
WHITE = '#ffffff'  # white
RED = '#ff0000'  # red
BLUE = '#00ff00'  # blue
GREEN = '#0000ff'  # green
BLACK = '#000000'  # black
ORANGE = '#ffa50'  # orange
TOMATO = '#ff6347'  # tomato (a shade of red)
HOT_PINK = '#ff69b4'  # hot pink (a kind of pink)
REBECCA_PURPLE = '#663399'  # Rebecca Purple
LIME_GREEN = '#89ff00'  # lime green (brighter than regular green)
GREY0 = '#000000'  # gray 0 - basically the same as black
GRAY37 = '#5e5e5e'  # gray 37 - lighter than black and gray 36
GREY74 = '#bdbdbd'  # gray 74 - almost white
GRAY99 = '#fcfcfc'  # gray 99 - almost white
```
* There are a bunch of instances of bad comments at `src/julia_fractal.py`, lines 243-259. Pretty much all of these comments either share too much or are otherwise unnecessary. All will be deleted.
```
    # Look, I  know globals are bad, but I don't know how else to use those
    # variables in here if I don't do it this way.  I didn't take any fancy CS
    # classes, sue me
    global tkPhotoImage
    global win

    # Note the time of when we started so we can measure performance improvements
    b4 = time()
    # Set up the GUI so that we can display the fractal image on the screen
    win = Tk()

    # the size of the image we will create is 512x512 pixels
    s = 512
    # construct a new TK PhotoImage object that is 512 pixels square...
    tkPhotoImage = PhotoImage(width=512, height=512)
    # ... and use it to make a picture of a fractal
    # TODO - should I have named this function "makeFractal()" or maybe just "makePicture"?
```
* There is an instance of redundant code at `src/julia_fractal.py`, lines 262-269. Here the file is written to a .png file 4 times, where only the first time is necessary. The remaining 3 will be deleted.
```
    # Write out the Fractal into a .gif image file
    tkPhotoImage.write(i + ".png")
    print(f"Done in {time() - b4:.3f} seconds!", file=sys.stderr)

    # Output the Fractal into a .png image
    tkPhotoImage.write(i + ".png")
    print("Wrote picture " + i + ".png")
    tkPhotoImage.write(i + ".png")
```
* There is an instance of dead code at `src/julia_fractal.py`, lines 277-295. This is a commented out if __name__ == '__main__' section which appears to have the same functionality as main.py. because it is commented out and there is already a working version in main.py, It can safely be deleted.
```
## This is some weird Python thing... but all of the tutorials do it, so here we go
#if __name__ == '__main__':
#    # Process command-line arguments, allowing the user to select their fractal
#    if len(sys.argv) < 2:
#        print("Please provide the name of a fractal as an argument")
#        for i in f:
#            print(f"\t{i}")
#        sys.exit(1)
#
#    elif sys.argv[1] not in f:
#        print(f"ERROR: {sys.argv[1]} is not a valid fractal")
#        print("Please choose one of the following:")
#        for i in f:
#            print(f"\t{i}")
#        sys.exit(1)
#
#    else:
#        fratcal_config = getFractalConfigurationDataFromFractalRepositoryDictionary(f, sys.argv[1])
#        julia_main(fratcal_config)
```
