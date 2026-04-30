#!/usr/bin/env python3

"""Filename : ft_coordinate_system.py

Date: 2026-03-16
Description: This program manipulates 3D coordinates passed as input stream. It
calculates Euclidean distances between points, and demonstrates tuple
unpacking in a game coordinate system context.
"""
import math


def get_player_pos() -> tuple[float, float, float]:
    """Function to get user coordinate via input() check error and
    return a tuple of position x,y,z
    """
    inp_us: str = input("Enter new coordinates as floats in format 'x,y,z:' ")
    try:
        x, y, z = inp_us.split(",")
        coordinates: list[str] = [x, y, z]
    except Exception:
        print("Invalid syntax")
        return get_player_pos()
    try:
        for pos in coordinates:
            float(pos)
        tuple_user: tuple[float, float, float] = (float(coordinates[0]),
                                                  float(coordinates[1]),
                                                  float(coordinates[2]))
        return tuple_user

    except Exception as error:
        print(f"Error on parameter '{pos}':", error)
        return get_player_pos()


def main() -> None:
    """Entry point of the program"""
    print("=== Game Coordinate System ===\n")
    center: tuple[float, float, float] = (0.0, 0.0, 0.0)
    x1, y1, z1 = center
    print("Get a first set of coordinates")
    first_set = get_player_pos()
    x2, y2, z2 = first_set
    print(f"Got a first tuple: {first_set}")
    print(f"It includes: X={x2}, Y={y2}, Z={z2}")
    distance: float = math.sqrt((float(x2)-float(x1))**2 +
                                (float(y2)-float(y1))**2 +
                                (float(z2)-float(z1))**2)
    print(f"Distance to center: {distance:.4f}\n")
    print("Get a second set of coordinates")
    x1, y1, z1 = x2, y2, z2
    second_set = get_player_pos()
    x2, y2, z2 = second_set
    distance = math.sqrt((float(x2)-float(x1))**2 +
                         (float(y2)-float(y1))**2 +
                         (float(z2)-float(z1))**2)
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")


if __name__ == "__main__":
    main()
