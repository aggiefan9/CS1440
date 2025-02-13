# Tests the NumberSet Class

import unittest
import NumberSet


class TestNumberSet(unittest.TestCase):
    def setUp(self):
        self.ns0 = NumberSet.NumberSet(0)
        self.ns18 = NumberSet.NumberSet(18)
        self.ns8192 = NumberSet.NumberSet(8192)

    def test_getSize(self):
        """Ensure that a NumberSet's size is as expected""" 
        self.assertIsNotNone(self.ns0)
        self.assertIsNotNone(self.ns18)
        self.assertIsNotNone(self.ns8192)
        self.assertEqual(self.ns0.getSize(), 0)
        self.assertEqual(self.ns18.getSize(), 18)
        self.assertEqual(self.ns8192.getSize(), 8192)

    def test_get(self):
        """Ensure that a NumberSet's gracefully handles requests for out-of-bounds numbers""" 
        # In my implementation getting an invalid index results in None
        self.assertIsNotNone(self.ns18.get(17))
        self.assertIsNotNone(self.ns18.get(0))
        self.assertIsNone(self.ns18.get(-1))
        self.assertIsNone(self.ns18.get(18))

    def test_getNext(self):
        """Ensure that a NumberSet's .getNext() method can be safely called more times than the quantity of nubmers it contains"""
        # In my implementation, once a NumberSet is exhausted, repeated invocations of `.getNext()` returns None
        for i in range(1, 19):
            self.assertIsNotNone(self.ns18.getNext())
        self.assertIsNone(self.ns18.getNext())
        self.assertIsNone(self.ns18.getNext())

        for i in range(1, 8193):
            self.assertIsNotNone(self.ns8192.getNext())
        self.assertIsNone(self.ns8192.getNext())
        self.assertIsNone(self.ns8192.getNext())

    def test_noDuplicates(self):
        """Ensure that a NumberSet contains no duplicates"""

        # Here I use a set to quickly and easily detect duplicates:
        # First, create a list of all the numbers yielded from a NumberSet
        # Then convert that list into a set
        # If the length of the list is not equal to that of the set, then there
        # must have been duplicates in the list
        l_ns = [self.ns0.getNext() for i in range(self.ns0.getSize()) ]
        s_ns = set(l_ns)
        self.assertEqual(len(l_ns), len(s_ns))

        l_ns = [self.ns18.getNext() for i in range(self.ns18.getSize()) ]
        s_ns = set(l_ns)
        self.assertEqual(len(l_ns), len(s_ns))

        l_ns = [self.ns8192.getNext() for i in range(self.ns8192.getSize()) ]
        s_ns = set(l_ns)
        self.assertEqual(len(l_ns), len(s_ns))


if __name__ == '__main__':
    unittest.main()
