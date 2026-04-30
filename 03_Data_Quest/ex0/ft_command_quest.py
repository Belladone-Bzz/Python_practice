#!/usr/bin/env python3

"""Filename : ft_command_quest.py

Date: 2026-03-12
Description: This program processes command-line arguments
and displays basic information about the executed program.
"""
import sys


def ft_command_quest(data: list[str]) -> None:
    """Function to handle and display command line arguments"""
    total_arguments: int = len(data)
    program_name: str = data[0]
    if total_arguments < 2:
        print(f"Program name: {program_name[2:]}")
        print("No arguments provided !")
        print(f"Total arguments: {total_arguments}\n")
        return
    else:
        index: int = 1
        print(f"Program name: {program_name[2:]}")
        print(f"Argument received: {total_arguments - 1}")
        for argument in data[1:]:
            print(f"Argument {index}: {argument}")
            index += 1
        print(f"Total arguments: {total_arguments}\n")


def main() -> None:
    """Entry point of the program"""
    print("=== COMMAND QUEST ===")
    ft_command_quest(sys.argv)


if __name__ == "__main__":
    main()
