import unittest
import Julia, Mandelbrot, BurningShipJulia


class TestFractals(unittest.TestCase):
    def test_countReturn_Julia(self):
        fullJuliaFCDict = {'type': 'julia', 'pixels': 1024, 'centerx': 0.0, 'centery': 0.0, 'axislength': 4.0, 'iterations': 78, 'imagename': 'fulljulia.png', 'creal': -1, 'cimag': 0}
        for i in range(100):
            for j in range(100):
                self.assertTrue(type(Julia.Julia(fullJuliaFCDict).count(complex(i, j))) is int)
                self.assertFalse(type(Julia.Julia(fullJuliaFCDict).count(complex(i, j))) is (str or bool or float))

    def test_countReturn_Mandelbrot(self):
        mandelbrotFCDict = {'type': 'mandelbrot', 'pixels': 640, 'centerx': 0.0, 'centery': 0.0, 'axislength': 4.0, 'iterations': 100, 'imagename': 'mandelbrot.png'}
        for i in range(100):
            for j in range(100):
                self.assertTrue(type(Mandelbrot.Mandelbrot(mandelbrotFCDict).count(complex(i, j))) is int)
                self.assertFalse(type(Mandelbrot.Mandelbrot(mandelbrotFCDict).count(complex(i, j))) is (str or bool or float))

    def test_countReturn_BurningShip(self):
        burningShipFCDict = {'type': 'burningshipjulia', 'pixels': 512, 'centerx': 0.0, 'centery': 0.0, 'axislength': 4.0, 'iterations': 64, 'imagename': 'burningship.png', 'creal': -.598, 'cimag': .9225}
        for i in range(100):
            for j in range(100):
                self.assertTrue(type(BurningShipJulia.BurningShipJulia(burningShipFCDict).count(complex(i, j))) is int)
                self.assertFalse(type(BurningShipJulia.BurningShipJulia(burningShipFCDict).count(complex(i, j))) is (str or bool or float))

