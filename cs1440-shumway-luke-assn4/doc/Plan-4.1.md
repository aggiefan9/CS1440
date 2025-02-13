# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

*   A detailed written description of the problem this program aims to solve.
*   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.

This program (or rather this refactoring of the program) strives to solve the problem of maintenance and universality, or being able to interact with a standardized input format, and allow the program to have much greater freedom and capabilities regarding functionality. (sorry that sounded a little wordy, I have a specific word in mind for all that, but I cant remember it, so this is what I have).
It also strives to better modularize (I think that's a word) the programs functionality, allowing for better testing, and even the possible implementations of new features in the future.

A good solution contains the 11 modules/classes (main, Fractal Factory, Fractal, Julia, Mandelbrot, BurningShipJulia, PaletteFactory, Palette, Palette1, Palette2, ImagePainter) and correctly applies inheritance and polymorphism within the Fractal-Julia-Mandelbrot-BurningShipJulia and the Palette-Palette1-Palette2 chains, and correctly funnels the two trees through the FractalFactory and the PaletteFactory modules.
* In the main module the input will be read from sys.argv and FractalFactory, PaletteFactory, and ImagePainter will be called respectively to generate a fractal, a palette, and an ImagePainter object that displays the appropriate fractal with the appropriate color palette.
* In the FractalFactory module the file will be read through and used to produce a dictionary containing the appropriate configuration information of the fractal, which will then be used to create and return a Fractal object (either Mandelbrot, Julia, or BurningShipJulia)
  * The default value for the fractal configuration dictionary will be defined as the mandelbrot config file, which will be hard coded into the program (the actual dictonary, not the path to a file), and passed to the constructor in place of the user-defined dictionary
* In the Fractal class the __init__() and count() method structures are set forth, but nothing more (because the two methods require the information of the subclasses) This just provides a structure so that the objects of the subclasses can be used polymoprphically (with polymorphism, I know that's not a word.)
* In the Julia class, a subclass of Fractal, the __init__() method is defined, which saves the fractal configuration data from the dictionary created by FractalFactory.
  * The count method is defined with a complex number as the input, and uses the max iteration count from the fractal configuration dictionary in a for loop and returns the number of iterations tried before the formula produces a value greater than 2.0 (the specific formula for incrementation is as follows: z = z * z + c, where z is the input, and c is the constant defined as complex(-1,0))
* In the Mandelbrot class, a subclass of Fractal, the __init__() method is defined, which saves the fractal configuration data from the dictionary created by FractalFactory. 
  * The count method is defined with a complex number as the input, and uses the max iteration count from the fractal configuration dictionary in a for loop and returns the number of iterations tried before the formula produces a value greater than 2.0 (the specific formula for incrementation is as follows: z = z * z + c, where c is the input, and z is initializes as complex(0,0))
* In the BurningShipJulia class, a subclass of Fractal, the __init__() method is defined, which saves the fractal configuration data from the dictionary created by FractalFactory. 
  * The count method is defined with a complex number as the input, and uses the max iteration count from the fractal configuration dictionary in a for loop and returns the number of iterations tried before the formula produces a value greater than 2.0 (the specific formula for incrementation is as follows: z = |z| * |z| + c, where z is the input, and c is the constant defined as complex(-1,0), and the || surrounding z represent the absolute value (or math.fabs() in actual implementation))
* In the PaletteFactory module the name of the color palette will be read (if it is provided) which will then be used to create and return an Palette object (either Red-Green-Blue or Black-White)
  * The default color palette will be the Red-Green-Blue palette (starts red, then fades to black, then to green, then back to black, then to blue)
  * One of the parameters for the PaletteFactory function will be the max iteration count (from the fractal configuration dictionary) this will be passed from main.py to the PaletteFactory module 
* In the Palette class the __init__() and getColor() method structures are set forth, but nothing more (because the two methods require the information of the subclasses) This just provides a structure so that the objects of the subclasses can be used polymoprphically (with polymorphism, I know that's not a word.)
* In the Red-Green-Blue class (in the program it will be RGB), a subclass of Palette, the __init__() method is defined, which saves the max iteration count passed through PaletteFactory, and creates an array of colors, beginning with Red, then fading to black, then to green, then back to black, then finally to blue, all in (max iterations divided by 4) steps.
  * The getColor() method is defined with an integer as the input, and returns the item at index[n] within the array (which will be a string with the following format: "#RRGGBB")
* In the Black-White class (in the program it will be Noir), a subclass of Palette,  the __init__() method is defined, which saves the max iteration count passed through PaletteFactory, and creates an array of colors, alternating between Black and White (max iterations divided by 2) times.
  * The getColor() method is defined with an integer as the input, and returns the item at index[n] within the array (which will be a string with the following format: "#RRGGBB")
    * NOTE: This method behaves exactly the same as the other palette, to me it seems as though it could be moved to the Palette superclass, but the code requirements specify that we should do it this way, so that is how it will be done.
* In the ImagePainter class, the actual printing of the fractal will be done, which behaves the same as the refactored version (in my refactoring I even refactored it as a class, so it will be largely unchanged)
  * One change that will be made is the parameters will now just be a Fractal object (subclass of course) and a Palette object (same, a subclass). The if-else statements used to handle the different types of fractals will be replaced with just fractal.count(), and the palette.getColor(n), as the objects are polymorphic.
  * The length of the palette will also not be a necessary member of the class, and will also be deleted. All othe functionality will remain the same (more or less. eg. the dictionary keys for the x min, etc. will be replaced with variable fields specific to the class)

Things I know how to do:
* Funnel both the Palette and Fractal generation through the respective 'factories'
* Initialize both of the color palettes with the correct colors using colour.Color and the range_to() method to get the correct number of steps
* The getColor() method
* The __init__() and count() methods for all the subclasses
* The ImagePainter changes (mostly accidental, not really essential)
* The PaletteFactory function (I'm implementing it as a function within a module, not a class)
* The default fractal configuration dictionary for the FractalFactory function (again, a function instead of a class)

Challenges I forsee:
* I'm not really sure completely how abstract classes and concrete/subclasses work
* I have an idea for how I'm going to read the information of the config file and slurp it into a dictionary, but there are still a lot of unknowns
  * I assume We're going to open the files and read them line by line and take the good key and store their appropriate values in the dictionary, the exact specifics of that I can tell will be a bit of a challenge
    * ie. it will just require a bit of fine-tuning


## Phase 1: System Analysis *(10%)*

**Deliver:**

*   List all of the data that is used by the program, making note of where it comes from.
*   Explain what form the output will take.
*   Describe what algorithms and formulae will be used (but don't write them yet).

Data used in the program:
* main.py
  * fractal-config-file-name (string from sys.argv)
    * used to open a file of the corresponding name by Fractal Factory
  * color-palette-name (string from sys.argv)
  * fractal - a Fractal object (instance of a subclass)
  * palette - a Palette object (instance of a subclass)
  * imafePainter - an ImagePainter object
* FractalFactory
  * fractal-config-file-name - passed as a parameter
    * used to open a file of the corresponding name
      * used to produce a fractal-config dictionary
  * a default fractal-config dictionary - hardcoded
  * an instance of a Fractal subclass - what is returned by the function
* Fractal
  * no data - just a skeleton for the subclasses
* Mandelbrot
  * fractal-config dictionary
    * used to initialize the following member variables
      * type
      * min (a list containing the min x and min y)
      * max (a list containing the max x and max y)
      * axisLength
      * pixels
      * pixelsize
      * iterations
  * count() method
    * a complex number - passed as a parameter
    * uses self.iterations
    * returns the iteration (or self.iterations minus 1 if the end of the for loop is reached)
* Julia
  * fractal-config dictionary
    * used to initialize the following member variables
      * type
      * min (a list containing the min x and min y)
      * max (a list containing the max x and max y)
      * axisLength
      * pixels
      * pixelsize
      * iterations
      * creal
      * cimag
  * count() method
    * a complex number - passed as a parameter
    * uses self.iterations
    * returns the iteration (or self.iterations minus 1 if the end of the for loop is reached)
* BurningShipJulia
  * fractal-config dictionary
    * used to initialize the following member variables
      * type
      * min (a list containing the min x and min y)
      * max (a list containing the max x and max y)
      * axisLength
      * pixels
      * pixelsize
      * iterations
      * creal
      * cimag
  * count() method
    * a complex number - passed as a parameter
    * uses self.iterations
    * returns the iteration (or self.iterations minus 1 if the end of the for loop is reached)
* PaletteFactory
  * iteration count - passed as a parameter 
  * palette-name - passed as a parameter
    * used to create an instance of a Palette subclass - what is returned by the function
  * a default palette name
    * used to create an instance of a Palette subclass - what is returned by the function
* Palette
  * no data - just a skeleton for the subclasses
* RGB
  * iteration count - passed as a parameter
    * used to determine the length of the array member variable
  * array - list containing strings of color codes
  * red - an instance of colour.Color with color='red'
  * green - an instance of colour.Color with color='green'
  * blue - an instance of colour.Color with color='blue'
  * black - an instance of colour.Color with color='black'
* Noir
  * iteration count - passed as a parameter
    * used to determine the length of the array member variable
  * array - list containing strings of color codes
  * black - an instance of colour.Color with color='black'
  * white - an instance of colour.Color with color='white'
* ImagePainter
  * a Palette object (subclass) - passed as a parameter
  * a Fractal object (subclass) - passed as a parameter
  * window - an instance of Tk() class
  * canvas - a tkinter Canvas
  * photoImage - a tkinter PhotoImage

Output will take the form of a Tkinter window, which displays the chosen fractal, as well as a .png file of the fractal saved to the directory from which the program was run (cwd in the command line when the command was run)

Algorithms
* main.py
  * none
* FractalFactory
  * determine if a correct fractal-config-file was provided
    * if none are provided, use the default
    * if a file was provided, proceed as normal (we'll let python fail if it's incorrect)
  * read the file and slurp the contents into a dictionary
    * open the file, read it line by line, disregard lines beginning with #, slurp the keys and their respective values into a dictionary (all lowercase)
  * create the appropriate Fractal subclass object
    * if the 'file' key in the dictionary is equal to 'julia', create Julia object
      * if 'mandelbrot', create a Mandelbrot object
      * if 'burningshipjulia', create a BurningShipJulia object
      * else raise a NotImplemented error
* Fractal
  * none
* Mandelbrot
  * count()
    * within a for loop, increment z (z = z * z + c) and check if |z| is greater than 2
      * if yes, return the iteration count
    * at the end of the for loop, return max iterations minus 1
* Julia
  * count()
    * within a for loop, increment z (z = z * z + c) and check if |z| is greater than 2
      * if yes, return the iteration count
    * at the end of the for loop, return max iterations minus 1
* BurningShipJulia
  * count()
    * within a for loop, increment z (z = |z| * |z| + c) and check if |z| is greater than 2
      * if yes, return the iteration count
    * at the end of the for loop, return max iterations minus 1
* PaletteFactory
  * determine if a correct palette-name was proided
    * if none are provided, use the default
    * if an incorrect name was provided, raise a NotImplemented error
    * if a correct name was provided, proceed as normal
* Palette
  * none
* RGB
  * initialize the array
    * add the fade from color red to black
    * add the fade from color black to green (excluding the first color (black))
    * add the fade from color green to black (excluding the first color (green))
    * add the fade from color black to blue (excluding the first color (black))
  * getColor()
    * return the get_hex_l() method of tne item at array[n]
* Noir
  * initialize the array
    * within a for loop, if i % 2 == 0, append the color black
      * otherwise, append the color white
  * getColor()
    * return the get_hex_l() method of tne item at array[n]
* ImagePainter
  * create the window, canvas, and photoImage, packing each within its parent
  * within a for loop, paint each pixel of the fractal, line by line
    * return palette.getColor(fractal.count())
    * update the window after each row
  * save the fractal png file using photoImage.write()


## Phase 2: Design *(30%)*

**Deliver:**

*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.

main.py
* Determine if a fractal config file and/or a color palette have been provided
  * If both, call the FractalFactory() and PaletteFactory() functions with sys.argv[1] and sys.argv[2] respectively as parameters
    * NOTE: the error checking will be done within the two factory functions
  * If only the name of a fractal config file (it is assumed that if there is only 1 argument (besides the name of the program) that it is a fractal config file), call the FractalFactory() function with sys.argv[1] as the parameter and PaletteFactory() without parameters
  * If neither a fractal config file nor a color palette are provided, call both the FractalFactory() and PaletteFactory() functions without any parameters
* Store the result of each FractalFactory() function call as fractal, a variable referencing a fractal object, and each PaletteFactory() function call as palette, a reference to a palette object
* Create an ImagePainter object (instance of the ImagePainter class) and pass fractal and palette as parameters
* Use the printFractal() method to display, and save, the fractal with the chosen color palette

FractalFactory
* Parameters: fcf (fractal config file name)
* create a dictionary, frac, to store all the fractal configuration settings
* if fcf = None return mandelbrot (a default dictionary with contents equivalent to the mandelbrot.frac file within the data directory)
* otherwise, file = open(fcf)
  * for each line in file
    * if line.strip.startswith('#'), continue
    * if line.strip.lowercase.startswith('type'), set the 'type' key in frac equal to the last half of the line
    * if line.strip.lowercase.startswith('pixels'), set the 'pixels' key in frac equal to the last half of the line
    * if line.strip.lowercase.startswith('axislength'), set the 'axisLength' key in frac equal to the last half of the line
    * if line.strip.lowercase.startswith('iterations'), set the 'iterations' key in frac equal to the last half of the line
    * if line.strip.lowercase.startswith('creal'), set the 'creal' key in frac equal to the last half of the line
    * if line.strip.lowercase.startswith('cimag'), set the 'cimag' key in frac equal to the last half of the line
    * if line.strip.lowercase.startswith('centerx'), set the 'centerx' key in frac equal to the last half of the line
    * if line.strip.lowercase.startswith('centery'), set the 'centery' key in frac equal to the last half of the line
  * set the 'imagename' key in frac equal to the last half of fcf (after the last / and with .png instead of whatever extension it had before)
  * if type is not a string, raise a RuntimeError
    * if type is not 'mandelbrot', 'julia', or 'burningshipjulia', raise a NotImplementedError
  * if pixels is not an int, raise a RuntimeError
  * if axislength is not a float, raise a RuntimeError
  * if iterations is not an int, raise a RuntimeError
  * if type=='julia' or 'burningshipjulia' and creal or cimag is not a float, raise a RuntimeError
  * if centerx or centery is not a float, raise a RuntimeError
* after parsing through each line, and ensuring the contents of the fractal config dictionary are correct, instantiate a fractal subclass corresponding to the 'type' key in the dictionary
  * ie. if type='julia' create a Julia object, if type='mandelbrot' create a Mandelbrot object, and if type='burningshipjulia' create a BurningShipJulia object
* return the created object

Fractal
* Parameters: frac (fractal configuration dictionary)
* Methods:
  * __init__(Parameters: frac)
    * raise NotImplementedError("Concrete subclass of Fractal must implement __init__")
  * count(Parameters: complex number)
    * raise NotImplementedError("Concrete subclass of Fractal must implement count() method")

Mandelbrot
* Parameters: frac (fractal configuration dictionary)
* Methods:
  * __init__(Parameters: frac)
    * set self.__type equal to the ['type'] entry in the dictionary
    * set self.pixels equal to the ['pixels'] entry in the dictionary
    * set self.axislength equal to the ['axislength'] entry in the dictionary
    * set self.iterations equal to the ['iterations'] entry in the dictionary
    * set self.min as a list with entry[0] equal to the ['centerx'] entry in the dictionary minus the ['axislength'] entry in the dictionary
      * set entry[1] equal to the ['centery'] entry in the dictionary minus the ['axislength'] entry in the dictionary
    * set self.max as a list with entry[0] equal to the ['centerx'] entry in the dictionary plus the ['axislength'] entry in the dictionary
      * set entry[1] equal to the ['centery'] entry in the dictionary plus the ['axislength'] entry in the dictionary
    * set self.imagename equal to the ['imagename'] entry in the dictionary
  * count(Parameters: c (a complex number))
    * create a variable, z, and set it as complex(0.0, 0.0)
    * for i in range(self.iterations)
      * z = z * z + c(the complex number parameter)
      * if abs(z) is greater than 2
        * return i
    * if the for loop runs to completion and has not returned a value, return self.iterations minus 1

Julia
* Parameters: frac (fractal configuration dictionary)
* Methods:
  * __init__(Parameters: frac)
    * set self.__type equal to the ['type'] entry in the dictionary
    * set self.pixels equal to the ['pixels'] entry in the dictionary
    * set self.axislength equal to the ['axislength'] entry in the dictionary
    * set self.iterations equal to the ['iterations'] entry in the dictionary
    * set self.min as a list with entry[0] equal to the ['centerx'] entry in the dictionary minus the ['axislength'] entry in the dictionary
      * set entry[1] equal to the ['centery'] entry in the dictionary minus the ['axislength'] entry in the dictionary
    * set self.max as a list with entry[0] equal to the ['centerx'] entry in the dictionary plus the ['axislength'] entry in the dictionary
      * set entry[1] equal to the ['centery'] entry in the dictionary plus the ['axislength'] entry in the dictionary
    * set self.constant as complex(the ['creal'] entry in the dictionary, the ['cimag'] entry in the dictionary)
    * set self.imagename equal to the ['imagename'] entry in the dictionary
  * count(Parameters: z (a complex number))
    * for i in range(self.iterations)
      * z = z * z + self.constant
      * if abs(z) is greater than 2
        * return i
    * if the for loop runs to completion and has not returned a value, return self.iterations minus 1

BurningShipJulia
* Parameters: frac (fractal configuration dictionary)
* Methods:
  * __init__(Parameters: frac)
    * set self.__type equal to the ['type'] entry in the dictionary
    * set self.pixels equal to the ['pixels'] entry in the dictionary
    * set self.axislength equal to the ['axislength'] entry in the dictionary
    * set self.iterations equal to the ['iterations'] entry in the dictionary
    * set self.min as a list with entry[0] equal to the ['centerx'] entry in the dictionary minus the ['axislength'] entry in the dictionary
      * set entry[1] equal to the ['centery'] entry in the dictionary minus the ['axislength'] entry in the dictionary
    * set self.max as a list with entry[0] equal to the ['centerx'] entry in the dictionary plus the ['axislength'] entry in the dictionary
      * set entry[1] equal to the ['centery'] entry in the dictionary plus the ['axislength'] entry in the dictionary
    * set self.constant as complex(the ['creal'] entry in the dictionary, the ['cimag'] entry in the dictionary)
    * set self.imagename equal to the ['imagename'] entry in the dictionary
  * count(Parameters: z (a complex number))
    * for i in range(self.iterations)
      * z = abs(z) * abs(z) + self.constant
      * if abs(z) is greater than 2
        * return i
    * if the for loop runs to completion and has not returned a value, return self.iterations minus 1

PaletteFactory
* Parameters: name (string), length (integer)
* if name was not provided, set name equal to 'RGB'
* if name was provided, check if it is valid
  * if name is not equal to either 'RGB' or 'Noir' raise a NotImplementedError
  * otherwise, instantiate a Palette subclass of the corresponding type
    * ie. if name='RGB' create an RGB object, if name='Noir' create a Noir object
    * return the object created

Palette
* Parameters: length (integer)
* Methods:
  * __init__(Parameters: length)
    * raise NotImplementedError("Concrete subclass of Palette must implement __init__")
  * getColor(Parameters: integer)
    * raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")

RGB
* Parameters: length (integer)
* Methods:
  * __init__(Parameters: length)
    * create a variable, fadeLen, and set it equal to length/8
    * create a variable, red, and set it equal to an instance of colour.Color with color='red'
    * create a variable, green, and set it equal to an instance of colour.Color with color='green'
    * create a variable, blue, and set it equal to an instance of colour.Color with color='blue'
    * create a variable, black, and set it equal to an instance of colour.Color with color='black'
    * create a variable, cyan, and set it equal to an instance of colour.Color with color='cyan'
    * create a variable, magenta, and set it equal to an instance of colour.Color with color='magenta'
    * create a variable, yellow, and set it equal to an instance of colour.Color with color='yellow'
    * set self.__array as an empty list
    * append the fade from black to red (using the range_to() method with fadeLen as the step parameter)
    * append the fade from red to green (using the range_to() method with fadeLen as the step parameter) - NOTE: the first item of this appendage will not be included, to avoid duplicate colors
    * append the fade from green to blue (using the range_to() method with fadeLen as the step parameter) - NOTE: the first item of this appendage will not be included, to avoid duplicate colors
    * append the fade from blue to black (using the range_to() method with fadeLen as the step parameter) - NOTE: the first item of this appendage will not be included, to avoid duplicate colors
    * append the fade from black to cyan (using the range_to() method with fadeLen as the step parameter) - NOTE: the first item of this appendage will not be included, to avoid duplicate colors
    * append the fade from cyan to magenta (using the range_to() method with fadeLen as the step parameter) - NOTE: the first item of this appendage will not be included, to avoid duplicate colors
    * append the fade from magenta to yellow (using the range_to() method with fadeLen as the step parameter) - NOTE: the first item of this appendage will not be included, to avoid duplicate colors
    * append the fade from yellow to black (using the range_to() method with fadeLen as the step parameter) - NOTE: the first item of this appendage will not be included, to avoid duplicate colors
  * getColor(Parameters: n (integer))
    * return the get_hex_l() method performed on self.__array[n (the parameter)]

Noir
* Parameters: length (integer)
* Methods:
  * __init__(Parameters: length)
    * create a variable, white, and set it equal to an instance of colour.Color with color='white'
    * create a variable, black, and set it equal to an instance of colour.Color with color='black'
    * set self.__array as an empty list
    * for i in range(length)
      * if i % 2 == 0, append the color black
      * otherwise, append the color white
  * getColor(Parameters: n (integer))
    * return the get_hex_l() method performed on self.__array[n (the parameter)]

ImagePainter ## take input(a Fractal object, and a Palette object) and display that fractal to the screen in a tkinter GUI window, displaying the fractal line by line
  * parameters: a Fractal object, and a Palette object
  * Methods:
    * __init__(Parameters: fractal (a fractal subclass object), palette (a palette subclass object))
      * set self.__fractal equal to fractal
      * set self.__palette equal to palette
      * set self.__SIZE equal to fractal.pixels
      * set self.__PIXEL_SIZE equal to fractal.axislength divided by self.__SIZE
      * set self.__window equal to a Tk instance
      * set self.__canvas equal to a Canvas with parameters(None, width=fractal.pixels, height=fractal.pixels, bg='#000000')
      * pack the Canvas within its parent widget (the Tk() instance above)
      * set self.__photoImage equal to a PhotoImage with width and height equal to fractal.pixels
      * use the create_image() method on self.__canvas to create an image with parameters ((self.__SIZE/2, self.__SIZE/2), image=self.__photoImage, state="normal")
    * printFractal(Parameters: None)
      * get start time usint time.time()
      * for loop through rows in range(self.__SIZE to 0 incremented down by 1)
        * for loop through columns in range(0 to self.__SIZE incremented up by 1)
          * set x equal to the fractal.min[0] plus the column multiplied by self.__PIXEL_SIZE
          * set y equal to the fractal.min[1] plus the row multiplied by self.__PIXEL_SIZE
          * set color equal to the result of the getPixelColor() method with x and y as parameters
          * use the put() method on the PhotoImage with parameters (color, (column, self.__SIZE minus row))
        * use the update() method on the Tk() instance to update the image with each row
      * get end time usint time.time()
      * call the saveFractal method of this class
      * print the time taken to print fractal using the difference between time.time() and the start time
      * print a message informing the user a new file was created with the name self.__fractal.imagename
      * use the mainloop() method to keep the window on the screen
    * getPixelColor(Parameters: x, y (both integers))
      * use the result of the count() method of self.__fractal with the parameter complex(x,y) as the parameter for the getColor() method of self.__palette and return the result
    * saveFractal(Parameters: None)
      * use the write() method on the PhotoImage with parameter (self.__fractal.imagename) to save the picture
  * NOTE: Most of this code is identical to the previous refactoring of ImagePainter (as I refactored it as a class already) the notable changes are the constants and the use of count() and getColor() on the Fractal and Palette objects


## Phase 3: Implementation *(15%)*

**Deliver:**

*   (More or less) working Python code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan

Interesting Events:
* It was actually harder than expected to implement the burningShipJulia formula, I even considered switching to the phoenix fractal formula, but decided to tough it out and finally I figured it out.
* getting the exact length of the RGB color palette proved more difficult than anticipated, particularly when dealing with iteration counts that do not divide evenly by 8.
* For like 3 hours, I couldnt get any of the non-basic fractals to print right. Turned out when changing instantiating the fractals, I set the minY equal to the minX instead, which caused a bunch of problems.
  * Lowkey I was super stressed, and threw away most of the code, and after rewriting it, I realized what I had done and felt pretty stupid

## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.

There isn't a lot of input to test with this program. The tests one can run are from the command line:
`python src/main.py` - The expected output is a Tk interface window opening, and the mandelbrot fractal printing out line by line with the RGB color palette (starts black, then fades through red, green, blue, black, cyan, magenta, yellow, and ends with black again). upon completion, the program saves the file as a .png file in the directory from which the command was run.
`python src/main.py data/fulljulia.frac` - The expected output is a Tk interface window opening, and the fractal printing out line by line with the RGB color palette. upon completion, the program saves the file as a .png file in the directory from which the command was run.
`python src/main.py data/DOESNOTEXIST` - The expected output is the program quitting with the open() error informing the user the file either does not exist, or cannot be open.
`python src/main.py data/fulljulia.frac DOESNTEXIST` - The expected output is the program quitting with a NotImplementedError informing the user that an invalid palette has been requested.
`python src/main.py data/burningship.frac Noir` - The expected output is a Tk interface window opening, and the fractal printing out line by line with the Noir color palette (alternating between black and white). upon completion, the program saves the file as a .png file in the directory from which the command was run.
`python src/main.py data/infalid.frac` - The expected output is the program quitting with both a ValueError and a RuntimeError informing the user of the incorrect parameter. NOTE: within this file there are a bunch of errors, and only the first is caught before quitting, so if you want to see all of them, fix only the error displayed to the console and re-run the command to see the next error.

To view tests that test the behind the scenes functionality of this program, view the files in the Testing directory. a brief description is provided here
* TestFractalFactory tests that the fractalFactory function returns the correct type of fractal, and parses through the file correctly to create the dictionary used in the fractal creation process.
* TestFractals tests the count function return of each of the fractal subclasses, and that the return value is an integer.
* TestImagePainter tests the formula used to get the color of each pixel, and specifically that it works every time with any type of fractal (testing the polymorphism).
* TestPaletteFactory tests that the paletteFactory function returns the correct type of palette, and that the palettes instantiate correctly.
* TestPalettes tests the instantiating process of each palette, and ensures that the length of the array of colors is always the same as the input.


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
    * What parts of your program are sloppily written and hard to understand? - The initialization of the RGB color palette (I can see how the bunch of if statements could be confusing, but it was the simplest way to initialize it correctly without rewriting a bunch of code) and fracChecking function within the FractalFactory module (there are a bunch of try-catch blocks for specificity in the error messages)
      * Are there parts of your program which you aren't quite sure how/why they work? - not really. I understand most everything in the program pretty well
      * If a bug is reported in a few months, how long would it take you to find the cause? - Depending on where it is found, pretty easy. (The caveot is if it is in the way the fractal is displayed, it could be in the ImagePainter or the Fractal Subclasses)
    * Will your documentation make sense to
        *   anybody besides yourself? - hopefully. even though the RGB and fracChecking parts are not the cleanest, they still follow good basic programming language stuff, so a programmer should know whats going on
        *   yourself in six months' time? - definitely. 
    * How easy will it be to add a new feature to this program in a year? - Depending on the feature, pretty easy. If the way the fractal configuration is taken changes, that would be a little tricky (it would just require a complete rewrite) but other features would be relatively simple to add
    * Will your program continue to work after upgrading
        *   your computer's hardware? - yes
        *   the operating system? - yes
        *   to the next version of Python? - to my knowledge
