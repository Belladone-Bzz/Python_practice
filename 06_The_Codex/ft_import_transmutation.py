#!/usr/bin/env python3

"""Filename : ft_import_transmutation.py

Date: 2026-03-30
Description: Module at the root of the repository. Import alchemy and test
function by direct access to module potion.py or through package.
"""


def method_1() -> None:
    """Method_1 needs acces to package alchemy, then to module elements.py to
    uses the function create_fire().
    We import the package alchemy and then can access to creat_fire and
    create_water of element, wich are imported in the __init__.py"""
    import alchemy
    print("Method 1 - Full Module import:")
    print("alchemy.elements.create_fire(): ", alchemy.elements.create_fire())


def method_2() -> None:
    """Method_2 uses absolute import. It imports directly the function
    create_water() from alchemy.elements
    """
    from alchemy.elements import create_fire
    print("\nMethod 2 - Specific function import:")
    print("create_fire(): ", create_fire())


def method_3() -> None:
    """Method_3 uses aliased import to import healing_potion() as heal()
    from alchemy.elements
    """
    from alchemy.potions import healing_potion as heal
    print("\nMethod 3 - Aliased import:")
    print("heal(): ", heal())


def method_4() -> None:
    """Method_4 uses multiple imports from different modules: alchemy.elements
    and alchemy.potions
    """
    from alchemy.elements import create_water, create_fire
    from alchemy.potions import strength_potion
    print("\nMethod 4 - Multiple imports:")
    print("create_water(): ", create_water())
    print("create_fire(): ", create_fire())
    print("strength_potion(): ", strength_potion())


def main() -> None:
    """Entry point of the program"""
    print("\n=== Import Transmutation Mastery ===\n")
    method_1()
    method_2()
    method_3()
    method_4()
    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    main()
