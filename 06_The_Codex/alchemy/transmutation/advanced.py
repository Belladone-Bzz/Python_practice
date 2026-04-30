#!/usr/bin/env python3

"""Filename : advanced.py

Date: 2026-03-30
Description: This module contains philosopher_stone() and elixir_of_life().
It uses relative import to use lead_to_gold() and healing_potion() functions.
"""
from .basic import lead_to_gold
from ..potions import healing_potion


def philosopher_stone() -> str:
    """Function to create a pholosopher's stone"""
    return (f"Philosopher's stone created using {lead_to_gold()} "
            f"and {healing_potion()}")


def elixir_of_life() -> str:
    """Function to create an elixir of life"""
    return ("Elixir of life: eternal youth achieved!")
