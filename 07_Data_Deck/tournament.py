#!/usr/bin/env python3

"""Filename : tournament.py

Date: 2026-04-13
Description: This simulate battle with multiples strategies.
"""
from ex0 import CreatureFactory, AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy, \
    DefensiveStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    """Function to simulate battle between
    tuple[creatures(from creature facory-strategy]
    """
    nb_opponents: int = len(opponents)
    print("*** Tournament ***")
    if nb_opponents < 2:
        print("Tournament needs at least 2 opponents")
        return
    print(f"{nb_opponents} opponents involved\n")
    index_1: int = 0
    index_2: int = 0
    for index_1 in range(nb_opponents):
        for index_2 in range(index_1 + 1, nb_opponents):
            factory_a, strat_a = opponents[index_1]
            factory_b, strat_b = opponents[index_2]
            factory_a.create_base()
            factory_b.create_base()
            creature_a = factory_a.basecreatures[-1]
            creature_b = factory_b.basecreatures[-1]
            print("* Battle *")
            print(creature_a.describe())
            print("vs.")
            print(creature_b.describe())
            print("now fights!")
            try:
                strat_a.act(creature_a)
                strat_b.act(creature_b)
            except AttributeError as error:
                print("Battle error, aborting tournament: ", error)
                return
            print()


def main() -> None:
    """Entry point of the program"""
    normal_factory1: AquaFactory = AquaFactory()
    normal_factory2: FlameFactory = FlameFactory()
    healing_factory: HealingCreatureFactory = HealingCreatureFactory()
    transform_factory: TransformCreatureFactory = TransformCreatureFactory()

    normal_strat: NormalStrategy = NormalStrategy()
    aggressive_strat: AggressiveStrategy = AggressiveStrategy()
    defensive_strat: DefensiveStrategy = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    opponents_1: list[tuple[CreatureFactory, BattleStrategy]] = [
        (normal_factory2, normal_strat),
        (healing_factory, defensive_strat)]
    battle(opponents_1)

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents_2: list[tuple[CreatureFactory, BattleStrategy]] = [
        (normal_factory2, aggressive_strat),
        (healing_factory, defensive_strat)]
    battle(opponents_2)

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents_3: list[tuple[CreatureFactory, BattleStrategy]] = [
        (normal_factory1, normal_strat),
        (healing_factory, defensive_strat),
        (transform_factory, aggressive_strat)]
    battle(opponents_3)


if __name__ == "__main__":
    main()
