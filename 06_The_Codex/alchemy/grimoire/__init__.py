#!/usr/bin/env python3

"""Filename : __init__.py

Date: 2026-03-30
Description: Define a package's public API by importing
record_spell and validate_ingredients
"""
from .validator import validate_ingredients
__all__ = ["validate_ingredients"]
