class Fractal():
    def __init__(self, frac):
        raise NotImplementedError("Concrete subclass of Fractal must implement init")

    def count(self, complex):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")
