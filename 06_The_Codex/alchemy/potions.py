#!/usr/bin/env python3

"""Filename : potions.py

Date: 2026-03-30
Description: Module to create and return potion.
"""


def healing_potion() -> str:
    """Function to create a healing potion"""
    from .elements import create_fire, create_water
    return (f"Healing potion brewed with {create_fire()} and {create_water()}")


def strength_potion() -> str:
    """Function to create a strength potion"""
    from .elements import create_fire, create_earth
    return (f"Strength potion brewed with {create_earth()} and "
            f"{create_fire()}")


def invisibility_potion() -> str:
    """Function to create an invisibility potion"""
    from .elements import create_air, create_water
    return (f"Invisibility potion brewed with {create_air()}"
            f" and {create_water()}")


def wisdom_potion() -> str:
    """Function to create a wisdom potion"""
    from .elements import create_fire, create_water, create_earth, create_air
    return (f"Wisdom potion brewed with all elements: {create_fire()}, "
            f"{create_water()}, {create_earth()} and {create_air()}")
