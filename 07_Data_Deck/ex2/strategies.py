#!/usr/bin/env python3

"""Filename : strategies.py

Date: 2026-04-13
Description: Module with class for different combat strategies.
"""
from abc import ABC, abstractmethod
from typing import Any
from ex0.creature_factory import Creature


class BattleStrategy(ABC):
    """Abstract class BattleStrategy inheriting for ABC.
    Abstract method: act() and is_valid().
    """
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Abstract method to check if a creature is suitable
        for the strategy. Return a bool.
        """
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Abstract method called by tournament script"""
        pass


class NormalStrategy(BattleStrategy):
    """NormalStrategy class inheriting from BattleStrategy."""
    def is_valid(self, creature: Creature) -> bool:
        """Overridden method. Any creature is suitable for normal strategy."""
        if isinstance(creature, Creature):
            return True
        else:
            return False

    def act(self, creature: Creature) -> None:
        """Overridden method to do the strategy if creature is suitable"""
        if self.is_valid(creature) is True:
            print(creature.attack())
        else:
            raise AttributeError(f"Invalid Creature '{creature.name}' for this"
                                 " normal strategy")


class AggressiveStrategy(BattleStrategy):
    """AggressiveStrategy class inheriting from BattleStrategy."""
    def is_valid(self, creature: Any) -> bool:
        """Overridden method. Any creature is suitable for normal strategy."""
        if hasattr(creature, "transform") and hasattr(creature, "revert"):
            return True
        else:
            return False

    def act(self, creature: Any) -> None:
        """Overridden method to do the strategy if creature is suitable"""
        if self.is_valid(creature) is True:
            print(creature.transform())
            print(creature.revert())
            print(creature.attack())
        else:
            raise AttributeError(f"Invalid Creature '{creature.name}' for this"
                                 " aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    """Concrete class inheriting from BattleStrategy."""
    def is_valid(self, creature: Any) -> bool:
        """Overridden method. Any creature is suitable for normal strategy."""
        if hasattr(creature, "heal"):
            return True
        else:
            return False

    def act(self, creature: Any) -> None:
        """Overridden method to do the strategy if creature is suitable"""
        if self.is_valid(creature) is True:
            print(creature.attack())
            print(creature.heal("itself"))
        else:
            raise AttributeError(f"Invalid Creature '{creature.name}' for this"
                                 " defensive strategy")
