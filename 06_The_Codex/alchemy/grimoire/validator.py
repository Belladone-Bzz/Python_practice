#!/usr/bin/env python3

"""Filename : validator.py

Date: 2026-04-01
Description: This module contains validate_ingredients function.
"""


def validate_ingredients(ingredients: str) -> str:
    """Function to check if ingredients are valid"""
    list_ingredients: list[str] = ingredients.split(" ")
    valid_ingredients: list[str] = ["fire", "water", "earth", "air"]
    if all(ingredients in valid_ingredients for ingredients
            in list_ingredients):
        return (f"{ingredients} - VALID")
    else:
        return (f"{ingredients} - INVALID")
