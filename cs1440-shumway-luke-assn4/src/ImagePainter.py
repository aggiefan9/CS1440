import time
import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop

class ImagePainter:
    def __init__(self, fractal, palette):
        self.__fractal = fractal
        self.__palette = palette
        self.__SIZE = fractal.pixels
        self.__PIXEL_SIZE = fractal.axislength / self.__SIZE

    def printFractal(self):
        start = time.time()
        self.__window = Tk()
        self.__canvas = Canvas(None, width=self.__SIZE, height=self.__SIZE, bg='#000000')
        self.__canvas.pack()
        self.__photoImage = PhotoImage(width=self.__SIZE, height=self.__SIZE)
        self.__canvas.create_image((self.__SIZE/2, self.__SIZE/2), image=self.__photoImage, state='normal')
        for row in range(self.__SIZE, 0, -1):
            for col in range(self.__SIZE):
                x = self.__fractal.min[0] + col * self.__PIXEL_SIZE
                y = self.__fractal.min[1] + row * self.__PIXEL_SIZE
                color = self.getPixelColor(x, y)
                self.__photoImage.put(color, (col, self.__SIZE - row))
            self.__window.update()
        self.saveFractal()
        end = time.time()
        print(f"Done in {end - start:.3f} seconds!", file=sys.stderr)
        print("Wrote picture " + self.__fractal.imagename + ".png", file=sys.stderr)
        print("Close the image window to exit the program", file=sys.stderr)
        mainloop()

    def getPixelColor(self, x, y):
        index = self.__fractal.count(complex(x, y))
        return self.__palette.getColor(index)

    def saveFractal(self):
        self.__photoImage.write(self.__fractal.imagename + ".png")
