#!/usr/bin/env python3

"""Filename : creature_factory.py

Date: 2026-04-11
Description: Module with all classes used for creature
factory.
"""
from abc import ABC, abstractmethod


class Creature(ABC):
    """Class Creature inheriting for ABC
    Attributes: name, type
    Abstract method: attack()
    Concrete method: describe()
    """
    @abstractmethod
    def __init__(self) -> None:
        """Initialize instance's attributes name and type"""
        self.name: str
        self.type: str

    @abstractmethod
    def attack(self) -> str:
        """Abstract method to make an attack"""
        pass

    def describe(self) -> str:
        """Concrete methode to display creature's attributes"""
        return (f"{self.name} is a {self.type} type Creature")


class Flameling(Creature):
    """Class Flameling inheriting from Creature
    Abstract methods: __init__() and attack()
    """
    def __init__(self) -> None:
        """Overriden initialization of name and type"""
        self.name: str = "Flameling"
        self.type: str = "Fire"

    def attack(self) -> str:
        """Overridden method to make an attack"""
        return (f"{self.name} uses Ember!")


class Pyrodon(Creature):
    """Class Pyrodon inheriting from Creature
    Abstract methods: __init__() and attack()
    """
    def __init__(self) -> None:
        """Overriden initialization of name and type"""
        self.name: str = "Pyrodon"
        self.type: str = "Fire/Flying"

    def attack(self) -> str:
        """Overridden method to make an attack"""
        return (f"{self.name} uses Flamethrower!")


class Aquabub(Creature):
    """Class Aquabub inheriting from Creature
    Abstract methods: __init__() and attack()
    """
    def __init__(self) -> None:
        """Overriden initialization of name and type"""
        self.name: str = "Aquabub"
        self.type: str = "Water"

    def attack(self) -> str:
        """Overridden method to make an attack"""
        return (f"{self.name} uses Water Gun!")


class Torragon(Creature):
    """Class Torragon inheriting from Creature
    Abstract methods: __init__() and attack()
    """
    def __init__(self) -> None:
        """Overriden initialization of name and type"""
        self.name: str = "Torragon"
        self.type: str = "Water"

    def attack(self) -> str:
        """Overridden method to make an attack"""
        return (f"{self.name} uses Hydro Pump!")


class CreatureFactory(ABC):
    """Class CreatureFactory inheriting from ABC
    Abstrac methods: create_base() and create_evolved()
    """
    def __init__(self) -> None:
        """Initialize instance's attribute list basecreatures and
        advancedcreatures"""
        self.basecreatures: list[Creature] = []
        self.advancedcreatures: list[Creature] = []

    @abstractmethod
    def create_base(self) -> None:
        """Abstract method to create a base creature"""
        pass

    @abstractmethod
    def create_evolved(self) -> None:
        """Abstract method to create an evolved creature"""
        pass


class FlameFactory(CreatureFactory):
    """Class FlameFactory inheriting from CreatureFactory
    Abstract methods: create_base() and create_evolved()
    """
    def create_base(self) -> None:
        """Overridden method to create a basic flame creature"""
        self.basecreatures.append(Flameling())

    def create_evolved(self) -> None:
        """Overridden method to create an evolved flame creature"""
        self.advancedcreatures.append(Pyrodon())


class AquaFactory(CreatureFactory):
    """Class AquaFactory inheriting from CreatureFactory
    Abstract methods: create_base() and create_advanced()
    """
    def create_base(self) -> None:
        """Overridden method to create a basic water creature"""
        self.basecreatures.append(Aquabub())

    def create_evolved(self) -> None:
        """Overridden method to create an evolved water creature"""
        self.advancedcreatures.append(Torragon())
