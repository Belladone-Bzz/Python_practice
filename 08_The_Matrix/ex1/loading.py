#!/usr/bin/env python3

"""Filename : loading.py

Date: 2026-04-16
Description: This program import data from an API and create a plot of them.
Pip is the standard/default package installer for Python. It get packages from
the Python Package Index (PyPI) and installs them on the package directory.
Poetry manages dependencies, virtual enrironments and packaging all in one
place.
"""
import importlib


def checking_dependencies(packages: dict[str, str]) -> bool:
    """Function to try import and check dependencies"""
    print("Checking dependencies:")
    check: bool = True
    for key, value in packages.items():
        try:
            module = importlib.import_module(key)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {key} - ({version}) {value} ready")
        except ImportError:
            check = False
            print(f"[KO] {key} - missing dependencie")
    return check


def installation_instructions() -> None:
    """Function to give package's intallation instructions"""
    print("\nTo install missing dependencies with pip and run the program:")
    print("pip install -r requirements.txt")
    print("python3 loading.py")
    print("\nTo install missing dependencies with poetry and run the program:")
    print("poetry install")
    print("poetry run python loading.py")


def matrix() -> None:
    """Function to import data from an API and create a plot"""
    import requests
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    print("\nAnalyzing Matrix data...")
    url = ("https://ressources.data.sncf.com/api/explore/v2.1/catalog/"
           "datasets/frequentation-gares/records?limit=10")
    print("Processing data from an API on 'https://ressources.data"
          ".sncf.com'...")
    connexion = requests.get(url)
    data = connexion.json()["results"]
    """Conversion list[dict] to DataFrame pandas """
    data_frame = pd.DataFrame(data)
    """Creation 3(years)x10(city) matrix numpy"""
    attendance = np.array([
        data_frame["total_voyageurs_2015"].to_numpy(),
        data_frame["total_voyageurs_2020"].to_numpy(),
        data_frame["total_voyageurs_2024"].to_numpy(),
    ])
    """station name extraction"""
    station_name = data_frame["nom_gare"].to_numpy()
    print("Generating visualization...")
    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(station_name))
    width = 0.25
    ax.bar(x - width, attendance[0], width, label="2015")
    ax.bar(x, attendance[1], width,  label="2020")
    ax.bar(x + width, attendance[2], width, label="2024")
    ax.set_xticks(x)
    ax.set_xticklabels(station_name, rotation=45, ha="right")
    ax.ticklabel_format(style="plain", axis="y")
    ax.set_ylabel("Number of travelers")
    ax.set_title("Traveler traffic per station (2015, 2020, 2024)")
    ax.legend()
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    """Entry point of the program"""
    packages: dict[str, str] = {"pandas": "Data manipulation", "numpy":
                                "Numerical computation", "requests":
                                "Network access", "matplotlib":
                                "Visualization"}
    print("LOADING STATUS: Loading programs...\n")
    if checking_dependencies(packages) is False:
        installation_instructions()
    else:
        print()
        matrix()


if __name__ == "__main__":
    main()
