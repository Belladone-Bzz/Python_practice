#!/usr/bin/env python3

"""Filename : battle.py

Date: 2026-04-11
Description: This code import CreatureFactories from ex0 and
tests these factories and simulate a battle between base creatures
"""
from ex0 import CreatureFactory, FlameFactory, AquaFactory


def testing_factory(factory: CreatureFactory) -> None:
    """Funcrion to test creature factory inside ex0 package"""
    print("Testing factory")
    try:
        factory.create_base()
        factory.create_evolved()
        for creature in factory.basecreatures:
            print(creature.describe())
            print(creature.attack())
        for creature in factory.advancedcreatures:
            print(creature.describe())
            print(creature.attack())
    except Exception:
        print("An error occured.")


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    """Function to simulate a battle between base creatures"""
    print("Testing battle")
    for creature1 in factory1.basecreatures:
        print(creature1.describe())
        print("vs.")
        for creature2 in factory2.basecreatures:
            print(creature2.describe())
        print("fight!")
        print(creature1.attack())
        print(creature2.attack())


def main() -> None:
    """Entry point of the program"""
    flame_factory: FlameFactory = FlameFactory()
    aqua_factory: AquaFactory = AquaFactory()
    testing_factory(flame_factory)
    print()
    testing_factory(aqua_factory)
    print()
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
