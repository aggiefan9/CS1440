import sys

import NumberSet


class Card():
    def __init__(self, idnum, size, numberMax):
        """Card constructor"""
        self.__m_id = idnum
        self.__m_size = size
        self.__m_numbers = []
        for i in range(self.__m_size):
            self.__m_numbers.append([])
        numberSet = NumberSet.NumberSet(numberMax)
        numberSet.randomize()
        for row in range(self.__m_size):
            for col in range(self.__m_size):
                if self.__m_size % 2 == 1 and self.__m_size // 2 == row and row == col:
                    self.__m_numbers[row].append("FREE")
                else:
                    self.__m_numbers[row].append(numberSet.getNext())

    def getId(self):
        """Return an integer: the ID number of the card"""
        return self.__m_id

    def getSize(self):
        """Return an integer: the size of one dimension of the card.
        A 3x3 card will return 3, a 5x5 card will return 5, etc.
        """
        return self.__m_size

    def getSquare(self, row, col):
        """Return the value in the Bingo square at (row, col) """
        return self.__m_numbers[row][col]

    def print(self, file=sys.stdout):
        """void function:
        Prints a card to the screen or to an open file object"""
        print()
        print(f"Card #{self.getId()}")
        for row in range(self.__m_size):
            print("+", end="")
            print("------+" * self.__m_size)
            for col in range(self.__m_size):
                print("|", end="")
                print(format(self.getSquare(row, col), "^6"), end="")
            print("|")
        print("+", end="")
        print("------+" * self.__m_size)

