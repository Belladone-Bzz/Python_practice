#!/usr/bin/env python3

"""Filename : ft_garden_intro.py

Date: 2026-02-20
Description: This program displays garden info.
"""


def ft_garden_intro() -> None:
    """Function to display garden info"""
    plant: str = "Rose"
    height: int = 25
    age: int = 30
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant.capitalize()}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Progam ===")


if __name__ == "__main__":
    ft_garden_intro()
