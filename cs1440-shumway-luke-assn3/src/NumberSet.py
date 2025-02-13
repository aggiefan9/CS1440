import random


class NumberSet():
    def __init__(self, size):
        """NumberSet constructor"""
        self.__m_numbers = []
        for i in range(1, size + 1):
            self.__m_numbers.append(i)

    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return len(self.__m_numbers)

    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        if 0 <= index < self.getSize():
            return self.__m_numbers[index]
        else:
            return None

    def randomize(self):
        """void function: Shuffle this NumberSet"""
        random.shuffle(self.__m_numbers)

    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""
        if self.getSize() < 1:
            return None
        else:
            return self.__m_numbers.pop()
