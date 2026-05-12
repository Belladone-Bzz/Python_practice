#!/usr/bin/env python3

"""Filename : lambda_spells.py

Date: 2026-05-04
Description: This program organize magical artifacts using anonymous functions.
This is done using lambda expressions.
"""


def artifact_sorter(
        artifacts: list[dict[str, str | int]]) -> list[dict[str, str | int]]:
    """This function sort magical artifacts using lambda expression."""
    print("\nTesting artifact sorter...")
    print("=" * 40)
    print("Initial artifacts:")
    for artifact in artifacts:
        print(f"{artifact["name"]} ({artifact["power"]} power)")
    sorted_artifacts = sorted(artifacts, key=lambda artifact:
                              artifact["power"], reverse=True)
    print("\nSorted artifacts:")
    for artifact in sorted_artifacts:
        print(f"{artifact["name"]} ({artifact["power"]} power)")
    print("=" * 40)
    return sorted_artifacts


def power_filter(
        mages: list[dict[str, str | int]],
        min_power: int) -> list[dict[str, str | int]]:
    """This function filter mages by power using lambda expression."""
    print("\nTesting mage filter...")
    print("=" * 40)
    print("Initial mages:")
    for caster in mages:
        print(f"{caster["name"]} ({caster["power"]} power)")
    filtered_mages: list[dict[str, str | int]] = list(filter(
        lambda mage: int(mage.get("power", 0)) >= min_power, mages))
    print("\nFiltered mages:")
    for caster in filtered_mages:
        print(f"{caster["name"]} ({caster["power"]} power)")
    print("=" * 40)
    return filtered_mages


def spell_transformer(spells: list[str]) -> list[str]:
    """This function transform spell names using lambda expression."""
    print("\nTesting spell transformer...")
    print("=" * 40)
    print("Initial spells:")
    for spell in spells:
        print(spell)
    transformed_spells = list(map(lambda spell: f"* {spell} *", spells))
    print("\nTransformed spells:")
    for spell in transformed_spells:
        print(spell)
    print("=" * 40)
    return transformed_spells


def mage_stats(mages: list[dict[str, str | int]]) -> dict[str, float]:
    """This function calculate statistic unsing lambda expression."""
    print("\nStatistic for mages:")
    print("=" * 40)
    stats: dict[str, float] = {
        "max_power": int(max(mages, key=lambda mage: mage["power"])["power"]),
        "min_power": int(min(mages, key=lambda mage: mage["power"])["power"]),
        "avg_power": sum(map(
            lambda mage: int(mage["power"]), mages)) / len(mages)
    }
    print(f"Power max: {stats["max_power"]}")
    print(f"Power min: {stats["min_power"]}")
    print(f"Average power: {stats["avg_power"]:.2f}")
    print("=" * 40)
    return stats


def main() -> None:
    """Entry point of the program"""
    artifacts: list[dict[str, str | int]] = [
        {"name": "Sacred Sword", "power": 12, "type": "sacred"},
        {"name": "Monolith", "power": 25, "type": "evil"},
        {"name": "Luminous Ring", "power": 14, "type": "fairy"}]
    artifact_sorter(artifacts)
    mages: list[dict[str, str | int]] = [
        {"name": "Dark Yannou", "power": 15, "element": "Darkness"},
        {"name": "La Stige", "power": 10, "element": "Grass"},
        {"name": "La Gige", "power": 12, "element": "Earth"},
        {"name": "Dark Marine", "power": 14, "element": "Chaos"}]
    power_filter(mages, 14)
    spells: list[str] = ["poison", "fireball", "heal", "teleportation"]
    spell_transformer(spells)
    mage_stats(mages)


if __name__ == "__main__":
    main()
