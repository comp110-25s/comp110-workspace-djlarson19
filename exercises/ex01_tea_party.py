"""Tea Party Planner"""

__author__: str = "730667045"


def main_planner(guests: int) -> None:
    """Plans the tea bags, treats, and cost of a tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed based on number of people"""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed based on number of tea bags"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of the party based on treats and tea"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
