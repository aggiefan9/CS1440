import sys
from RGB import RGB
from Noir import Noir

def paletteFactory(length, name=None):
    if name is None:
        print("PaletteFactory: Creating default color palette", file=sys.stderr)
        palette = RGB(length)
    elif name == 'RGB':
        palette = RGB(length)
    elif name == 'Noir':
        palette = Noir(length)
    else:
        raise NotImplementedError("Invalid palette requested")

    return palette
