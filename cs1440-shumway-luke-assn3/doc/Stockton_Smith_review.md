Luke and I each developed our UML diagrams independently from each other; as a result, the two of us seem to have come
up with slightly different solutions to solve the same problem. For example, when looking at our dependencies, I noticed
that Luke’s “NumberSet” class depends on his “Card” class, while I have my Card class depending on my NumberSet class.
Not only do Luke’s dependencies appear to follow a different pattern, but several of his dependencies are already labeled
in applicable ways; for instance, a reader can tell from Luke’s UML that a Deck object “creates” a card object, and a
Menu object “creates” a MenuOption object.

I also noticed that Luke’s UML diagram at this stage seems to already be filled out with most of his variables that are
getting passed through his methods. This is a strength to his UML and its readability, as an outside reader or developer
will be able to tell more easily what each method in the program uses to function. This is especially helpful considering
that the main objective of the UML diagram is to illustrate the functionality of the program and how each class interacts
with one other.

There are also several components of Luke’s UML that could be improved upon in the final version based on the material
covered in Friday’s lecture. These would include features such as associations (which serve to differentiate one-way
dependencies from two-way dependencies) and multiplicity constraints (which will provide numerical ranges for class
relationships, thereby improving overall readability and comprehension).