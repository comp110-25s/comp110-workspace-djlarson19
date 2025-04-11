"""File to define Bear class."""

__author__: str = "730667045"


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        """Initialize bears age and hunger to be 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Bear age increases by one for each day that passes."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Bear hunger score increases by the number of fish it eats."""
        self.hunger_score += num_fish
        return None
