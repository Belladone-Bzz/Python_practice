#!/usr/bin/env python3

"""Filename : ft_data_alchemist.py

Date: 2026-03-23
Description: This program demonstrates list and dict comprehension
for data processing.
"""
import random


def ft_data_alchemist() -> None:
    """Function to create new list and dict with comprehension method"""
    players_list: list[str] = ["Alice", "bob", "Charlie", "dylan", "Jolyne",
                               "camille", "Ady", "emma", "Luka", "audrey"]
    print(f"Initial list of players: {players_list}")
    all_capitalize: list[str] = [name.capitalize() for name in players_list]
    print(f"New list with all names capitalized: {all_capitalize}")
    capitalized_only: list[str] = \
        [name for name in players_list if name[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}")
    score_dict: dict[str, int] = \
        {name: random.randint(0, 1000) for name in all_capitalize}
    print(f"\nScore dict: {score_dict}")
    length_dict: int = len(score_dict)
    sum_score: int = 0
    for _, quantity in score_dict.items():
        sum_score += quantity
    mean_score: float = sum_score / length_dict
    print(f"Score average is {mean_score:.2f}")
    higher_score_dict: dict[str, int] = {pair[0]: pair[1] for
                                         pair in score_dict.items()
                                         if pair[1] > mean_score}
    print(f"High scores: {higher_score_dict}")


def main() -> None:
    """Entry point of the program"""
    print("=== Game Analytics Dashboard ===\n")
    ft_data_alchemist()


if __name__ == "__main__":
    main()
