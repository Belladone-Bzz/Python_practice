#!/usr/bin/env python3

"""Filename : ft_first_exception.py

Date: 2026-03-01
Description: This program check error for input data informations
"""


def check_temperature(temp_str: str) -> None:
    """Function to checks input for data validation"""
    print(f"Testing temperature : {temp_str}")
    try:
        temp_int: int = int(temp_str)
        if temp_int < 0:
            print(f"Error: {temp_int}°C is too cold for plants (min 0°C)\n")
        elif temp_int > 40:
            print(f"Error: {temp_int}°C is too hot for plants (min 40°C)\n")
        else:
            print(f"Temperature {temp_int}°C is perfect for plants!\n")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def check_input_temperature() -> None:
    """Function to test with a temperature given by the user"""
    temp_str: str = str(input("Enter a temperature: "))
    check_temperature(temp_str)


def main() -> None:
    """Entry point of the program"""
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    check_input_temperature()
    print("All tests completed - program didn’t crash!")


if __name__ == "__main__":
    main()
