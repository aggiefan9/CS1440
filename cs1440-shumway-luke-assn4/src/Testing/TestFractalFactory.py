import unittest
import FractalFactory as ff


class TestFractalFactory(unittest.TestCase):
    def test_fractal_config_dictionary_return(self):
        defaultFCDict = {'type': 'mandelbrot', 'pixels': 640, 'centerx': 0.0, 'centery': 0.0, 'axislength': 4.0, 'iterations': 100, 'imagename': 'mandelbrot'}
        branches512FCF = "data/branches512.frac"
        branches512FCDict = {'type': 'mandelbrot', 'pixels': 640, 'centerx': 0.354957789387306, 'centery': -0.338644137198173, 'axislength': 5.05822370716613e-06, 'iterations': 512, 'imagename': 'branches512'}
        fullJuliaFCF = "data/fulljulia.frac"
        fullJuliaFCDict = {'type': 'julia', 'pixels': 1024, 'centerx': 0.0, 'centery': 0.0, 'axislength': 4.0, 'iterations': 78, 'imagename': 'fulljulia', 'creal': -1, 'cimag': 0}
        burningShipFCF = "data/burningship.frac"
        burningShipFCDict = {'type': 'burningshipjulia', 'pixels': 512, 'centerx': 0.0, 'centery': 0.0, 'axislength': 4.0, 'iterations': 64, 'imagename': 'burningship', 'creal': -.598, 'cimag': .9225}

        default = ff.fractalFactory()

        self.assertIn('type', default.dict)
        self.assertIn('pixels', default.dict)
        self.assertIn('centerx', default.dict)
        self.assertIn('centery', default.dict)
        self.assertIn('axislength', default.dict)
        self.assertIn('iterations', default.dict)
        self.assertIn('imagename', default.dict)

        self.assertIn('type', ff.fractalFactory(branches512FCF).dict)
        self.assertIn('pixels', ff.fractalFactory(branches512FCF).dict)
        self.assertIn('centerx', ff.fractalFactory(branches512FCF).dict)
        self.assertIn('centery', ff.fractalFactory(branches512FCF).dict)
        self.assertIn('axislength', ff.fractalFactory(branches512FCF).dict)
        self.assertIn('iterations', ff.fractalFactory(branches512FCF).dict)
        self.assertIn('imagename', ff.fractalFactory(branches512FCF).dict)

        self.assertIn('type', ff.fractalFactory(fullJuliaFCF).dict)
        self.assertIn('pixels', ff.fractalFactory(fullJuliaFCF).dict)
        self.assertIn('centerx', ff.fractalFactory(fullJuliaFCF).dict)
        self.assertIn('centery', ff.fractalFactory(fullJuliaFCF).dict)
        self.assertIn('axislength', ff.fractalFactory(fullJuliaFCF).dict)
        self.assertIn('iterations', ff.fractalFactory(fullJuliaFCF).dict)
        self.assertIn('imagename', ff.fractalFactory(fullJuliaFCF).dict)
        self.assertIn('creal', ff.fractalFactory(fullJuliaFCF).dict)
        self.assertIn('cimag', ff.fractalFactory(fullJuliaFCF).dict)

        self.assertIn('type', ff.fractalFactory(burningShipFCF).dict)
        self.assertIn('pixels', ff.fractalFactory(burningShipFCF).dict)
        self.assertIn('centerx', ff.fractalFactory(burningShipFCF).dict)
        self.assertIn('centery', ff.fractalFactory(burningShipFCF).dict)
        self.assertIn('axislength', ff.fractalFactory(burningShipFCF).dict)
        self.assertIn('iterations', ff.fractalFactory(burningShipFCF).dict)
        self.assertIn('imagename', ff.fractalFactory(burningShipFCF).dict)
        self.assertIn('creal', ff.fractalFactory(burningShipFCF).dict)
        self.assertIn('cimag', ff.fractalFactory(burningShipFCF).dict)

        self.assertEqual(default.dict['type'], defaultFCDict['type'])
        self.assertEqual(default.pixels, defaultFCDict['pixels'])
        self.assertEqual(default.min[0], defaultFCDict['centerx'] - (defaultFCDict['axislength'] / 2))
        self.assertEqual(default.min[1], defaultFCDict['centery'] - (defaultFCDict['axislength'] / 2))
        self.assertEqual(default.max[0], defaultFCDict['centerx'] + (defaultFCDict['axislength'] / 2))
        self.assertEqual(default.max[1], defaultFCDict['centery'] + (defaultFCDict['axislength'] / 2))
        self.assertEqual(default.axislength, defaultFCDict['axislength'])
        self.assertEqual(default.iterations, defaultFCDict['iterations'])
        self.assertEqual(default.imagename, defaultFCDict['imagename'])

        self.assertEqual(ff.fractalFactory(branches512FCF).dict['type'], branches512FCDict['type'])
        self.assertEqual(ff.fractalFactory(branches512FCF).pixels, branches512FCDict['pixels'])
        self.assertEqual(ff.fractalFactory(branches512FCF).min[0], branches512FCDict['centerx'] - (branches512FCDict['axislength'] / 2))
        self.assertEqual(ff.fractalFactory(branches512FCF).min[1], branches512FCDict['centery'] - (branches512FCDict['axislength'] / 2))
        self.assertEqual(ff.fractalFactory(branches512FCF).max[0], branches512FCDict['centerx'] + (branches512FCDict['axislength'] / 2))
        self.assertEqual(ff.fractalFactory(branches512FCF).max[1], branches512FCDict['centery'] + (branches512FCDict['axislength'] / 2))
        self.assertEqual(ff.fractalFactory(branches512FCF).axislength, branches512FCDict['axislength'])
        self.assertEqual(ff.fractalFactory(branches512FCF).iterations, branches512FCDict['iterations'])
        self.assertEqual(ff.fractalFactory(branches512FCF).imagename, branches512FCDict['imagename'])

        self.assertEqual(ff.fractalFactory(fullJuliaFCF).dict['type'], fullJuliaFCDict['type'])
        self.assertEqual(ff.fractalFactory(fullJuliaFCF).pixels, fullJuliaFCDict['pixels'])
        self.assertEqual(ff.fractalFactory(fullJuliaFCF).min[0], fullJuliaFCDict['centerx'] - (fullJuliaFCDict['axislength'] / 2))
        self.assertEqual(ff.fractalFactory(fullJuliaFCF).min[1], fullJuliaFCDict['centery'] - (fullJuliaFCDict['axislength'] / 2))
        self.assertEqual(ff.fractalFactory(fullJuliaFCF).max[0], fullJuliaFCDict['centerx'] + (fullJuliaFCDict['axislength'] / 2))
        self.assertEqual(ff.fractalFactory(fullJuliaFCF).max[1], fullJuliaFCDict['centery'] + (fullJuliaFCDict['axislength'] / 2))
        self.assertEqual(ff.fractalFactory(fullJuliaFCF).axislength, fullJuliaFCDict['axislength'])
        self.assertEqual(ff.fractalFactory(fullJuliaFCF).iterations, fullJuliaFCDict['iterations'])
        self.assertEqual(ff.fractalFactory(fullJuliaFCF).imagename, fullJuliaFCDict['imagename'])
        self.assertEqual(ff.fractalFactory(fullJuliaFCF).constant, complex(fullJuliaFCDict['creal'], fullJuliaFCDict['cimag']))

        self.assertEqual(ff.fractalFactory(burningShipFCF).dict['type'], burningShipFCDict['type'])
        self.assertEqual(ff.fractalFactory(burningShipFCF).pixels, burningShipFCDict['pixels'])
        self.assertEqual(ff.fractalFactory(burningShipFCF).min[0], burningShipFCDict['centerx'] - (burningShipFCDict['axislength'] / 2))
        self.assertEqual(ff.fractalFactory(burningShipFCF).min[1], burningShipFCDict['centery'] - (burningShipFCDict['axislength'] / 2))
        self.assertEqual(ff.fractalFactory(burningShipFCF).max[0], burningShipFCDict['centerx'] + (burningShipFCDict['axislength'] / 2))
        self.assertEqual(ff.fractalFactory(burningShipFCF).max[1], burningShipFCDict['centery'] + (burningShipFCDict['axislength'] / 2))
        self.assertEqual(ff.fractalFactory(burningShipFCF).axislength, burningShipFCDict['axislength'])
        self.assertEqual(ff.fractalFactory(burningShipFCF).iterations, burningShipFCDict['iterations'])
        self.assertEqual(ff.fractalFactory(burningShipFCF).imagename, burningShipFCDict['imagename'])
        self.assertEqual(ff.fractalFactory(burningShipFCF).constant, complex(burningShipFCDict['creal'], burningShipFCDict['cimag']))
