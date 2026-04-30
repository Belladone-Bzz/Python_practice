#!/usr/bin/env python3

"""Filename : construct.py

Date: 2026-04-15
Description: This program create a clean, isolated Python virtual environment.
It detects if its running inside a virtual environment, displays informations
about the current Python environment, provides insctructions fo creating and
activating a virtual environment if non is detected and shows the difference
between global and virtual environment package locations.
"""
import sys
import site


def main() -> None:
    """Entry point of the program"""
    virtual_env: str = sys.prefix
    if sys.platform == "linux":
        path_split: list[str] = virtual_env.split("/")
    if sys.platform == "win32":
        path_split: list[str] = virtual_env.split("\\")
    if sys.prefix == sys.base_prefix:
        """sys.prefix gives the prefix directory where Python files are
        installed. On Unix, the default is /usr/local. If a virtual environment
        is in effect, this prefix will point to this virtual environment. As
        sys.base.prefix gives the prefix directory where base Python files are
        installed, if sys.prefix == base_prefix, then, we are not in a virtual
        environment.
        """
        print("MATRIX STATUS : You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual environment: None detected")
        print("\nWARNING: You are in the global envirnment!")
        print("The machine can see everything you install.")
        print("\nPackage installation path:")
        print(f"{site.getsitepackages()[0]}")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {path_split[-1]}")
        print(f"Environment Path: {virtual_env}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install package without affecting the global system.\n")
        print("Package installation path:")
        print(f"{site.getsitepackages()[0]}")


if __name__ == "__main__":
    main()
