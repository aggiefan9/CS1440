import sys
from ImagePainter import ImagePainter
from FractalFactory import fractalFactory
from PaletteFactory import paletteFactory

# if no arguments are given, choose default values
if len(sys.argv) < 2:
    frac = fractalFactory()
    pal = paletteFactory(length=frac.iterations)
elif len(sys.argv) < 3:
    frac = fractalFactory(sys.argv[1])
    pal = paletteFactory(length=frac.iterations)
else:
    frac = fractalFactory(sys.argv[1])
    pal = paletteFactory(name=sys.argv[2], length=frac.iterations)

imgpnt = ImagePainter(frac, pal)
imgpnt.printFractal()
