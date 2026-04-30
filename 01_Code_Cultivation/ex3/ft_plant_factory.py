#!/usr/bin/env python3

"""Filename : ft_plant_factory.py

Date: 2026-02-21
Description: This program use plant class to manage plant
instances. Introduction to tuple to initialize plant instances
in expandable maner.
"""


class Plant:
    """Class Plant
    Attributes: name, height, age
    Methods: __str__() and __repr__()
    """

    def __init__(self, name: str, start_height: float,
                 start_age: int) -> None:
        """Initialize instance's attributes"""
        self.name: str = name
        self.start_height: float = start_height
        self.start_age: int = start_age

    def __str__(self) -> str:
        """Return format str with all informations"""
        return (f"Created: {self.name.capitalize()}"
                f" ({self.start_height}cm, {self.start_age} days)")


def ft_plant_factory(data_plant: list[tuple[str, int, int]]) -> None:
    """Create a list of plants belonging to the class Plant. Take
    attributes of each objects inside the tuple list data_plant.
    Then, print the plants
    """
    plants: list[Plant] = []
    count: int = 0
    for name, start_height, start_age in data_plant:
        plants.append(Plant(name, start_height, start_age))
        count += 1
    for plant in plants:
        print(plant)
    print(f"\nTotal plants created : {count}")


def ft_plant_data() -> list[tuple[str, int, int]]:
    """Create a tuple list data_plant"""
    data_plant: list[tuple[str, int, int]] = [
        ("rose", 25, 30),
        ("oak", 200, 365),
        ("catus", 5, 90),
        ("sunflower", 80, 45),
        ("fern", 15, 120)
    ]
    return data_plant


def main() -> None:
    """Entry point of the program"""
    data_plant: list[tuple[str, int, int]] = ft_plant_data()
    print("=== Plant Factory Output ===")
    ft_plant_factory(data_plant)


if __name__ == "__main__":
    main()
