#!/usr/bin/env python3

"""Filename : spellbook.py

Date: 2026-04-01
Description: This module contains record_spell function.
"""


def record_spell(spell_name: str, ingredients: str) -> str:
    """Function to check validity of a spell"""
    from .validator import validate_ingredients
    check: str = validate_ingredients(ingredients)
    if check == f"{ingredients} - INVALID":
        return (f"Spell rejected: {spell_name} {check}")
    else:
        return (f"Spell recorded: {spell_name} {check}")
