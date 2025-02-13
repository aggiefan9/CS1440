Maxwell Ramsdell
Max’s UML diagram was very well designed and has quite the exquisite touch. It is very easy to read and understand and
very straightforward. All of his Class diagram descriptions are accurate and contain just the perfect member variables,
with the exception of the deck class. Every member variable/ attribute is correct, there are just also a few variables
which I personally feel might be a little unnecessary. The first is the variable/ attribute named numberMax, which fees
unnecessary as the max number input from the user could just be passed straight to an instance of the NumberSet class
without needing to be passed and stored through the deck class instance. The second and third are similarly unnecessary,
and are the attributes/ variables named Card Size and Card Count. Both are inputs from the user, and could be utilized
without needing to be stored within the deck instance. The card count could be used in a for loop to create the
appropriate number of cards, and the card size could be passed directly to each instance of the card class. I would also
add the __init__() method to the user interface class, the menu class, and the menu option class. But other than that
everything is spectacular. With regards to the dependency arrows , they are all in the correct places with the correct
orientation. I would just change the words describing the relationships of the user interface and the deck classes, the
deck and the card classes, and the menu and menu option classes, all to “creates” because while it is true that they do
use the corresponding partners, the user interface creates an instance of the deck class, the deck class creates multiple
instances of the card class, and the menu class creates multiple instances of the menu option class. Again. Everything
else tho is impeccable and this is a really good first draft, with amazing quality. Great job Max!

Stockton Smith
Stockton’s UML diagram was very well designed and very easy to understand. The class diagrams had all of the correct
member variable/ attributes and the correct types, with a couple exceptions. first I would change the variable type of
the attribute m_cards of the deck class to be the list type, as it will be a list containing instances of the card class.
Second, I would add an additional member variable in the NumberSet class with the variable type of list to store the
actual list of numbers that can then be shuffled and passed to the bingo cards as needed. Other than that the class
diagrams are excellent. With the regards to the dependency arrows, I think all of them are correctly placed and have the
appropriate directions, and I even realized I had made an error with the direction of one of mine that I will have to fix.
I would change a few of the description words of the dependency arrows, specifically the ones linking the user interface
class to the deck class, the deck class to the card class, and the menu class to the menu option class. I would change
all of the words to “creates” as that describes the relationship a little better than “uses” even though it is true that
the dependent classes do use the corresponding partner, they also create said partner. With regards to the methods,
almost all are correct, and again I realized I need to correct the output type of my getSquare method on the card class
to incorporate the “free” space. I would make one change, changing the type of the show method of the menu class to be a
void function, as it doesn’t necessarily return a value, rather it prints output to the screen. All in all, the UML
diagram was a great first draft, and possessed exceptional quality. Great job Stockton!