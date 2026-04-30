#!/usr/bin/env python3

"""Filename : __init__.py

Date: 2026-03-30
Description: Define a package's public API by importing
create_fire and create_water from elements.py
"""
__version__ = "1.0.0"
__author__ = "Master Pythonicus"
from .elements import create_fire, create_water
__all__ = ["create_fire", "create_water"]
