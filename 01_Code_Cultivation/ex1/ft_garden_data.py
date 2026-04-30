#!/usr/bin/env python3

"""Filename : ft_garden_data.py

Date: 2026-02-20
Description: This program use plant class to manage plant
instances. Then displays plants informations.
"""


class Plant:
    """Class Plant
    Attributes: name, height, age
    Methods: __str__() and __repr__()
    """
    def __init__(self, name: str, height: int,
                 age: int) -> None:
        """Initialize instance's attributes"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def __str__(self) -> str:
        """Return format str with all informations"""
        return (f"{self.name.capitalize()}: {self.height}cm,"
                f" {self.age} days old")


def ft_garden_data() -> None:
    """Function to initialize plant instances in plant class"""
    rose: Plant = Plant("rose", 25, 30)
    sunflower: Plant = Plant("sunflower", 80, 45)
    cactus: Plant = Plant("cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(rose)
    print(sunflower)
    print(cactus)


if __name__ == "__main__":
    ft_garden_data()
