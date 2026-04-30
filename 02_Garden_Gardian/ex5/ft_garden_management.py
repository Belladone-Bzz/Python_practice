#!/usr/bin/env python3

"""Filename : ft_garden_management.py

Date: 2026-03-01
Description: This program manage gardens and check for
differents possible custom errors. This module uses
all precedents concepts.
"""


class GardenError(Exception):
    """Garden Error class that inherit from Exception"""
    pass


class PlantError(GardenError):
    """PlantError class that inherit from GardenError"""
    pass


class NameError(PlantError):
    """PlantError class that inherit from GardenError"""
    pass


class WaterError(PlantError):
    """PlantError class that inherit from GardenError"""
    pass


class SunError(PlantError):
    """PlantError class that inherit from GardenError"""
    pass


class Plant:
    """Class Plant
    Attributes: name, height and growth
    """
    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        """Initialize instance's attributes"""
        self.name: str = name
        self.water_level: int = water_level
        self.sunlight_hours: int = sunlight_hours


class GardenManager:
    """Class GardenManager
    Attributes: plants_list, water_tank
    Methods: add_plant(), water_plant(), check_plant_health()
    """
    def __init__(self, water_tank: int) -> None:
        """Initialize instance's attributes"""
        self.plants_list: list[Plant] = []
        self.water_tank: int = water_tank

    def add_plant(self, plants: list[Plant]) -> None:
        """Method to add plant in plants_list"""
        print("\nAdding plants to garden...")
        for plant in plants:
            try:
                if plant.name != "":
                    self.plants_list.append(plant)
                    print(f"Added {plant.name} successfully")
                else:
                    raise NameError("Plant name cannot be empty!")
            except NameError as error:
                print("Error adding plant: ", error)

    def water_plants(self) -> None:
        """Method to water plant in plants_list"""
        print("\nWatering plants...")
        print("Opening watering system")
        try:
            for plant in self.plants_list:
                if self.water_tank > 0:
                    print(f"Watering {plant.name} - success")
                    self.water_tank -= 1
                    plant.water_level += 1
                else:
                    raise GardenError("Not enough water in tank")
        except GardenError as error:
            print("Caught GardenError: ", error)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        """Method to check plants health"""
        print("\nChecking plant health...")
        for plant in self.plants_list:
            try:
                if plant.water_level < 1:
                    raise WaterError(f"Water level {plant.water_level}"
                                     " is too low (min 1)")
                elif plant.water_level > 10:
                    raise WaterError(f"Water level {plant.water_level}"
                                     " is too hight (max 10)")
                elif plant.sunlight_hours < 2:
                    raise SunError(f"Sunlight hours {plant.sunlight_hours}"
                                   " is too low (min 2)")
                elif plant.sunlight_hours > 12:
                    raise SunError(f"Sunlight hours {plant.sunlight_hours}"
                                   " is too hight (max 12)")
                else:
                    print(f"{plant.name}: healthy (water: {plant.water_level},"
                          f" sun: {plant.sunlight_hours})")
            except (WaterError, SunError) as error:
                print(f"Error checking {plant.name}: ", error)

    def check_garden_tools(self) -> None:
        """Method to check garden tools"""
        print("\nTesting error recovery...")
        try:
            if self.water_tank < 1:
                raise GardenError("Not enough water in tank")
            else:
                print(f"There are {self.water_tank} units of"
                      " water left in the tank ")
        except GardenError as error:
            print("Caught GardenError: ", error)
        finally:
            print("System recovered and continuing...")


def test_garden_management() -> None:
    """Function to init garden and check it"""
    print("=== Garden Management System ===")
    plants_list: list[Plant] = [
        Plant("tomato", 4, 8),
        Plant("lettuce", 14, 5),
        Plant("", 8, 5),
    ]
    garden = GardenManager(2)
    garden.add_plant(plants_list)
    garden.water_plants()
    garden.check_plant_health()
    garden.check_garden_tools()
    print("\nGarden management system test complete!\n")


if __name__ == "__main__":
    test_garden_management()
