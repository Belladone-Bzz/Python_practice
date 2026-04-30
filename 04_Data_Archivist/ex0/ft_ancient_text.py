#!/usr/bin/env python3

"""Filename : ft_ancient_text.py

Date: 2026-03-03
Description: This program open a file, read it and display
his content. Then close the file.
"""


def ft_ancient_text() -> None:
    """"Function to open, read and close a file text"""
    filename: str = "ancient_fragment.txt"
    try:
        print(f"Accessing Storage Vault: {filename}")
        file = open(filename, "r")
        print("Connection established...\n")
        content = file.read()
        print(f"RECOVERED DATA: \n{content}\n")
        file.close()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found."
              " Run data generator first.")
    except Exception as error:
        print("An error occured: ", error)


def main() -> None:
    """Entry point of the program"""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    ft_ancient_text()


if __name__ == "__main__":
    main()
