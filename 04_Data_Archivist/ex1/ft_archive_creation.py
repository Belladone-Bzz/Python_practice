#!/usr/bin/env python3

"""Filename : ft_archive_creation.py

Date: 2026-03-03
Description: This program creates a file, write content on it
and close the file. If the file already exist, it overwrites
it depending on a user input
"""


def ft_check_file(filename: str) -> int:
    """Function to check if file already exist, if it's the case
    the user can ask to overwrite it or not
    """
    try:
        open(filename, "r")
        print(f"{filename} already exist.")
        response = input(f"Do you want to overwrite on {filename} ? (y/n)")
        print()
        if response == "y":
            return 0
        else:
            return -1
    except FileNotFoundError:
        print(f"Initializing new storage unit: {filename}")
        return 1


def ft_archive_creation() -> None:
    """Function to create and write in a file text. Or to
    overwrite it depending on check_file() return
    """
    filename: str = "new_discovery.txt"
    content: list[str] = [
        ("New quantum algorithm discovered"),
        ("Efficiency increased by 347%"),
        ("Archived by Data Archivist trainee")
    ]
    try:
        response = ft_check_file(filename)
        if response != -1:
            file = open(filename, "w")
            if response == 1:
                print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            initial_entry: int = 0
            for line in content:
                printed_line = f"[ENTRY {"%03d" % initial_entry}] {line}"
                file.write(printed_line)
                if initial_entry < (len(content) - 1):
                    file.write("\n")
                print(printed_line)
                initial_entry += 1
            file.close()
            print("\nData inscription complete. Storage unit sealed.")
            print(f"Archive '{filename}' ready for long-term preservation.")
        else:
            print(f"As asked, {filename} was not overwrited")
    except Exception as error:
        print("An error as occured: ", error)


def main() -> None:
    """Entry point of the program"""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    ft_archive_creation()


if __name__ == "__main__":
    main()
