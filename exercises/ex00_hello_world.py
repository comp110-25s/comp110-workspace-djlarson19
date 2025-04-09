"""My First Exercise in COMP110!"""

__author__ = "730667045"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


greet(name="student")
if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
