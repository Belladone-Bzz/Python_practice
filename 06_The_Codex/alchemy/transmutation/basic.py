#!/usr/bin/env python3

"""Filename : basic.py

Date: 2026-03-30
Description: This module contains lead_to_gold() and stone_to_gem() functions.
It uses absolute import to use create_fire and create_earth functions.
"""
from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Function to transmute to gold"""
    return (f"Lead transmuted to gold using {create_fire()}")


def stone_to_gem() -> str:
    """Function to transmute to gem"""
    return (f"Stone transmuted to gem using {create_earth()}")
