import unittest

from Testing import TestImagePainter, TestFractals, TestFractalFactory, TestPalettes, TestPaletteFactory


suite = unittest.TestSuite()
tests = (TestImagePainter.TestImagePainter, TestFractals.TestFractals, TestFractalFactory.TestFractalFactory, TestPalettes.TestPalettes, TestPaletteFactory.TestPaletteFactory)
for test in tests:
    suite.addTest(unittest.makeSuite(test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
