#!/usr/bin/env python3

"""Filename : ft_plant_growth.py

Date: 2026-02-20
Description: This program use plant class to manage plant
instances. Introduction to instance method to grow plants.
Then displays plants informations and growth.
"""


class Plant:
    """Class Plant
    Attributes: name, height, age, growth
    Methods: grow(), age(), __str__(), __repr__()
    """

    def __init__(self, name: str, starting_height: int,
                 starting_age: int, growth: int) -> None:
        """Initialize instance's attributes"""
        self.name: str = name
        self.starting_height: int = starting_height
        self.starting_age: int = starting_age
        self.growth: int = growth

    def grow(self) -> None:
        """Operation to grow the plant"""
        self.starting_height += self.growth

    def age(self) -> None:
        """Operation to age the plant"""
        self.starting_age += 1

    def __str__(self) -> str:
        """Return format str with all informations"""
        return (f"{self.name.capitalize()}: {self.starting_height}cm,"
                f" {self.starting_age} days old")


def get_info(day: int, plant: Plant) -> None:
    """Function to write info of an object"""
    print(f"=== Day {day + 1} ===")
    print(plant)
    if day > 0:
        print(f"Growth this week: +{plant.growth * day:.0f}cm\n")


def ft_plant_growth(plant: Plant, day: int) -> None:
    """Function to induce plant aging and growing"""
    if day == 0:
        get_info(day, plant)
    else:
        i = 0
        while i < day:
            plant.grow()
            plant.age()
            i += 1
        get_info(day, plant)


def main() -> None:
    """Entry point of the program"""
    rose: Plant = Plant("rose", 25, 30, 1)
    tulip: Plant = Plant("tulip", 10, 15, 2)
    ft_plant_growth(rose, 0)
    ft_plant_growth(rose, 6)
    ft_plant_growth(tulip, 0)
    ft_plant_growth(tulip, 6)


if __name__ == "__main__":
    main()
