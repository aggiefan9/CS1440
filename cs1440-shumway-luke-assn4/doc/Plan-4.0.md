# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

*   A detailed written description of the problem this program aims to solve.
*   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.

This program aims to display a number of different fractals to the screen via the tkinter module. Using complex numbers to determine both the location and color of each pixel,
this program draws, pixel by pixel, one of the provided fractals with different colors to illustrate the beauty of complex math.

A good solution to this program will take a user's input of which fractal to draw, and will then parse through a canvas painting pixel by pixel the image desired.
With regards to the code, the functions in mbrot_fractal.py and julia_fractal.py will be clear (as possible with complex math) and easy to read (again, to the extent possible with complex math)
without the excess lines of code either unused or unreachable, and without (to a certain extent) global variables.

Looking at the starter code, there is not a lot I already know, however the following are things I have noticed that I could potentially eliminate to refactor the code:
* global variables
* declaring variables multiple times before use
* code after return statements
* commented out code (for the most part can be deleted)
* (seemingly) arbitrary numbers/constants (Magic numbers as described in class)

Some challenges I foresee (at this point) are as follows:
* The color pallete (I have no idea how it works, but why are only some colors named?)
* I still don't fully understand how tkinter works (like the commands and stuff, but there doesn't appear to be very many so hopefully it will be a non-issue)

## Phase 1: System Analysis *(10%)*

**Deliver:**

