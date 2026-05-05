#!/usr/bin/env python3

"""Filename : space_crew.py

Date: 2026-04-25
Description: This program create an even more sophisticated validation system
that go beyond simple field constraints with nested Pydantic models.
"""
from datetime import datetime
from enum import Enum


try:
    from pydantic import BaseModel, Field, model_validator, ValidationError
except ImportError:
    print("\n[ERROR]: pydantic is not available. Run the command:")
    print("pip install pydantic")
    print("Then run this program again\n")
    exit()


class Rank(str, Enum):
    """Enumeration for type of crew member rank."""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Pydantic model representing crew member with validated fields."""
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Pydantic model representing SpaceMission with validated fields."""
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_validation(self) -> "SpaceMission":
        """Model validator for SpaceMission attributes."""
        if self.mission_id.startswith("M") is False:
            raise ValueError("Mission ID must start with 'M' (Mission)")
        if all(crew.is_active for crew in self.crew) is False:
            raise ValueError("All crew members must be active")
        if any(crew.rank in [Rank.CAPTAIN, Rank.COMMANDER]
               for crew in self.crew) is False:
            raise ValueError("Mission must have at least one Commander or"
                             " Captain")
        if self.duration_days > 365 and len(list(filter(
                lambda crew: crew.years_experience >= 5,
                self.crew))) < (len(self.crew)) / 2:
            raise ValueError("Long mission(> 350 days) need 50% of 5+ "
                             "years experienced members in the crew")
        return self

    def __str__(self) -> str:
        """Display SpaceMission attributes."""
        return (
            f"Mission: {self.mission_name}\n"
            f"ID: {self.mission_id}\n"
            f"Destination: {self.destination}\n"
            f"Duration: {self.duration_days} days\n"
            f"Budget: ${self.budget_millions}M\n"
            f"Crew size: {len(self.crew)}\n"
            "Crew members:\n"
            + "\n".join(
                f"- {member.name} ({member.rank.value}) - "
                f"{member.specialization}" for member in self.crew))


def main() -> None:
    """Entry point of the program"""
    print("\nSpace Mission Crew Validation")
    print("=" * 30)
    print("Valid mission created:")
    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        launch_date=datetime.now(),
        destination="Mars",
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="CM001", name="Sarah Connor",
                rank=Rank.COMMANDER, age=35,
                specialization="Mission Command", years_experience=8),
            CrewMember(
                member_id="CM002", name="John Smith",
                rank=Rank.LIEUTENANT, age=43,
                specialization="Navigation", years_experience=3),
            CrewMember(
                member_id="CM002", name="Alice Johnson",
                rank=Rank.OFFICER, age=51,
                specialization="Engineering", years_experience=12)])
    print(mission)
    print()
    print("=" * 30)
    print("Expected validation error:")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            launch_date=datetime.now(),
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="CM001", name="Sarah Connor",
                    rank=Rank.CADET, age=35,
                    specialization="Mission Command", years_experience=8),
                CrewMember(
                    member_id="CM002", name="John Smith",
                    rank=Rank.LIEUTENANT, age=43,
                    specialization="Navigation", years_experience=3),
                CrewMember(
                    member_id="CM002", name="Alice Johnson",
                    rank=Rank.OFFICER, age=51,
                    specialization="Engineering", years_experience=12)])
    except ValidationError as error:
        print(error.errors()[0]["ctx"]["error"])


if __name__ == "__main__":
    main()
