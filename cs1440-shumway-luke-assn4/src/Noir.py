from Palette import Palette
from colour import Color


class Noir(Palette):
    def __init__(self, length):
        white = Color('white')
        black = Color('black')
        self.__array = []
        for i in range(length):
            if i % 2 == 0:
                self.__array.append(black)
            else:
                self.__array.append(white)

    def getColor(self, n):
        return self.__array[n].get_hex_l()

    def getLength(self):
        return len(self.__array)
