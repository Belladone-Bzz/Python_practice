#!/usr/bin/env python3

"""Filename : ft_finally_block.py

Date: 2026-03-01
Description: This program uses custom error inherithibg from
Exception class and catches them with Try/Except block. Then
use a Finally block.
"""


class Plant_Name_Error(Exception):
    """Initialize instance's attributes"""
    def __init__(self, name: str | None) -> None:
        self.name: str | None = name

    def __str__(self) -> str:
        """str representation of object"""
        return (f"Error: Cannot water {self.name} - invalid plant!")


def water_plants(plants_list: list[str | None]) -> None:
    """Function to water plants in the list"""
    print("Opening watering system")
    try:
        for plant in plants_list:
            if test_watering_system(plant) is True:
                print(f"Watering {plant}")
            else:
                raise Plant_Name_Error(plant)
    except Plant_Name_Error as error:
        print(error)
        return
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


def test_watering_system(plant: str | None) -> bool:
    """Function to check error before watering"""
    if plant == "" or plant is None:
        return False
    else:
        return True


def plants_init() -> None:
    """Function to init list of plants and call watering system"""
    plants_list: list[str | None] = [
        ("tomato"),
        ("lettuce"),
        ("carrots")
    ]
    plants_list_invalid: list[str | None] = [
        ("tomato"),
        (None),
    ]
    print("\nTesting normal watering...")
    water_plants(plants_list)
    print("\nTesting with error...")
    water_plants(plants_list_invalid)


def main() -> None:
    """Entry point of the program"""
    print("=== Garden Watering System ===")
    plants_init()
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
