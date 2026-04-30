#!/usr/bin/env python3

"""Filename : ft_sacred_scroll.py

Date: 2026-03-30
Description: Module at the root of the repository. Import alchemy and test
function by direct access to module element.py or through package.
"""
import alchemy


def main() -> None:
    """Entry point of the program"""
    print("\n=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print("alchemy.elements.create_fire(): ", alchemy.elements.create_fire())
    print("alchemy.elements.create_water(): ", alchemy.elements.create_water())
    print("alchemy.elements.create_earth(): ", alchemy.elements.create_earth())
    print("alchemy.elements.create_air(): ", alchemy.elements.create_air())
    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print("alchemy.create_fire(): ", alchemy.create_fire())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_water(): ", alchemy.create_water())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_earth(): ", alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_air(): ", alchemy.create_air())
    except AttributeError:
        print("AttributeError - not exposed")
    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
