import unittest
import RGB, Noir


class TestPalettes(unittest.TestCase):
    def test_palette_length(self):
        for i in range(112, 120):  # 8 goes into 112 and 120 evenly, whereas the numbers in between do not, this tests that all iteration counts can be accepted
            rgb = RGB.RGB(i)
            noir = Noir.Noir(i)
            self.assertEqual(rgb.getLength(), i)
            self.assertEqual(noir.getLength(), i)
