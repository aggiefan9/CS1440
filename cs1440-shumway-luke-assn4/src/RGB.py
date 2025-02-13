from Palette import Palette
from colour import Color


class RGB(Palette):
    def __init__(self, length):
        offset = length % 8
        fadeLen = length // 8
        red = Color('red')
        green = Color('green')
        blue = Color('blue')
        cyan = Color('cyan')
        magenta = Color('magenta')
        yellow = Color('yellow')
        black = Color('black')
        self.__array = []
        '''
        The if statements are the shortest way to add all the different fades while ensuring the length of the palette
        is exactly the correct length, while still accepting any iteration count
        '''
        # add the first fade to the array
        if offset > 0:
            self.__array.extend(list(black.range_to(red, fadeLen + 1)))
        else:
            self.__array.extend(list(black.range_to(red, fadeLen)))
        # add the second fade to the array
        if offset > 1:
            self.__array.extend(list(red.range_to(green, fadeLen + 2))[1:])
        else:
            self.__array.extend(list(red.range_to(green, fadeLen + 1))[1:])
        # add the third fade to the array
        if offset > 2:
            self.__array.extend(list(green.range_to(blue, fadeLen + 2))[1:])
        else:
            self.__array.extend(list(green.range_to(blue, fadeLen + 1))[1:])
        # add the fourth fade to the array
        if offset > 3:
            self.__array.extend(list(blue.range_to(black, fadeLen + 2))[1:])
        else:
            self.__array.extend(list(blue.range_to(black, fadeLen + 1))[1:])
        # add the fifth fade to the array
        if offset > 4:
            self.__array.extend(list(black.range_to(cyan, fadeLen + 2))[1:])
        else:
            self.__array.extend(list(black.range_to(cyan, fadeLen + 1))[1:])
        # add the sixth fade to the array
        if offset > 5:
            self.__array.extend(list(cyan.range_to(magenta, fadeLen + 2))[1:])
        else:
            self.__array.extend(list(cyan.range_to(magenta, fadeLen + 1))[1:])
        # add the seventh fade to the array
        if offset > 6:
            self.__array.extend(list(magenta.range_to(yellow, fadeLen + 2))[1:])
        else:
            self.__array.extend(list(magenta.range_to(yellow, fadeLen + 1))[1:])
        # add the eigth fade to the array. Because of the offset, this is always the same
        self.__array.extend(list(yellow.range_to(black, fadeLen + 1))[1:])

    def getColor(self, n):
        return self.__array[n].get_hex_l()

    def getLength(self):
        return len(self.__array)
