#!/usr/bin/env python3

"""Filename : capacitor.py

Date: 2026-04-13
Description: This code import CreatureFactories from ex0 and
HealingCreatureFactory and TransformCreatureFactory from ex1. It tests ex1
package's factories.
"""
from ex0 import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def testing_factory(factory: CreatureFactory) -> None:
    """Function to test healing and transform creature factory from ex1
    package
    """
    factory.create_base()
    factory.create_evolved()
    for creature in factory.basecreatures:
        print(creature.describe())
        print(creature.attack())
        if isinstance(factory, HealingCreatureFactory):
            print(creature.heal("itself"))
        elif isinstance(factory, TransformCreatureFactory):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
    print("evolved:")
    for creature in factory.advancedcreatures:
        print(creature.describe())
        print(creature.attack())
        if isinstance(factory, HealingCreatureFactory):
            print(creature.heal("itself"))
        elif isinstance(factory, TransformCreatureFactory):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


def main() -> None:
    """Entry point of the program"""
    print("Testing Creature with healing capability base:")
    healing_factory: HealingCreatureFactory = HealingCreatureFactory()
    testing_factory(healing_factory)
    print("\nTesting Creature with transform capability base:")
    transform_factory: TransformCreatureFactory = TransformCreatureFactory()
    testing_factory(transform_factory)


if __name__ == "__main__":
    main()
