import unittest
import Card
import NumberSet


class TestCard(unittest.TestCase):
    def setUp(self):
        idnum, size = 0, 3
        self.card0 = Card.Card(idnum, size, (3*size*size))

        idnum, size = 1, 5
        self.card1 = Card.Card(idnum, size, (2*size*size))

        idnum, size = 2, 16
        self.card2 = Card.Card(idnum, size, (3*size*size))

        idnum, size = 3, 8
        self.card3 = Card.Card(idnum, size, (2*size*size))


    def test_getSize(self):
        """Assert that card size is as expected"""
        self.assertEqual(self.card0.getSize(), 3)
        self.assertEqual(self.card1.getSize(), 5)
        self.assertEqual(self.card2.getSize(), 16)
        self.assertEqual(self.card3.getSize(), 8)

    def test_getID(self):
        """Assert that card ID number is as expected"""
        self.assertIsNotNone(self.card0)
        self.assertEqual(self.card0.getId(), 0)

        self.assertIsNotNone(self.card1)
        self.assertEqual(self.card1.getId(), 1)

        self.assertIsNotNone(self.card2)
        self.assertEqual(self.card2.getId(), 2)

        self.assertIsNotNone(self.card3)
        self.assertEqual(self.card3.getId(), 3)

    def test_hasFreeSquares(self):
        """
        Ensure that odd-numbered cards have 1 "Free!" square in the center
        This test expects that "Free!" squares are represented by string values
        and all other squares contain integer values.

        Update this test if you use another way to store "Free!" squares
        """
        # Check every single square of the 3x3 card
        self.assertIsInstance(self.card0.getSquare(0, 0), int)
        self.assertIsInstance(self.card0.getSquare(0, 1), int)
        self.assertIsInstance(self.card0.getSquare(0, 2), int)
        self.assertIsInstance(self.card0.getSquare(1, 0), int)
        self.assertIsInstance(self.card0.getSquare(1, 1), str)
        self.assertIsInstance(self.card0.getSquare(1, 2), int)
        self.assertIsInstance(self.card0.getSquare(2, 0), int)
        self.assertIsInstance(self.card0.getSquare(2, 1), int)
        self.assertIsInstance(self.card0.getSquare(2, 2), int)

        # Examine the 3x3 region at the center of this card
        self.assertIsInstance(self.card1.getSquare(1, 1), int)
        self.assertIsInstance(self.card1.getSquare(1, 2), int)
        self.assertIsInstance(self.card1.getSquare(1, 3), int)
        self.assertIsInstance(self.card1.getSquare(2, 1), int)
        self.assertIsInstance(self.card1.getSquare(2, 2), str)
        self.assertIsInstance(self.card1.getSquare(2, 3), int)
        self.assertIsInstance(self.card1.getSquare(3, 1), int)
        self.assertIsInstance(self.card1.getSquare(3, 2), int)
        self.assertIsInstance(self.card1.getSquare(3, 3), int)

        # Examine the 2x2 region around the "center" of the even-numbered cards
        self.assertIsInstance(self.card2.getSquare(7, 7), int)
        self.assertIsInstance(self.card2.getSquare(7, 8), int)
        self.assertIsInstance(self.card2.getSquare(8, 7), int)
        self.assertIsInstance(self.card2.getSquare(8, 8), int)

        self.assertIsInstance(self.card3.getSquare(3, 3), int)
        self.assertIsInstance(self.card3.getSquare(3, 4), int)
        self.assertIsInstance(self.card3.getSquare(4, 3), int)
        self.assertIsInstance(self.card3.getSquare(4, 4), int)

    def test_noDuplicates(self):
        """Ensure that cards do not contain duplicate numbers"""

        # Because numbers are randomly assigned there *may* be a chance that a
        # duplicate slips through.  Without auditing the source code, we can't
        # prove there is no possibility this could happen.  The best we can do
        # with an automated test is to generate a bunch of cards, check them all
        # for duplicates until we are confident enough

        size = 16
        for i in range(10001):
            # The largest card with the smallest allowed NumberSet gives the
            # highest probability of a repeated number, if that is possible

            if i % 1000 == 0:
                print(f"Searching for a card with a duplicate number #{i}...")

            seen = set()
            c = Card.Card(i, size, (2*size*size))
            for row in range(size):
                for col in range(size):
                    n = c.getSquare(row, col)
                    self.assertNotIn(n, seen)
                    seen.add(n)



if __name__ == '__main__':
    unittest.main()
