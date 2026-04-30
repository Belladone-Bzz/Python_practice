#!/usr/bin/env python3

"""Filename : ft_different_errors.py

Date: 2026-03-01
Description: This program check different error and catch them with
Try/Except block.
"""


def test_error_types() -> None:
    """Function to catch different common errors"""
    try:
        print("\nTesting ValueError...")
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    try:
        print("\nTesting ZeroDivisionError...")
        garden_operations("zero_div")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    try:
        print("\nTesting FileNotFoundError...")
        garden_operations("open_file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    try:
        print("\nTesting KeyError...")
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    try:
        print("\nTesting multiple errors together...")
        garden_operations("all")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


def garden_operations(test: str) -> None:
    """Function to test possible errors"""
    if test == "value" or test == "all":
        int("abc")
    elif test == "zero_div" or test == "all":
        number: int = 12
        number / 0
    elif test == "open_file" or test == "all":
        open("missing.txt")
    elif test == "key" or test == "all":
        dictionary: dict[str, int] = {}
        dictionary["missing_plant"]


def main() -> None:
    """Entry point of the program"""
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!\n")


if __name__ == "__main__":
    main()
