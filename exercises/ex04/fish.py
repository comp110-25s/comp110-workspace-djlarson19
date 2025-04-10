"""File to define Fish class."""

__author__ = "730667045"


class Fish:
    age: int

    def __init__(self):
        """initialize a fish's age to be 0"""
        self.age = 0
        return None

    def one_day(self):
        """fish age increases by 1 each day"""
        self.age += 1
        return None
