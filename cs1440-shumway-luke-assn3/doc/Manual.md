# Bingo! User Manual

**Your instructions go here**
Upon running the program, the user will be confronted with a main menu, which lays out the two options of creating a deck, or exiting the program (via keystrokes "C" and "X" respectively).
If the user types "X" (the keystrokes ARE case-sensitive) and enter the program will quit and the journey ends.
If, however, the user types "C" and hits enter, they will then be prompted for the following inputs:
number of cards(between 2 and 8192), card size(between 3 and 16(the card will then have that many rows AND columns(it is square))),
and the highest number seen on each card (which is anywhere from twice the size squared to four times the size squared (give or take)).
After entering the required inputs, a second menu will be displayed giving the user three additional commands to perform on the newly created deck, plus the "X" from before.
The three commands are as follows: "P" to Print a card to the screen, "D" to Display the whole deck to the screen, and "S" to Save the whole deck to a file
NOTE: (the options are again case-sensitive)
If the print Card option is chosen, the user will be asked which card the user would like to print from the deck (and the number of cards will be displayed for reference).
If the display deck option is chosen, each card in the deck will be printed to the screen in an ascii format. 
If the save deck option is chosen, the user will be prompted to input the file path of a file where the deck will be saved (NOTE: the contents of the file will be identical to the format of the display deck option)
The save deck option does not result in anything printed to the screen, and after each option is resolved, the same menu with the four options ("P", "D", "S", and "X") will be displayed
This same loop will repeat until the "X" option is selected, after which the program will quit

Possible errors the user could experience:
If at any time the user enters an invalid command, there will not be an error, but rather the same menu as before will be presented and the user will have another chance to enter a valid command.
If when the user is prompted for a number value (such as the number of cards, the size of the cards, the highest number shown on the cards, and the card number desired for printing) the user instead enters any input other than an integer in the desired range, the program will again display the same menu and a second chance will be given (even until 70 times 7 chances)
If when the user is prompted for a file to save the deck in, the user enters a bad file path, (whether the file does not exist or there is a typo of any kind or the permissions needed to open and write to are not granted) the program will quit with an error informing the user the file could not be opened or does not exist
