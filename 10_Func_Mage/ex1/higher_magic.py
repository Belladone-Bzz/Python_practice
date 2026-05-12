#!/usr/bin/env python3

"""Filename : higher_magic.py

Date: 2026-05-04
Description: This program create a spell-crafting system where functions can
modify, combine, and enhance other functions. This is done using callable().
"""
from collections.abc import Callable
from typing import Any


def heal(target: str, power: int) -> str:
    """Function to use heal."""
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    """Function to use fireball."""
    return f"Fireball hit {target} for {power} HP"


def sacred_wall(target: str, power: int) -> str:
    """Function to use sacred_wall."""
    return f"Sacred Wall protect {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Function to combine two spells."""
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Function to amplify the power of a spell."""
    def amplified(target: str, power: int) -> Any:
        return (base_spell(target, (power * multiplier)))
    return amplified


def is_powerfull(target: str, power: int) -> bool:
    """Condition to cast a spell for conditional_caster."""
    if power >= 10:
        return True
    return False


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Function to cast a spell if condition is true."""
    def conditional_spell(target: str, power: int) -> Any:
        if condition(target, power) is True:
            return (spell(target, power))
        else:
            return ("Spell fizzled")
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    """Function to cast a list of spells."""
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def main() -> None:
    """Entry point of the program"""
    print("\nTesting spell combiner...")
    combined = spell_combiner(heal, fireball)
    result = combined("Dark Yannou", 15)
    print(f"Combined spell result: {result[0]}, {result[1]}")
    print("\nTesting spell amplifier...")
    amplified = power_amplifier(heal, 10)
    result = amplified("Dark Yannou", 15)
    print(f"Spell power amplified: {result}")
    print("\nTesting conditional caster (power need to be >= 10)")
    cast = conditional_caster(is_powerfull, fireball)
    print(f"With a power of 9: {cast("Dark Yannou", 9)}")
    cast = conditional_caster(is_powerfull, fireball)
    print(f"With a power of 15: {cast("Dark Yannou", 15)}")
    print("\nTesting spell sequence...")
    sequence = spell_sequence([heal, fireball, sacred_wall])
    result = sequence("Dark Yannou", 15)
    for spell in result:
        print(spell)


if __name__ == "__main__":
    main()
