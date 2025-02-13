import Deck
import Menu
import math


class UserInterface():
    def __init__(self):
        pass

    def run(self):
        """Present the main menu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
        menu = Menu.Menu("Main")
        menu.addOption("C", "Create a new deck")
        
        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "C":
                self.__createDeck()
            elif command == "X":
                keepGoing = False

    def __createDeck(self):
        """Command to create a new Deck"""
        # TODO: Get the user to specify the card size, max number, and number of cards
        cardSize = self.__getIntegerInput("Enter card size", 3, 16)
        maxNum = self.__getIntegerInput("Enter max number", 2*cardSize*cardSize, math.floor(3.9*cardSize*cardSize))
        numCards = self.__getIntegerInput("Enter number of cards", 2, 8192)
        # TODO: Create a new deck
        self.__m_currentDeck = Deck.Deck(cardSize=cardSize, cardCount=numCards, numberMax=maxNum)
        # TODO: Display a deck menu and allow use to do things with the deck
        self.__deckMenu()

    def __getIntegerInput(self, prompt, m, n):
        """
        Prompt the user for an integer in the range [m, n] INCLUSIVE
        If the provided input is NOT an integer NOR in the range, repeat the prompt
        Otherwise, convert the user's value to an integer and return it.
        """
        keepGoing = True
        while keepGoing:
            print("\n" + prompt + f" [{m} - {n}]: ")
            num = input()
            if m <= int(num) <= n:
                return int(num)
            else:
                print(f"Please input a number in the range [{m} - {n}]")

    def __getStringInput(self, prompt):
        """
        Prompt the user for a string and return it
        """
        print("\n" + prompt + ": ")
        return input()

    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
        menu = Menu.Menu("Deck")
        menu.addOption("P", "Print a card to the screen")
        menu.addOption("D", "Display the whole deck to the screen")
        menu.addOption("S", "Save the whole deck to a file")

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                print()
                self.__m_currentDeck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False

    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getIntegerInput("Id of card to print", 1, self.__m_currentDeck.getCardCount())
        if cardToPrint > 0:
            print()
            self.__m_currentDeck.print(idx=cardToPrint)

    def __saveDeck(self):
        """Command to save a deck to a file"""
        fileName = self.__getStringInput("Enter output file name")
        if fileName != "":
            # TODO: open a file and pass to currentDeck.print()
            outputStream = open(fileName, 'w')
            self.__m_currentDeck.print(file=outputStream)
            outputStream.close()
            print("Done!")
