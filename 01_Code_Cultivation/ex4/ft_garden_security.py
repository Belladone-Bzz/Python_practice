#!/usr/bin/env python3

"""Filename : ft_garden_security.py

Date: 2026-02-22
Description: This program use plant class to manage plant
instances. Introduction to setter and getter to secure the
initialization of attributes of plant instances.
"""


class SecurePlant:
    """Class SecurePlant
    Attributes: name, height and age
    Methods: setter, getter, __str__(), __repr__()
    """
    def __init__(self, name: str) -> None:
        """Initialize instance's attributes"""
        self.__name: str = name
        self.__height: int | None = None
        self.__age: int | None = None

    def __str__(self) -> str:
        """Return format str with all informations"""
        return (f"Current plant: {self.__name.capitalize()}"
                f" ({self.get_height()}cm, {self.get_age()} days)")

    def get_name(self) -> str:
        """Getter for name attribute, capitalize and return it"""
        return self.__name.capitalize()

    def get_height(self) -> None | int:
        """Getter for height attribute"""
        return self.__height

    def get_age(self) -> None | int:
        """Getter for age attribute"""
        return self.__age

    def set_height(self, value: int) -> None:
        """Setter for height attribute, can't be negative"""
        if value > 0:
            self.__height = value
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print("\nInvalid operation attempted: height",
                  f"{value}cm [REJECTED]")
            print("Security: Negative height rejected\n")

    def set_age(self, value: int) -> None:
        """Setter for age attribute, can't be negative"""
        if value > 0:
            self.__age = value
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print("\nInvalid operation attempted: age",
                  f"{value} days [REJECTED]")
            print("Security: Negative age rejected\n")


def ft_garden_security() -> None:
    """Function to check the security of setter
    Send a negative value to set the height attribute
    Print the Garden datas
    """
    rose: SecurePlant = SecurePlant("rose")
    print("=== Garden Security System ===")
    print(f"Plant Created: {rose.get_name()}")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print(rose)


if __name__ == "__main__":
    ft_garden_security()
