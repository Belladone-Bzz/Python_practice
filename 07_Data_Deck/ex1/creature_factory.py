#!/usr/bin/env python3

"""Filename : capabilities.py

Date: 2026-04-13
Description: Module with all classes used for creature
factory with capabilities.
"""
from .capabilities import HealCapability, TransformCapability
from ex0.creature_factory import Creature, CreatureFactory


class Sproutling(Creature, HealCapability):
    """Class Sproutling inheriting from Creature and HealCapability
    Abstract methods: attack(), heal(target)
    """
    def __init__(self) -> None:
        """Overriden initialization of name and type"""
        self.name: str = "Sproutling"
        self.type: str = "Grass"

    def attack(self) -> str:
        """Overridden method to attack"""
        return (f"{self.name} uses Vine Whip!")

    def heal(self, target: str) -> str:
        """Overridden method to heal"""
        return (f"{self.name} heals {target} for a small amount")


class Bloomelle(Creature, HealCapability):
    """Class Bloomelle inheriting from Creature and HealCapability
    Abstract methods: attack(), heal(target)
    """
    def __init__(self) -> None:
        """Overriden initialization of name and type"""
        self.name: str = "Bloomelle"
        self.type: str = "Grass/Fairy"

    def attack(self) -> str:
        """Overridden method to attack"""
        return (f"{self.name} uses Petal Dance!")

    def heal(self, target: str) -> str:
        """Overridden method to heal"""
        return (f"{self.name} heals {target} and others for a large amount")


class Shiftling(Creature, TransformCapability):
    """Class Shiftling inheriting from Creature and TransformCapability
    Abstract methode: attack(), transform(), revert()
    """
    def __init__(self) -> None:
        """Overriden initialization of name and type and initialization
        of state
        """
        self.name: str = "Shiftling"
        self.type: str = "Normal"
        TransformCapability.__init__(self)

    def attack(self) -> str:
        """Overridden method to attack"""
        if self.state is False:
            return (f"{self.name} attacks normally.")
        return (f"{self.name} performs a boosted strike!")

    def transform(self) -> str:
        """Overridden method to transform"""
        self.state = True
        return (f"{self.name} shifts into a sharper form!")

    def revert(self) -> str:
        """Overridden method to revert"""
        self.state = False
        return (f"{self.name} returns to normal.")


class Morphagon(Creature, TransformCapability):
    """Class Marphagon inheriting from Creature and TransformCapability
    Abstract methode: attack(), transform(), revert()
    """
    def __init__(self) -> None:
        """Overriden initialization of name and type and initialization
        of state
        """
        self.name: str = "Morphagon"
        self.type: str = "Normal/Dragon"
        TransformCapability.__init__(self)

    def attack(self) -> str:
        """Overridden method to attack"""
        if self.state is False:
            return (f"{self.name} attacks normally.")
        return (f"{self.name} unleashes a devasting morph strike!")

    def transform(self) -> str:
        """Overridden method to transform"""
        self.state = True
        return (f"{self.name} shifts into a dragonic battle form!")

    def revert(self) -> str:
        """Overridden method to revert"""
        self.state = False
        return (f"{self.name} stabilizes its form.")


class HealingCreatureFactory(CreatureFactory):
    """Class HealingCreatureFactory inheriting from CreatureFactory
    Abstract methods: create_base() and create_advanced()
    """
    def create_base(self) -> None:
        """Overridden method to create a basic healing creature"""
        self.basecreatures.append(Sproutling())

    def create_evolved(self) -> None:
        """Overridden method to create an evolved healing creature"""
        self.advancedcreatures.append(Bloomelle())


class TransformCreatureFactory(CreatureFactory):
    """Class TransformCreatureFactory inheriting from CreatureFactory
    Abstract methods: create_base() and create_advanced()
    """
    def create_base(self) -> None:
        """Overridden method to create a basic healing creature"""
        self.basecreatures.append(Shiftling())

    def create_evolved(self) -> None:
        """Overridden method to create an evolved healing creature"""
        self.advancedcreatures.append(Morphagon())
