#!/usr/bin/env python3

"""Filename : alien_contact.py

Date: 2026-04-23
Description: This program create a more sophisticated validation system
that go beyond simple field constraints.
"""
from datetime import datetime
from enum import Enum
from typing import Optional


try:
    from pydantic import BaseModel, Field, model_validator
except ImportError:
    print("\n[ERROR]: pydantic is not available. Run the command:")
    print("pip install pydantic")
    print("Then run this program again\n")
    exit()


class ContactType(Enum):
    """Enumeration for type of alien contact."""
    RADIO = 0
    VISUAL = 1
    PHYSICAL = 2
    TELEPATHIC = 3


class AlienContact(BaseModel):
    """Pydantic model representing Alien contact with validated fields."""
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=0, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_validation(self) -> "AlienContact":
        """Model validator for attributes of Alien Contact."""
        if self.contact_id.startswith("AC") is False:
            raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
        if self.contact_type == ContactType.PHYSICAL and\
                self.is_verified is False:
            raise ValueError("Physical contact reports must be verifed")
        if self.contact_type == ContactType.TELEPATHIC and\
                self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 "
                             "witnesses")
        if self.signal_strength > 7 and\
                self.message_received is None:
            raise ValueError("Strong signals (> 7.0) should include received "
                             "messages")
        return self

    def __str__(self) -> str:
        """Display AlienContact attributes."""
        return (
            f"ID: {self.contact_id}\n"
            f"Type: {self.contact_type}\n"
            f"Location: {self.location}\n"
            f"Signal: {self.signal_strength}/10\n"
            f"Duration: {self.duration_minutes} minutes\n"
            f"Witnesses: {self.witness_count}\n"
            f"Message: '{self.message_received}'\n")


def main() -> None:
    """Entry point of the program."""
    print("\nAlien Contact Log Validation")
    print("=" * 30)
    contact = AlienContact(
        contact_id="AC_2024_01",
        timestamp=datetime.now(),
        location="Area 42, Marseille",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from PythonPlanet"
    )
    print("Valid contact report:")
    print(contact)
    print("=" * 30)
    print("Expected validation error:")
    try:
        contact = AlienContact(
            contact_id="AC_2024_01",
            timestamp=datetime.now(),
            location="Area 42, Marseille",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from PythonPlanet"
        )
    except ValueError as error:
        print(error.errors()[0]["ctx"]["error"])


if __name__ == "__main__":
    main()
