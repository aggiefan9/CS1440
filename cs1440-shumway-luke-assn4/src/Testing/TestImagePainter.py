import unittest
import Julia, Mandelbrot, BurningShipJulia, RGB, Noir
import ImagePainter


class TestImagePainter(unittest.TestCase):
    def test_colorOfPixel(self):
        branches512FCDict = {'type': 'mandelbrot', 'pixels': 640, 'centerx': 0.354957789387306, 'centery': -0.338644137198173, 'axislength': 5.05822370716613e-06, 'iterations': 512, 'imagename': 'branches512.png'}
        fullJuliaFCDict = {'type': 'julia', 'pixels': 1024, 'centerx': 0.0, 'centery': 0.0, 'axislength': 4.0, 'iterations': 78, 'imagename': 'fulljulia.png', 'creal': -1, 'cimag': 0}
        burningShipFCDict = {'type': 'burningshipjulia', 'pixels': 512, 'centerx': 0.0, 'centery': 0.0, 'axislength': 4.0, 'iterations': 64, 'imagename': 'burningship.png', 'creal': -.598, 'cimag': .9225}
        julia = Julia.Julia(fullJuliaFCDict)
        mbrot = Mandelbrot.Mandelbrot(branches512FCDict)
        burningShip = BurningShipJulia.BurningShipJulia(burningShipFCDict)

        rgbJulia = RGB.RGB(julia.iterations)
        rgbMbrot = RGB.RGB(mbrot.iterations)
        rgbBurningShip = RGB.RGB(burningShip.iterations)

        ipJuliaRgb = ImagePainter.ImagePainter(julia, rgbJulia)
        ipMbrotRgb = ImagePainter.ImagePainter(mbrot, rgbMbrot)
        ipBurnRgb = ImagePainter.ImagePainter(burningShip, rgbBurningShip)

        self.assertEqual(ipMbrotRgb.getPixelColor(0, 0), rgbMbrot.getColor(rgbMbrot.getLength() - 1))  # end
        self.assertEqual(ipMbrotRgb.getPixelColor(-0.751, 1.1075), rgbMbrot.getColor(2)) # index[2]
        self.assertEqual(ipMbrotRgb.getPixelColor(-0.2, 1.1075), rgbMbrot.getColor(9)) # index[9]
        self.assertEqual(ipMbrotRgb.getPixelColor(-0.75, 0.1075), rgbMbrot.getColor(30)) # index[30] or [34]
        self.assertEqual(ipMbrotRgb.getPixelColor(-0.748, 0.1075), rgbMbrot.getColor(56)) # index[56] or [65]
        self.assertEqual(ipMbrotRgb.getPixelColor(-0.7562500000000001, 0.078125), rgbMbrot.getColor(38)) # index[38]
        self.assertEqual(ipMbrotRgb.getPixelColor(-0.7562500000000001, -0.234375), rgbMbrot.getColor(12)) # index[12]
        self.assertEqual(ipMbrotRgb.getPixelColor(0.3374999999999999, -0.625), rgbMbrot.getColor(10)) # index[10]
        self.assertEqual(ipMbrotRgb.getPixelColor(-0.6781250000000001, -0.46875), rgbMbrot.getColor(29)) # index[29]
        self.assertEqual(ipMbrotRgb.getPixelColor(0.4937499999999999, -0.234375), rgbMbrot.getColor(4)) # index[4]
        self.assertEqual(ipMbrotRgb.getPixelColor(0.3374999999999999, 0.546875), rgbMbrot.getColor(22)) # index[22] or [42]

        self.assertEqual(ipJuliaRgb.getPixelColor(0, 0), rgbJulia.getColor(rgbJulia.getLength() - 1))  # end
        self.assertEqual(ipJuliaRgb.getPixelColor(-0.751, 1.1075), rgbJulia.getColor(0)) # index[0]
        self.assertEqual(ipJuliaRgb.getPixelColor(-0.2, 1.1075), rgbJulia.getColor(0)) # index[0]
        self.assertEqual(ipJuliaRgb.getPixelColor(-0.75, 0.1075), rgbJulia.getColor(rgbJulia.getLength() - 1)) # end
        self.assertEqual(ipJuliaRgb.getPixelColor(-0.748, 0.1075), rgbJulia.getColor(rgbJulia.getLength() - 1)) # end
        self.assertEqual(ipJuliaRgb.getPixelColor(-0.7562500000000001, 0.078125), rgbJulia.getColor(rgbJulia.getLength() - 1)) # end
        self.assertEqual(ipJuliaRgb.getPixelColor(-0.7562500000000001, -0.234375), rgbJulia.getColor(5)) # index[5]
        self.assertEqual(ipJuliaRgb.getPixelColor(0.3374999999999999, -0.625), rgbJulia.getColor(2)) # index[2]
        self.assertEqual(ipJuliaRgb.getPixelColor(-0.6781250000000001, -0.46875), rgbJulia.getColor(2)) # index[2]
        self.assertEqual(ipJuliaRgb.getPixelColor(0.4937499999999999, -0.234375), rgbJulia.getColor(9)) # index[9]
        self.assertEqual(ipJuliaRgb.getPixelColor(0.3374999999999999, 0.546875), rgbJulia.getColor(3)) # index[3]

        self.assertEqual(ipBurnRgb.getPixelColor(0, 0), rgbBurningShip.getColor(30))  # index[30]
        self.assertEqual(ipBurnRgb.getPixelColor(-0.751, 1.1075), rgbBurningShip.getColor(26)) # index[26]
        self.assertEqual(ipBurnRgb.getPixelColor(-0.2, 1.1075), rgbBurningShip.getColor(4)) # index[4]
        self.assertEqual(ipBurnRgb.getPixelColor(-0.75, 0.1075), rgbBurningShip.getColor(2)) # index[2]
        self.assertEqual(ipBurnRgb.getPixelColor(-0.748, 0.1075), rgbBurningShip.getColor(2)) # index[2]
        self.assertEqual(ipBurnRgb.getPixelColor(-0.7562500000000001, 0.078125), rgbBurningShip.getColor(2)) # index[2]
        self.assertEqual(ipBurnRgb.getPixelColor(-0.7562500000000001, -0.234375), rgbBurningShip.getColor(2)) # index[2]
        self.assertEqual(ipBurnRgb.getPixelColor(0.3374999999999999, -0.625), rgbBurningShip.getColor(8)) # index[8]
        self.assertEqual(ipBurnRgb.getPixelColor(-0.6781250000000001, -0.46875), rgbBurningShip.getColor(3)) # index[3]
        self.assertEqual(ipBurnRgb.getPixelColor(0.4937499999999999, -0.234375), rgbBurningShip.getColor(4)) # index[4]
        self.assertEqual(ipBurnRgb.getPixelColor(0.3374999999999999, 0.546875), rgbBurningShip.getColor(6)) # index[6]

