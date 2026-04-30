#!/usr/bin/env python3

"""Filename : ft_raise_errors.py

Date: 2026-03-01
Description: This program check errors and raise them and
Except block catch them.
"""


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """Function to check errors"""
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!\n")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level}"
                         f" is too high (max 10)\n")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level}"
                         f" is too low (min 1)\n")
    elif sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         f" is too low (min 2)\n")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         f" is too high (max 12)\n")
    else:
        print(f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks() -> None:
    """Function to check plant characterisctics"""
    plants: list[tuple[str, int, int]] = [("tomato", 5, 8), ("", 5, 8),
                                          ("tomato", 15, 8), ("tomato", 5, 0)]
    test: list[str] = [("good values"), ("empty plant name"),
                                        ("bad water level"),
                                        ("bad sunlight hours")]
    index: int = 0
    for plant in plants:
        print(f"Testing {test[index]}...")
        index += 1
        try:
            check_plant_health(plant[0], plant[1], plant[2])
        except ValueError as error:
            print(error)


def main() -> None:
    """Entry point of the program"""
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
    print("All error raising tests completed!\n")


if __name__ == "__main__":
    main()
