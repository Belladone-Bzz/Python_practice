#!/usr/bin/env python3

"""Filename : ft_stream_management.py

Date: 2026-03-03
Description: This program manipulate output, input and error
streams to take or display data.
"""

import sys


def ft_stream_management() -> None:
    """Function to manipulate output, input and error streams"""
    try:
        sys.stdout.write("Input Stream active. Enter archivist ID: ")
        sys.stdout.flush()
        archivist_id = sys.stdin.readline().rstrip("\n")
        sys.stdout.write("Input Stream active. Enter status report: ")
        sys.stdout.flush()
        status_report = sys.stdin.readline()
        sys.stdout.write(f"\n[STANDARD] Archive status from {archivist_id}: "
                         f"{status_report}")
        sys.stderr.write("[ALERT] System diagnostic: Communication channels"
                         " verified\n")
        sys.stderr.flush()
    except Exception as error:
        sys.stderr.write(f"[ALERT] System diagnostic: Error - {error}\n")
        sys.stderr.flush()
    finally:
        sys.stdout.write("[STANDARD] Data transmission complete\n")
        sys.stdout.write("\nThree-channel communication test successful\n")


def main() -> None:
    """Entry point of the program"""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    ft_stream_management()


if __name__ == "__main__":
    main()
