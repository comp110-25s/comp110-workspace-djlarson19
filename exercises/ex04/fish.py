"""File to define Fish class."""

__author__: str = "730667045"


class Fish:
    age: int

    def __init__(self):
        """Initialize a fish's age to be 0."""
        self.age = 0
        return None

    def one_day(self):
        """Fish age increases by 1 each day."""
        self.age += 1
        return None
