#!/usr/bin/env python3

"""Filename : functools_artifacts.py

Date: 2026-05-05
Description: This program uses functools module for reduce, wraps, partial and
more to store powerful functional programming tools.
"""
from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """Function to modify spell power."""
    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if not spells:
        return 0
    if operation not in operations:
        raise ValueError(f"Unknown operation: '{operation}'")
    result: int = reduce(operations[operation], spells)
    return result


def base_enchantment(power: int, element: str, target: str) -> str:
    """Function to cast a base enchantment spell on a target."""
    return f"{element} spell hits {target} for {power} HP"


def partial_enchanter(
        base_enchantment: Callable) -> dict[str, Callable]:
    """Function to create 3 specialized versions of base_enchantment with
    partial.
    """
    fire_enchant = partial(base_enchantment, power=50, element="Fire")
    water_enchant = partial(base_enchantment, power=50, element="Water")
    darkness_enchant = partial(base_enchantment, power=50, element="Darkness")
    return {
        "fire": fire_enchant,
        "water": water_enchant,
        "darkness": darkness_enchant
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Function to calculate fibonacci and memoized it."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    """Function to create a spell system using dispatch."""
    @singledispatch
    def spell_system(spell: Any) -> str:
        return "Unknown spell type"

    @spell_system.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @spell_system.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @spell_system.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"
    return spell_system


def main() -> None:
    """Entry point of the program."""
    print("\nTesting spell reducer...")
    print("=" * 40)
    spells = [10, 30, 40, 20]
    try:
        print(f"Sum: {spell_reducer(spells, "add")}")
        print(f"Product: {spell_reducer(spells, "multiply")}")
        print(f"Max: {spell_reducer(spells, "max")}")
        print(f"Max: {spell_reducer(spells, "min")}")
        print(f"Max: {spell_reducer(spells, "invalid")}")
    except ValueError as error:
        print(error)
    print("\nTesting partial enchanter...")
    print("=" * 40)
    enchants = partial_enchanter(base_enchantment)
    print(enchants["fire"](target="Yannou"))
    print(enchants["water"](target="Jolyne"))
    print(enchants["darkness"](target="Marine"))
    print("\nTesting memoized fibonacci...")
    print("=" * 40)
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")
    print("\nTesting spell dispatcher...")
    print("=" * 40)
    spell_system = spell_dispatcher()
    print(spell_system(42))
    print(spell_system("fireball"))
    print(spell_system(["fireball", "firewall", "heal", "storm"]))
    print(spell_system({"location": 42}))


if __name__ == "__main__":
    main()
