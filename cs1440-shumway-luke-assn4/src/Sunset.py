from Palette import Palette
from colour import Color


class Sunset(Palette):
    def __init__(self, length):
        offset = length % 3
        fadeLen = length // 3
        purple = Color('purple')
        blue = Color('blue')
        black = Color('black')
        white = Color('white')
        red = Color('red')
        self.__array = []
        if offset > 0:
            self.__array.extend(list(purple.range_to(white, fadeLen + 1)))
        else:
            self.__array.extend(list(purple.range_to(white, fadeLen)))
        if offset > 1:
            self.__array.extend(list(white.range_to(red, fadeLen + 2))[1:])
        else:
            self.__array.extend(list(white.range_to(red, fadeLen + 1))[1:])
        if offset > 2:
            self.__array.extend(list(red.range_to(black, fadeLen + 2))[1:])
        else:
            self.__array.extend(list(red.range_to(black, fadeLen + 1))[1:])

    def getColor(self, n):
        return self.__array[n].get_hex_l()

    def getLength(self):
        return len(self.__array)
