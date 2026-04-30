#!/usr/bin/env python3

"""Filename : ft_plant_types.py

Date: 2026-02-22
Description: This program use plant class and Flower, Vegetable
and Tree class that inherit from Plant class. These subclasses
has specifics attributes and methods. The program display all
types of Plant's informations.
"""


class Plant:
    """Class Plant
    Attributes: name, height and age
    Methods: __str__(), __repr__()
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize instance's attributes"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def __str__(self) -> str:
        """Return format str with all informations"""
        return (f"{self.name.capitalize()} ({self.__class__.__name__}):"
                f" {self.height}cm, {self.age} days")


class Flower(Plant):
    """Class Flower, inherits from Plant
    Attributes: name, height, age, color
    Methods: bloom()
    """

    def __init__(self, name: str, height: int,
                 age: int, color: str) -> None:
        """Initialize instance's attributes"""
        super().__init__(name, height, age)
        self.color: str = color

    def __str__(self) -> str:
        """Return format str with all informations"""
        return (super().__str__() + f", {self.color} color")

    def bloom(self) -> None:
        """Function bloom() specific to Flower child class"""
        if self.age > 15:
            print(f"{self.name.capitalize()} is blooming beautifully !")
        else:
            print(f"{self.name.capitalize()} is too young to bloom !")


class Tree(Plant):
    """Class Tree, inherits from Plant
    Attributes: name, height, age, trunk_diameter
    Methods: produce_shade()
    """

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialize instance's attributes"""
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def __str__(self) -> str:
        """Return format str with all informations"""
        return (super().__str__() + f", {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        """Calculate and print shade provided"""
        ratio: float = 1.56
        print(f"{self.name.capitalize()} provides",
              f"{int(self.trunk_diameter * ratio)}",
              "square meters of shade")


class Vegetable(Plant):
    """Class Vegetable, inherits from Plant
    Attributes: name, height, age, season, nut_value
    Methods: nutritional_intake()
    """

    def __init__(self, name: str, height: int, age: int, season: str,
                 nut_value: str) -> None:
        """Initialize instance's attributes"""
        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutritional_value: str = nut_value

    def __str__(self) -> str:
        """Return format str with all informations"""
        return (super().__str__() + f", {self.harvest_season} harvest")

    def nutritional_intake(self) -> None:
        """Print nutriment provided"""
        print(f"{self.name.capitalize()} is rich in {self.nutritional_value}")


def ft_print_plants(flowers: list[Flower], trees: list[Tree],
                    vegetables: list[Vegetable]) -> None:
    """Print all objects from all class and call their method"""
    for flower in flowers:
        print(flower)
        flower.bloom()
        print()
    for tree in trees:
        print(tree)
        tree.produce_shade()
        print()
    for vegetable in vegetables:
        print(vegetable)
        vegetable.nutritional_intake()
        print()


def ft_plants_init() -> None:
    """Create a plants_list with their attributes"""
    flowers_list: list[Flower] = [
        Flower("rose", 25, 30, "red"),
        Flower("tulip", 18, 13, "yellow"),
    ]
    trees_list: list[Tree] = [
        Tree("oak", 500, 1825, 50),
        Tree("willow", 1500, 425, 60),
    ]
    vegetables_list: list[Vegetable] = [
        Vegetable("tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("lettuce", 25, 12, "winter", "fibers")
    ]
    ft_print_plants(flowers_list, trees_list, vegetables_list)


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    ft_plants_init()
