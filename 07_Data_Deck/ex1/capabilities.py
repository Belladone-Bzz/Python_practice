#!/usr/bin/env python3

"""Filename : capabilities.py

Date: 2026-04-13
Description: Module with all classes used for creating healing and
transform capabilities.
"""
from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Class HealCapability inheriting for ABC.
    Abstract method: heal(target).
    """
    @abstractmethod
    def heal(self, target: str) -> str:
        """Abstract method to heal a target."""
        pass


class TransformCapability(ABC):
    """Class TransformCapability inheriting for ABC.
    Abstract method: transform() and revert().
    """
    def __init__(self) -> None:
        """Initialize instance's attribute state."""
        self.state: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Abstract method to transform a creature and its attack."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Abstract method for restoring a transformed creature to its
        normal state.
        """
        pass
