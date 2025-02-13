from Fractal import Fractal


class Mandelbrot(Fractal):
    def __init__(self, frac):
        self.dict = frac
        self.pixels = frac['pixels']
        self.axislength = frac['axislength']
        self.iterations = frac['iterations']
        self.min = [frac['centerx'] - (frac['axislength'] / 2), frac['centery'] - (frac['axislength'] / 2)]
        self.max = [frac['centerx'] + (frac['axislength'] / 2), frac['centery'] + (frac['axislength'] / 2)]
        self.imagename = frac['imagename']

    def count(self, c):
        z = complex(0, 0)
        for i in range(self.iterations):
            z = z * z + c
            if abs(z) > 2:
                return i
        return self.iterations - 1
