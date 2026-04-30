#!/usr/bin/env python3

"""Filename : ft_achievement_tracker.py

Date: 2026-03-17
Description: This program tracks and analyzes player achievements
using sets to demonstrate deduplication and set operations.
"""
import random


ACH_LIST: list[str] = ["Crafting Genius", "World Savior", "Master Explorer",
                       "Collector Supreme", "Untouchable", "Boss Slayer",
                       "Strategist", "Speed Runner", "Survivor",
                       "Treasure Hunter", "Unstoppable", "First Steps",
                       "Sharp Mind", "Hidden Path Finder"]


class Player:
    """Class Player
    Attributes: name, achievements
    """
    def __init__(self, name: str, achievements: set[str]) -> None:
        """Initialize instance's attributes"""
        self.achievements: set[str] = achievements
        self.name: str = name

    def __str__(self) -> str:
        """Display player attributes"""
        return (f"Player {self.name}: {self.achievements}")


class PlayerManager:
    """Class PlayerManager
    Methods: add_player(), display_all_distinct_achs(),
    display_common_achs(), display_unique_achs(), display_missing_achs()
    """
    player_list: list[Player] = []
    all_distinct_achv: set[str] = set()
    all_achs: list[set[str]] = []

    @classmethod
    def add_player(cls, new_player: str, ply_achs: set[str]) -> None:
        """Class method to add player in cls.player_list"""
        cls.player_list.append(Player(new_player, ply_achs))

    @classmethod
    def display_all_distinct_achs(cls) -> None:
        """Class method to display all disctinct achievements"""
        for player in cls.player_list:
            cls.all_distinct_achv = \
                cls.all_distinct_achv.union(player.achievements)
        print(f"\nAll distinct achievements: {cls.all_distinct_achv}\n")

    @classmethod
    def display_common_achs(cls) -> None:
        """Class method to display common achivementes between all players"""
        for player in cls.player_list:
            cls.all_achs.append(player.achievements)
        common_ach: set[str] = cls.all_achs[0]
        for achievement in cls.all_achs[1:]:
            common_ach = common_ach.intersection(achievement)
        len_set: int = len(common_ach)
        if len_set == 0:
            print("Common achievements: There is no common achievements "
                  "between all the players\n")
        else:
            print(f"Common achievements: {common_ach}\n")

    @classmethod
    def display_unique_achs(cls, players_name: list[str]) -> None:
        """Class method to display each player's unique achievements"""
        temp_player_list = cls.player_list
        for player in temp_player_list:
            temporary_all_achs: set[str] = set()
            unique_achs: set[str] = set()
            for ply in cls.player_list:
                if player.name != ply.name:
                    temporary_all_achs = \
                        temporary_all_achs.union(ply.achievements)
            unique_achs = player.achievements.difference(temporary_all_achs)
            print(f"Only {player.name} has: {unique_achs}")
        print()

    @classmethod
    def display_missing_achs(cls) -> None:
        """Class method to display each player's missing achievements"""
        all_existing_achs: set[str] = set()
        for achievement in ACH_LIST:
            all_existing_achs.add(achievement)
        for player in cls.player_list:
            missing_achs: set[str] = set()
            missing_achs = all_existing_achs.difference(player.achievements)
            print(f"{player.name} is missing: {missing_achs}")


def gen_player_achievements() -> set[str]:
    """Function to randomly assign achievements to player"""
    total_ach: int = len(ACH_LIST)
    nb_ach: int = random.randint(5, (total_ach))
    set_achievements: set[str] = set()
    i: int = 0
    while i < nb_ach:
        set_achievements.add(ACH_LIST[random.randint(0, (total_ach - 1))])
        i += 1
    return set_achievements


def players_initialization_and_stats() -> None:
    """Function to initialize player(Player)"""
    plys: list[str] = ["Alice", "Bob", "Charlie", "Dylan", "Jolyne"]
    achievements: set[str] = set()
    for player in plys:
        achievements = gen_player_achievements()
        PlayerManager.add_player(player, achievements)
        print(f"Player {player}: {achievements}")
    PlayerManager.display_all_distinct_achs()
    PlayerManager.display_common_achs()
    PlayerManager.display_unique_achs(plys)
    PlayerManager.display_missing_achs()


def main() -> None:
    """Entry point of the program"""
    print("=== Achievement Tracker System ===\n")
    players_initialization_and_stats()


if __name__ == "__main__":
    main()
