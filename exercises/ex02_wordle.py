"""Wordle"""

__author__: str = "730667045"


def contains_char(answer: str, character: str) -> bool:
    """Checks to see if a letter is contained in the answer"""
    assert (
        len(character) == 1
    ), f"len('{character}') is not 1"  # checks to see if the length of the character guessed is 1
    i: int = 0  # initialize the index for character at 0
    while i < len(answer):  # loop while i is less that the length of the answer
        if answer[i] == character:
            return True
        i += 1  # add one to check every letter

    return False


def emojified(guess: str, secret: str) -> str:
    """Uses contains_char to check the letters from the worlde guess and return a string of emojis representing the guess."""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    response: str = ""
    i: int = 0
    while i < len(secret):  # Continue loop through all letters in the guess
        if guess[i] == secret[i]:  # Right letter, right spot
            response += GREEN_BOX
        elif contains_char(secret, guess[i]):  # Right letter wrong spot
            response += YELLOW_BOX
        else:
            response += WHITE_BOX
        i += 1  # adds one to check every letter
    return response


def input_guess(expected_length: int) -> str:
    guess: str = input(
        f"Enter a {expected_length} character word:"
    )  # prompts to write an X length word
    while (
        len(guess) != expected_length
    ):  # if the input isn't the same length as the expected_length chosen
        guess = input(f"That wasn't {expected_length} chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    TOTAL_TURNS: int = 6  # Initialize total turns as 6
    turn: int = 1  # prints turn =1 for the first turn

    while turn <= TOTAL_TURNS:  # continue until 6th turn is used
        print(f"=== Turn {turn}/{TOTAL_TURNS} ===")  # Print the current turn/6

        guess: str = input_guess(len(secret))  # input guess
        result: str = emojified(guess, secret)  # runs emojified to test the guess
        print(result)  # prints result and continues in loop if wrong

        if guess == secret:
            print(f"You won in {turn}/6 turns!")  # Printed if correct
            return
        turn += 1  # Add to the turn variable
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
