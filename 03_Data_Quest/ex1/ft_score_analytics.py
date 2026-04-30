#!/usr/bin/env python3

"""Filename : ft_score_analytics.py

Date: 2026-03-12
Description: This program processes player scores passed as
command-line arguments and displays basic statistical information.
"""
import sys


def parsing_score(data: list[str]) -> list[int]:
    """Function to parse score passed as command-line arguments"""
    scores: list[int] = []
    for value in data:
        try:
            scores.append(int(value))
        except ValueError:
            print(f"Invalid parameter : '{value}'")
    return scores


def ft_score_analytics(data: list[str]) -> None:
    """Function to analyse scores"""
    total_args: int = len(data)
    program_name: str = data[0]
    if total_args < 2:
        print(f"No scores provided. Usage: python3 {program_name[2:]}"
              " <score1> <score2> ...")
        print()
        return
    scores: list[int] = parsing_score(data[1:])
    if scores == []:
        print(f"No scores provided. Usage: python3 {program_name[2:]}"
              " <score1> <score2> ...")
        print()
        return
    print(f"Scores processed: {scores}")
    total_players: int = len(scores)
    print(f"Total players: {total_players}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {(sum(scores)/total_players)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
    print()


def main() -> None:
    """Entry point of the program"""
    print("=== Player Score Analytics ===")
    ft_score_analytics(sys.argv)


if __name__ == "__main__":
    main()
