#!/usr/bin/env python3

"""Filename : decorator_mastery.py

Date: 2026-05-06
Description: This program creates decorators that can enhance any spells or
methods.
"""
from functools import wraps
from collections.abc import Callable
from typing import Any
import time
import random


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures function execution time."""
    @wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f"Spell completed in {end:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator that validates power lever to cast a spell."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: tuple[object], **kwargs: dict[str, object]) -> Any:
            power = int(str(kwargs.get(
                "power",
                args[1] if len(args) > 2 else args[0] if args else 0)))
            if power < min_power:
                return "Insufficient power for this spell"
            return func(power, *args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator that retries failed spells."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: tuple[object], **kwargs: dict[str, object]) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print("Spell failed, retrying..."
                              f" (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """Class Mageguild to use staticmethod and decorated instance methods."""
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Method to validate mage name. Valid if >= 3 chars and letters/spaces
        only.
        """
        if len(name) >= 3 and name.replace(" ", "").isalpha():
            return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        """Method with power validator decorator."""
        return f"Successfully cast {spell_name} ({power} power)"


@spell_timer
def fireball() -> str:
    """Function to cast a fireball with the spell-timer decorator."""
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def random_spell() -> str:
    """A spell that randomly succeeds or fails."""
    if random.random() < 0.7:
        raise RuntimeError("Spell failed!")
    return "Spell succeeded!"


def main() -> None:
    """Entry point of the program."""
    print("\nTesting spell timer...")
    print("=" * 40)
    print(f"Result: {fireball()}")
    print("\nTesting retrying spell...")
    print("=" * 40)
    print(random_spell())
    print("\nTesting MageGuild...")
    print("=" * 40)
    mage = MageGuild
    print(mage.validate_mage_name("Yannou le Dark"))
    print(mage.validate_mage_name("Ab"))
    print(mage.cast_spell(power=15, spell_name="Lightning"))
    print(mage.cast_spell(9, "fireball"))


if __name__ == "__main__":
    main()
