# Tests the Deck Class

import unittest
import Deck


class TestDeck(unittest.TestCase):
    def setUp(self):
        size = 7
        self.deck2 = Deck.Deck(cardSize=size, cardCount=2, numberMax=3*size*size)

        size = 16
        self.deck16 = Deck.Deck(cardSize=size, cardCount=16, numberMax=3*size*size)

        self.deck8192 = Deck.Deck(cardSize=size, cardCount=8192, numberMax=3*size*size)

    def test_getCardCount(self):
        """Ensure that Decks contain expected number of cards"""
        self.assertEqual(self.deck2.getCardCount(), 2)
        self.assertEqual(self.deck16.getCardCount(), 16)
        self.assertEqual(self.deck8192.getCardCount(), 8192)

    def test_getCard(self):
        """Ensure that Cards can be accessed from within a Deck"""

        # In my implementation, an attempt to get a non-existent card results in `None`
        # Cards are indexed by their ID number

        self.assertIsNone(self.deck2.getCard(0))
        self.assertIsNotNone(self.deck2.getCard(1))
        self.assertIsNotNone(self.deck2.getCard(2))
        self.assertIsNone(self.deck2.getCard(3))

        self.assertIsNone(self.deck16.getCard(0))
        self.assertIsNotNone(self.deck16.getCard(8))
        self.assertIsNotNone(self.deck16.getCard(16))
        self.assertIsNone(self.deck16.getCard(17))

        self.assertIsNone(self.deck8192.getCard(0))
        self.assertIsNotNone(self.deck8192.getCard(4096))
        self.assertIsNotNone(self.deck8192.getCard(8192))
        self.assertIsNone(self.deck8192.getCard(8193))


if __name__ == '__main__':
    unittest.main()
