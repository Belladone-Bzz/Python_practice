#!/usr/bin/env python3

"""Filename : ft_circular_curse.py

Date: 2026-03-30
Description: Module at the root of the repository. Avoid circular loop
from import.
"""
from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


def main() -> None:
    """Entry point of the program"""
    print("\n=== Circular Curse Breaking ===")
    print("\nTesting ingredient validation:")
    print(f"validate_ingredients(\"fire air\"): "
          f"{validate_ingredients("fire air")}")
    print(f"validate_ingredients(\"dragon scales\"): "
          f"{validate_ingredients("dragon scales")}")
    print("\nTesting spell recording with validation:")
    print("record_spell(\"Fireball\", \"fire air\"): "
          f"{record_spell("Fireball", "fire air")}")
    print("record_spell(\"Dark Magic\", \"shadow\"): "
          f"{record_spell("Dark Magic", "shadow")}")
    print("\nTesting late import technique:")
    print("record_spell(\"Lightning\", \"air\"): "
          f"{record_spell("Lightning", "air")}")
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
