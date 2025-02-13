from Fractal import Fractal


class Julia(Fractal):
    def __init__(self, frac):
        self.dict = frac
        self.pixels = frac['pixels']
        self.axislength = frac['axislength']
        self.iterations = frac['iterations']
        self.min = [frac['centerx'] - (frac['axislength'] / 2), frac['centery'] - (frac['axislength'] / 2)]
        self.max = [frac['centerx'] + (frac['axislength'] / 2), frac['centery'] + (frac['axislength'] / 2)]
        self.imagename = frac['imagename']
        self.constant = complex(frac['creal'], frac['cimag'])

    def count(self, z):
        for i in range(self.iterations):
            z = z * z + self.constant
            if abs(z) > 2:
                return i
        return self.iterations - 1