*   List all of the data that is used by the program, making note of where it comes from.
*   Explain what form the output will take.
*   Describe what algorithms and formulae will be used (but don't write them yet).

This is all the data used by the source code

main.py
* list of the fractals - list of strings (from sys.argv)

mbrot_fractal.py
* Color Names (8 at the top) - strings (color codes (hex code))
* palette - list of strings (color codes again)
  * there are two different palettes declared, but the first is commented out
* MAX_ITERATIONS - integer (length of the palette)
* z - first declared as zero, later re declared as a global complex number variable
* seven - a constant representing the number 7 as float
* TWO - same as seven but for integer 2
* img - First declared as none outside any functions, but in the mbrot_main function is declared as a PhotoImage (probably something with tkinter)
* mainWindowObject - None and appears to have no other use
* colorOfThePixel function (takes a 'c' and 'palette' parameter. palette is just the color palette, and c is a complex number (comes from paint() function))
  * z - declared as global and set to a complex number
  * MAX_ITERATIONS - declared as global (I think it's the same MAX_ITERATIONS as above, just now globalized)
  * iter - global (appears to only be used in the for loop)
  * len - literally just a rebrand of MAX_ITERATIONS
  * TWO - same TWO as before, now just globalized
* window - declared as None outside any functions but in mbrot_main function is declared as Tk() (probably the main tkinter window)
* paint function (takes a 'fractals' and 'imagename' parameter. fractals is a dictionary of fractals and their axes and centers, and imagename is the name of the fractal to access from fractals)
  * palette - same as original palette, just globalized
  * img - same as the img above, just globalized
  * fractal - dictionary of the center and axis length for the imagename in fractals
    * minx - obtained from the fractal dictionary above (center x minus the axis length)
    * maxx - just like minx but adding the axis length instead of subtracting it
    * miny - just like minx but with center y instead of center x
    * maxy - just like maxx but with center y instead of center x (this variable is never used)
  * canvas - a Canvas tkinter widget upon which our fractal will be printed (with parameters 'window' (the one from above that always appears to be None), width (set as 512), height(also set to 512), and bg(background color) (set to #000000 (black)))
    * canvas is then used to create an image with coordinates of 256,256 (half of 512, but I don't know if thats coincidental) the image is img(the variable) and state is "normal" (tkinter stuff that I don't understand)
  * pixelsize - the absolute value of maxx minus minx all divided by 512 (almost positive it is the same 512 as the window width/height)
  * portion - the integer division product of 512 divided by 64 (never used)
  * total_pixels - 1048576 (appears to be arbitrary) (also never used)
  * row - only used in the for loop, but is incremented down by 1 from 512 to 0 (should be the same 512 as window width/height)
  * col - only used in the for loop, but is for range(512) (should again be the same 512 as window width/height)
  * x - the minx plus (col multiplied by pixelsize)
  * y - the miny plut (row multiplied by pixelsize)
* pixelsWrittenSoFar function (takes 'rows' and 'cols' parameters) (never used)
* colorOfThePixel funtion (again but this one is commented out)
  * appears to be the same as the earlier function, but slightly worse (I didn't know that was possible)
    * ie. no new functionality
* images - a dictionary of dictionaries (the sub-dictionaries are the fractal names with their centers and axes)
  * there is a duplicate entry, 'spiral1'
* mbrot_main function (takes an 'image' parameter, which is the name of one of the fractals in the images dictionary)
  * img - same img as before, but globalized (again)
    * here it is set to be a PhotoImage with width and height of 512 (tkinter stuff again)
  * before - the start time
  * window - same window as before, but globalized and set to be Tk() (an instance of the class)
  * after - the end time

julia_fractal.py
* a BUNCH of unused imports
* getColorFromPalette (takes a 'z' parameter, which is a complex number)
  * c - the Julia Constant (a complex number)
  * grad - declared later outside any functions as a list of color codes (equivalent to palette from mbrot), but globalized here
  * win - globalized both here and in julia_main, it is only set to Tk() in julia_main, so not even sure why it is globalized yet again here
  * z - taken from the parameter above, but here it is incremented in the fractal form (itself times (itself plus the julia constant))
* getFractalConfigurationDataFromFractalRepositoryDictionary function (it is only used in some code at the bottom that is commented out)
  * a bunch of nested if and for loops that could be simplified with a simple "if name in dictionary"
* tkPhotoImage - declared here as None, later globalized and set to a PhotoImage in julia_main (equivalent to img from mbrot)
* makePictureOfFractal (takes 'f', 'i', 'e', 'w', 'g', 'p', 'W', and 's' parameters (only 'f', 'w', 'p', 'W', and 's' are used))
  * min - a tuple of the min x and min y calculated from the grad dictionary (equivalent to the combination of both minx and miny from mbrot)
    * f - the parameter above is the fractal name (equivalent to imagename from mbrot)
  * max - same as min, but with the max x and max y (equivalent to the combination of maxx and maxy from mbrot)
  * tk_Interface_PhotoImage_canvas_pixel_object - a Canvas tkinter widget (with parameters 'win' (the one from above that always appears to be None), width (set as s), height(also set to s), and bg (set to W ))
    * (equivalent to canvas from mbrot)
    * It is then used to create an image with coordinates (s/2, s/2), image of p (the parameter above), and state "normal"
  * area_in_pixels - appears to be arbitrarily set to 640 * 640 (also never used) (not even the same number as total_pixels from mbrot)
  * size - the max x (0 index of the max tuple) minus the min x (0 index of the min tuple) all divided by s
  * fraction_of_pixels_writtenSoFar = the size divided by 64 (updated at the end of this function, but never used) (probably equivalent to portion from mbrot)
  * r - only used in for loop, incremented down by 1 from s to 0 (equivalent to row from mbrot)
  * c - only used in for loop, from range(s) (equivalent to col from mbrot)
  * x - the min x (0 index of the min tuple) plus c times size
  * y - set to 0 and immediately updated to the min y (1 index of the min tuple) plus r times size
  * c2 - the result of getColorFromPalette(complex(x, y)) (but is declared three times (identical every time))
* grad - the global variable mentioned above, but here it is just declared as a list of color codes (outside any functions)
* f - a dictionary of dictionaries (the sub-dictionaries are the fractal names with their centers and axes) (equivalent to images from mbrot)
* Color Names (14 of them) - strings of color codes (all never used)
* julia_main function (takes an 'i' parameter)
  * tkPhotoImage - same as above, but here it is globalized and set to a PhotoImage with width and height both 512
  * win - same as above, but here it is globalized and set to a Tk() (instance of the class)
  * b4 - (clever shorthand for before) start time
  * s - set to 512 (but never used)
* if __name__ == '__main__': section but commented out
  * appears to be similar in functionality to main.py

WOW. sorry that was long-winded. I now realize that might not have been necessary or even what was asked for. but I did it and it helped me understand the program, so I'm going to leave it there.
I guess for the refactoring, the data used will be as follows:
* name of fractal to print - String from sys.argv
* dictionary of information for the name of fractal - obtained from FractalInformation
* size of window/image - will probably be constants
* coordinates for the fractal - obtained from the dictionary
* iteration count - used to determine color of pixel, and obtained from either Julia or Mandelbrot (depending on the fractal type)
* color for each pixel - obtained from Palette (specific for each type of fractal)
* the tkinter window, canvas widget, and photoimage widget - imported from tkinter

Now for the output. It will take the form of a tkinter window which will have a canvas widget inside which will have a photoimage inside,
which I think will also be created and stored as a png file in the directory from which the program was run.

And the algorithms: (NOTE: these are the names of the modules suggested in the instructions readme, but the implementation should just be as simple as a 1:1 ratio for modules and algorithms)
* Main - the entry point. ensures the arguments are valid, and calls ImagePainter
* ImagePainter - creates a tkinter window, with the canvas and photoimage widgets inside, and displays the fractal. calls either Julia or Mandelbrot (depending on which type of fractal it is) and Palette
* Julia - returns the iteration count from a complex coordinate
* Mandelbrot - same as Julia, but different math inside
* Palette - takes the iteration count and returns the pixel color (has two different palettes, one for Julia and another for Mandelbrot)


## Phase 2: Design *(30%)*

**Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.

Function Signatures:
* Main() ## take input(the name of a fractal to print) and check the validity of the name and either call the function to print it, or inform the user of the possible options of fractals to print
  * parameters: sys.argv
  * if the fractal name (sys.argv[1]) provided is incorrect, or isn't provided at all (it is not in the dictionary in FractalInformation.py)
    * if fractal name is invalid, inform user name is invalid
    * display the list of fractal names and quit
  * if the fractal name is correct, call the ImagePainter function with the dictionary corresponding to the fractal name input as the parameter
* ImagePainter() ## take input(a fractal to print) and display that fractal to the screen in a tkinter GUI window, displaying the fractal line by line
  * parameters: dictionary containing the appropriate information (such as the x and y min and max)
  * get start time usint time.time()
  * Declare Constants
    * SIZE - 512 (pixel width and height)
    * MAX_ITER_MBROT - length of mandelbrot color palette (from Palette.py)
    * MAX_ITER_JULIA - length of julia color palette (from Palette.py)
    * BLACK - #000000 (hex code for black, used in Canvas creation)
    * pixelSize (not a constant only because it changes depending on the fractal) - set to the difference between the max x and min x divided by SIZE
  * create a Tk() instance
  * create a Canvas with parameters(None, width=SIZE, height=SIZE, bg=BLACK)
  * pack the Canvas within its parent widget (the Tk() instance above)
  * create a PhotoImage with width and height equal to SIZE
  * use the create_image() method on the Canvas to create an image with parameters ((SIZE/2, SIZE/2), image=the PhotoImage above, state="normal")
  * for loop through rows in range(SIZE to 0 incremented down by 1)
    * for loop through columns in range(0 to SIZE incremented up by 1)
      * set x equal to the min x plus the column multiplied by the pixelSize
      * set y equal to the min y plus the row multiplied by the pixelSize
      * call the Julia/Mandelbrot function (depending on which fractal type) with parameters (complex(x, y), MAX_ITER_(JULIA/MBROT))
        * store the result as 'index'
      * set the color equal to the value at index[index] of the appropriate palette from Palette.py (either Julia or Mandelbrot)
      * use the put() method on the PhotoImage with parameters (color, (column, SIZE minus row))
    * use the update() method on the Tk() instance to update the image with each row
  * use the write() method on the PhotoImage with parameter (name of the fractal + ".png") to save the picture
  * print the time taken to print fractal using the difference between time.time() and the start time
  * print a message informing the user a new file was created with the name "(name of the fractal).png"
  * use the mainloop() method to keep the window on the screen
* Julia() ## take input(complex number, and maximum iteration) and compute and return the iteration count of the julia function for that point
  * parameters: z (complex(x, y)), and a MAX_ITER
  * declare the Julia Constant - complex(-1.0, 0.0)
  * for i in range(MAX_ITER)
    * z = z * z + c
    * if the absolute value of z is > 2
      * return i
  * return MAX_ITER - 1
* Mandelbrot() ## take input(complex number, and maximum iteration) and compute and return the iteration count of the mandelbrot function for that point
  * parameters: c (complex(x, y)), and a MAX_ITER
  * initialize z - complex(0, 0)
  * for i in range(MAX_ITER)
    * z = z * z + c
    * if the absolute value of z is > 2
      * set z equal to 2.0
      * return i
  * return MAX_ITER - 1
* Palette.py and FractalInformation.py do not contain any functions, but are rather lists/dictionaries respectively.

## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working Python code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.

There isn't a lot of input to test with this program. The tests one can run are from the command line:
`python src/main.py full-julia` - The expected output is a Tk interface window opening, and the fractal printing our line by line. upon completion, the program saves the file as a .png file in the directory from which the command was run.
`python src/main.py` - The expected output is a message informing the user a fractal name needs to be provided, and a list of possible fractal names.
`python src/main.py DOESNTEXIST` - The expected output is a message informing the user a fractal name from the following list needs to be provided, along with a list of possible fractal names.

To view tests that test the behind the scenes functionality of this program, view the files in the Testing directory. a brief description is provided here
* TestFractalINformation tests that the dictionary containing the fractal configuration information sub dictionaries is of the appropriate length, contains the appropriate entries, and that each sub dictionary also contains the right fields of the appropriate types (str, float, etc.)
* TestFractals tests the formula used in calculating the color of each pixel, for both Julia and Mandelbrot, specifically that the output is an integer
* TestImagePainter tests that the calculations are done correctly, and that the correct color is chosen for both the Julia and the Mandelbrot equations
* TestPalette tests that the respective palettes for the julia and mandelbrot series are of the correct type (str) and length



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
    *   What parts of your program are sloppily written and hard to understand? (maybe) the ImagePainter class. But even that is fairly simple and understandable
        *   Are there parts of your program which you aren't quite sure how/why they work? - not really
        *   If a bug is reported in a few months, how long would it take you to find the cause? - not long. if it is a color-related bug, it probably came from either the Palette or Julia/Mandelbrot files. if it is anything else, it most likely came from ImagePainter
    *   Will your documentation make sense to
        *   anybody besides yourself? - hopefully. I feel as though it is fairly straightforward
        *   yourself in six month's time? - absolutely
    *   How easy will it be to add a new feature to this program in a year? - pretty easy, especially after the object-oriented stuff done next sprint
    *   Will your program continue to work after upgrading
        *   your computer's hardware? - yes
        *   the operating system? - yes
        *   to the next version of Python? - yes
