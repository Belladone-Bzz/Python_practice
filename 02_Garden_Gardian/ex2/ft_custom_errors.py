#!/usr/bin/env python3

"""Filename : ft_custom_errors.py

Date: 2026-03-01
Description: This program uses custom error inherithibg from
Exception class and catches them with Try/Except block.
"""


class GardenError(Exception):
    """Garden Error class that inherit from Exception"""
    pass


class PlantError(GardenError):
    """PlantError class that inherit from GardenError"""
    def __init__(self, name: str) -> None:
        """Initialize instance's attributes"""
        self.name: str = name

    def __str__(self) -> str:
        """str representation of object"""
        return (f"The {self.name} plant is wilting !")


class WaterError(GardenError):
    """WaterError class that inherit from GardenError"""
    def __str__(self) -> str:
        """str representation of object"""
        return ("Not enough water in the tank!")


class Plant:
    """Plant class
    Attributes: name, water_level
    """
    def __init__(self, name: str, water_level: int) -> None:
        """Initialize instance's attributes"""
        self.name: str = name
        self.water_level: int = water_level


def check_plant(plant: Plant) -> None:
    """Function to check error plant"""
    if plant.water_level > 3:
        print("Plant is healthy")
    else:
        raise PlantError(plant.name)


def check_water_tank(water_tank: int) -> None:
    """Function to check water tank"""
    if water_tank > 4:
        print("Enought water in the tank")
    else:
        raise WaterError(water_tank)


def check_errors(plant: Plant, water_tank: int) -> None:
    """Function to initiate error checking and catch errors"""
    print("\nTesting PlantError...")
    try:
        check_plant(plant)
    except PlantError as error:
        print("Caught PlantError: ", error)
    print("\nTesting WaterError...")
    try:
        check_water_tank(water_tank)
    except WaterError as error:
        print("Caught WaterError: ", error)
    print("\nTesting catching all garden errors...")
    try:
        check_plant(plant)
    except GardenError as error:
        print("Caught a garden error: ", error)
    try:
        check_water_tank(water_tank)
    except GardenError as error:
        print("Caught a garden error: ", error)


def main() -> None:
    """Entry point of the program"""
    plant: Plant = Plant("tomato", 1)
    water_tank: int = 0
    print("=== Custom Garden Errors Demo ===")
    check_errors(plant, water_tank)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
