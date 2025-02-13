import unittest
import PaletteFactory as pf
import RGB, Noir


class TestPaletteFactory(unittest.TestCase):
    def test_palette_return(self):
        length = 512
        rgb = RGB.RGB(length)
        noir = Noir.Noir(length)
        testDefault = pf.paletteFactory(length=length)
        testRGB = pf.paletteFactory(length=length, name="RGB")
        testNoir = pf.paletteFactory(length=length, name="Noir")
        for i in range(length):
            self.assertEqual(rgb.getColor(i), testDefault.getColor(i))
            self.assertEqual(rgb.getColor(i), testRGB.getColor(i))
            self.assertEqual(noir.getColor(i), testNoir.getColor(i))
