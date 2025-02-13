# Fractal Visualizer User Manual

*TODO: Your instructions go here*

This program is mainly intended to be run through the command line. The command to run the program is `python main.py [FRACTAL_CONFIGURATION_FILE_PATH] [PALETTE]`.
If either the Fractal Configuration File Path or the Palette Name is not provided, the program will choose defaults (the basic mandelbrot set, and the rgb (red-green-blue) palette)
If an incorrect file path is provided, the program will quit with python's open() error, informing the user that the file either does not exist, or cannot be opened.
If an incorrect palette name is provided, the program will quit with a NotImplementedError, informing the user that an invalid palette has been provided.
If the file provided contains errors, but can still be open, The program will quit with a RuntimeError, or possibly a NotImplementedError if the fractal type is invalid, informing the user of the specific error committed.
The parameters are listed below, along with the required data types and an explanation of the purpose of each, in the event the user wishes to create their own file:
* type - *str* **required**
  * Informs the program which fractal formula to apply.
  * For example, this may be Mandelbrot, Julia or BurningShipJulia.
* centerX - *float* **required**
  * The center point of the image along the X axis.
  * a.k.a. the "real" axis.
* centerY - *float* **required**
  * The center point of the image along the Y axis
  * a.k.a. the "imaginary" axis.
* axisLength - *float* **required**
  * Defines the size of the square on the complex plane this image covers.
  * Because the images are square, both axes are the same size.
  * Making this value smaller results in a zoomed-in image.
  * Making this value larger results in a zoomed-out image.
* pixels - *int* **required**
  * The width (and height) of the image in pixels.
  * Increasing this parameter increases:
    * the size of the image.
    * the amount of detail visible in the image.
    * the amount of time it takes to generate the image.
* iterations - *int* **required**
  * The number of iterations the central for loop runs before giving up on coloring a pixel.
  * This is equal to the number of colors in the image.
  * Increasing this parameter means increasing...
    * ...the amount of time it takes to render the image
    * ...the amount detail visible in the image, provided your color palette has enough distinct, contrasting colors
* creal and cimag - *float* **optional**
  * The real and imaginary components of the C constant which is used by fractals defined by a variation of the Julia formula.
  * These items are required only for fractals using a variation of the Julia formula.
  * These configuration items are ignored by the Mandelbrot forumula.

After a correct input is provided, the program will open a Tk interface window which will proceed to draw, line by line, the chosen fractal.
After the fractal has been drawn, the console will display a message informing the user of the total time it took to draw said fractal, along with the writing(creation) of a .png file of the image.
The final message output to the console will inform the user that to exit the program, they will need to close the Tk interface window, which will have remained open the entire time.
Upon closing the Tk interface window, the program will exit and the user can view the .png file created (in the directory from which the command was run).