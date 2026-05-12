#!/usr/bin/env python3

"""Filename : scope_mysteries.py

Date: 2026-05-04
Description: This program uses lexical scoping to "remember" variables from
their creation environment. It creates then persistant magical effects.
"""
from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    """Function to create a counting closure."""
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Function to create a power accumulator"""
    power = initial_power

    def accumulation(additional: int) -> int:
        nonlocal power
        power += additional
        return power
    return accumulation


def enchantment_factory(enchantment_type: str) -> Callable:
    """Function to apply an enchantment type."""
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    """Function to create a memory system management."""
    storage: dict[str, Callable] = {}

    def store(key: str, value: Any) -> None:
        storage[key] = value

    def recall(key: str) -> Any:
        return storage.get(key, "Memory not found")
    return {"store": store, "recall": recall}


def main() -> None:
    """Entry point of the program"""
    print("\nTesting mage counter...")
    print("=" * 40)
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print(f"counter_a call 3: {counter_a()}")
    print(f"counter_b call 2: {counter_b()}")
    print("=" * 40)
    print("\nTesting spell accumulator...")
    print("=" * 40)
    base_100 = spell_accumulator(100)
    base_200 = spell_accumulator(200)
    print(f"Base 100, add 20: {base_100(20)}")
    print(f"Base 100, add 30: {base_100(30)}")
    print(f"Base 200, add 60: {base_200(60)}")
    print(f"Base 100, add 30: {base_100(30)}")
    print(f"Base 200, add 40: {base_200(40)}")
    print("=" * 40)
    print("\nTesting enchantment factory...")
    print("=" * 40)
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    sacred = enchantment_factory("Sacred")
    print(flaming("Sword"))
    print(frozen("Shield"))
    print(sacred("Helm"))
    print("=" * 40)
    print("\nTesting memory vault...")
    print("=" * 40)
    memory = memory_vault()
    memory["store"]("secret", "Marseille")
    print("Store 'secret' = Marseille")
    memory["store"]("year", 1994)
    print("Store 'year' = 1994")
    print(f"Recall 'secret': {memory['recall']('secret')}")
    print(f"Recall 'year': {memory['recall']('year')}")
    print(f"Recall 'unknown': {memory['recall']('unknown')}")
    print("=" * 40)


if __name__ == "__main__":
    main()
