import sys
from Mandelbrot import Mandelbrot
from Julia import Julia
from BurningShipJulia import BurningShipJulia


def fractalFactory(fcf=None):
    if fcf is None:
        print("FractalFactory: Creating default fractal", file=sys.stderr)
        default = {'type': 'mandelbrot', 'pixels': 640, 'centerx': 0.0, 'centery': 0.0, 'axislength': 4.0, 'iterations': 100, 'imagename': 'mandelbrot'}
        return Mandelbrot(default)
    else:
        frac = {}
        file = open(fcf)
        for line in file:
            if line.strip().lower().startswith('type'):
                frac['type'] = line.split(':')[1].strip().lower()
            elif line.strip().lower().startswith('pixels'):
                frac['pixels'] = line.split(':')[1].strip()
            elif line.strip().lower().startswith('axislength'):
                frac['axislength'] = line.split(':')[1].strip()
            elif line.strip().lower().startswith('iterations'):
                frac['iterations'] = line.split(':')[1].strip()
            elif line.strip().lower().startswith('creal'):
                frac['creal'] = line.split(':')[1].strip()
            elif line.strip().lower().startswith('cimag'):
                frac['cimag'] = line.split(':')[1].strip()
            elif line.strip().lower().startswith('centerx'):
                frac['centerx'] = line.split(':')[1].strip()
            elif line.strip().lower().startswith('centery'):
                frac['centery'] = line.split(':')[1].strip()
        if '/' in fcf:
            frac['imagename'] = fcf.split('/')[-1].split('.')[0]
        elif '\\' in fcf:
            frac['imagename'] = fcf.split('\\')[-1].split('.')[0]
        else:
            frac['imagename'] = fcf.split('.')[0]
    fracChecking(frac)
    if frac['type'] == 'julia':
        fractal = Julia(frac)
    elif frac['type'] == 'mandelbrot':
        fractal = Mandelbrot(frac)
    else:
        fractal = BurningShipJulia(frac)

    return fractal


def fracChecking(frac):
    try:
        for param in ['pixels', 'iterations']:
            if param not in frac:
                raise RuntimeError(f"The value of the '{param}' parameter is missing")
            else:
                frac[param] = int(frac[param])
    except ValueError:
         raise RuntimeError(f"The value of the '{param}' parameter is not an integer")
    try:
        for param in ['axislength', 'centerx', 'centery']:
            if param not in frac:
                raise RuntimeError(f"The value of the '{param}' parameter is missing")
            else:
                frac[param] = float(frac[param])
    except ValueError:
        raise RuntimeError(f"The value of the '{param}' parameter is not a number")
    if 'type' not in frac:
        raise RuntimeError(f"The value of the 'type' parameter is missing")
    elif frac['type'] in ['julia', 'burningshipjulia']:
        try:
            for param in ['creal', 'cimag']:
                if param not in frac:
                    raise RuntimeError(f"The value of the '{param}' parameter is missing")
                else:
                    frac[param] = float(frac[param])
        except ValueError:
            raise RuntimeError(f"This is a Julia fractal, but the '{param}' parameter was not specified")
    elif frac['type'] not in ['mandelbrot', 'julia', 'burningshipjulia']:
        raise NotImplementedError("Invalid fractal type requested")
