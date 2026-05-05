#!/usr/bin/env python3

"""Filename : space_station.py

Date: 2026-04-20
Description: This program create a validation system for critical data in a
simulated space station. It helps me to learn basic Pydantic model creation
with BaseModel and Field validation.
"""
from typing import Optional
from datetime import datetime


try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError:
    print("\n[ERROR]: pydantic is not available. Run the command:")
    print("pip install pydantic")
    print("Then run this program again\n")
    exit()


class Station(BaseModel):
    """Pydantic model representing space station with validated fields."""
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)

    def __str__(self) -> str:
        """Display Station attributes."""
        return (
            f"ID: {self.station_id}\n"
            f"Name: {self.name}\n"
            f"Crew: {self.crew_size} people\n"
            f"Power: {self.power_level}%\n"
            f"Oxygen: {self.oxygen_level}%\n"
            f"Last maintenance: {self.last_maintenance}")


def main() -> None:
    """Entry point of the program."""
    print("\nSpace Station Data Validation")
    print("=" * 30)
    station = Station(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now()
    )
    if station.is_operational is True:
        status: str = "Operational"
    else:
        status = "Maintenance Required"
    print("Valid station created")
    print(station)
    print(f"Status: {status}\n")
    print("=" * 30)

    print("Expected validation error:")
    try:
        station = Station(
            station_id="ISS002",
            name="Invalid Station",
            crew_size=22,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
    except ValidationError as error:
        print(error.errors()[0]["msg"])


if __name__ == "__main__":
    main()
