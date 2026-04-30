#!/usr/bin/env python3

"""Filename : ft_crisis_response.py

Date: 2026-03-03
Description: This program manipulate a file text using with protocol
and manages errors
"""


def ft_crisis_response(filename: str, error: str) -> None:
    """Function to handle error response"""
    print(f"CRISIS ALERT: Attempting access to '{filename}...")
    print(f"RESPONSE: {error}")


def ft_open_file(filename: str) -> None:
    """Function to open a file and handle it"""
    with open(filename, "r") as file:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}...")
        content = file.read()
        print(f"SUCCESS: Archive recovered - ''{content}''")


def ft_read_file(filename: str) -> None:
    """Function to handle error while manipulating files"""
    try:
        ft_open_file(filename)
        print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        error = "Archive not found in storage matrice"
        ft_crisis_response(filename, error)
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        error = "Security protocol deny access"
        ft_crisis_response(filename, error)
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as error:
        print(f"CRISIS ALERT: Attempting access to '{filename}...")
        print(f"RESPONSE: {error}")
        print("STATUS: Crisis handled\n")


def main() -> None:
    """Entry point of the program"""
    filename_00 = "lost_archive.txt"
    filename_01 = "classified_vault.txt"
    filename_02 = "standard_archive.txt"
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    ft_read_file(filename_00)
    ft_read_file(filename_01)
    ft_read_file(filename_02)
    print("All crisis scenarios handled successfully. Archive secure.")


if __name__ == "__main__":
    main()
