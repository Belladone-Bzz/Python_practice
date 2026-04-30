#!/usr/bin/env python3

"""Filename : ft_pathway_debate.py

Date: 2026-03-30
Description: Module at the root of the repository. It uses absolute and
relative import.
"""


def absolute_import() -> None:
    """Function to test absolute import"""
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    print("\nTesting Absolute Imports (from basic.py):")
    print("lead_to_gold(): ", lead_to_gold())
    print("stone_to_gem(): ", stone_to_gem())


def relative_import() -> None:
    """Function to test relative import"""
    from alchemy.transmutation import philosopher_stone, elixir_of_life
    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosopher_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")


def package_access() -> None:
    """Function to test package import"""
    import alchemy.transmutation
    print("\nTesting Package Access:")
    print("alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosopher_stone()}")


def main() -> None:
    """Entry point of the program"""
    print("\n=== Import Transmutation Mastery ===")
    absolute_import()
    relative_import()
    package_access()
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
