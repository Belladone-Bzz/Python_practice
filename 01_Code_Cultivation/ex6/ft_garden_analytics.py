#!/usr/bin/env python3

"""Filename : ft_garden_analytics.py

Date: 2026-02-23
Description: This program manage different gardens containing
different type of plants with their specific attributes and
methods. Then display informations about all plants of each garden.
Introduce nested classes and class and static methods.
"""


class Plant:
    """Class Plant
    Attributes: name, height and growth
    """

    def __init__(self, name: str, height: int, growth: int) -> None:
        """Initialize instance's attributes"""
        self.name: str = name
        self.__height: int = 0
        self.set_height(height)
        self.growth: int = growth

    def get_height(self) -> int:
        """Getter for height attribute"""
        return self.__height

    def set_height(self, value: int) -> None:
        """Setter for height attribute, can't be negative"""
        if value > 0:
            self.__height = value
        else:
            print("\nInvalid operation attempted: height",
                  f"{value}cm [REJECTED]")

    def __str__(self) -> str:
        """Display plant attributs"""
        return (f"- {self.name.capitalize()}: {self.get_height()}cm")

    def __int__(self) -> int:
        return 0

    def grow(self) -> int:
        """Operation to grow the plant"""
        self.__height += self.growth
        print(f"{self.name.capitalize()} grew {self.growth}cm")
        return self.growth


class FloweringPlant(Plant):
    """Class FloweringPlant, inherits from Plant
    Attributes: name, height, growth color
    """

    def __init__(self, name: str, height: int,
                 growth: int, color: str) -> None:
        """Initialize instance's attributes"""
        super().__init__(name, height, growth)
        self.color: str = color

    def __str__(self) -> str:
        """Return format str with all informations"""
        return (super().__str__() + f", {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    """Class PrizeFlower, inherits from FloweringPlant
    Attributes: name, height, growth, color, score
    """

    def __init__(self, name: str, height: int,
                 growth: int, color: str, score: int) -> None:
        """Initialize instance's attributes"""
        super().__init__(name, height, growth, color)
        self.score: int = score

    def __str__(self) -> str:
        """Return format str with all informations"""
        return (super().__str__() + f", Prize points: {self.score}")

    def __int__(self) -> int:
        return self.score


class Garden:
    """Class Garden
    Attributes: owner, plants list
    """

    def __init__(self, owner: str, plants: list[
                 Plant | FloweringPlant | PrizeFlower] = []) -> None:
        """Initialize instance's attributes"""
        self.owner: str = owner
        self.plants: list[Plant | FloweringPlant | PrizeFlower] = []
        self.total_growth: int = 0
        self.total_plants_number: int = 0
        self.plant_number: list[int] = [0, 0, 0]
        for plant in plants:
            self.add_plant(plant)
        print()

    def add_plant(self, new_plant: Plant | FloweringPlant
                  | PrizeFlower) -> None:
        """add plants in the garden"""
        self.plants.append(new_plant)
        self.total_plants_number += 1
        if new_plant.__class__.__name__ == "Plant":
            self.plant_number[0] += 1
        elif new_plant.__class__.__name__ == "FloweringPlant":
            self.plant_number[1] += 1
        elif new_plant.__class__.__name__ == "PrizeFlower":
            self.plant_number[2] += 1
        print(f"Added {new_plant.name.capitalize()} to",
              f"{self.owner.capitalize()}'s garden")

    def total_score(self) -> int:
        """calculate total score of garden"""
        total: int = 0
        for plant in self.plants:
            if plant.__class__.__name__ == "PrizeFlower":
                total += int(plant)
        return total

    def grow_plant(self) -> None:
        """grow all plants of garden"""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            growth = plant.grow()
            self.total_growth += growth
        print()


class GardenManager:

    gardens_list: list[Garden] = []
    total_gardens: int = 0

    @classmethod
    def create_garden_network(cls, gardens: list[tuple[
                              str, list[Plant | FloweringPlant |
                                        PrizeFlower]]]) -> None:
        """create garden network"""
        for garden in gardens:
            cls.add_garden(garden)

    @classmethod
    def add_garden(cls, new_garden: tuple[str, list[
                                          Plant | FloweringPlant |
                                          PrizeFlower]]) -> None:
        """add a garden to the garden network"""
        cls.total_gardens += 1
        cls.gardens_list.append(Garden(new_garden[0], new_garden[1]))

    @classmethod
    def grow_garden(cls) -> None:
        """grow all garden"""
        for garden in cls.gardens_list:
            garden.grow_plant()

    class GardenStats:
        @staticmethod
        def print_report_garden(gardens_list: list[Garden]) -> None:
            """display all informations of gardens"""
            for garden in gardens_list:
                test_height: bool = True
                print(f"=== {garden.owner}'s Garden Report ===")
                print("Plants in garden:")
                for plant in garden.plants:
                    if plant.get_height() < 0:
                        test_height = False
                    print(plant)
                print()
                print(f"Plants added: {garden.total_plants_number},",
                      f"Total growth: {garden.total_growth}cm")
                print(f"Plant types: {garden.plant_number[0]} regular,",
                      f"{garden.plant_number[1]} flowering,",
                      f"{garden.plant_number[2]} prize flowers")
                print()

                print(f"Height validation test: {test_height}")
            print("Garden scores -", end="")
            for garden in gardens_list:
                print(f" {garden.owner.capitalize()}:",
                      f"{garden.total_score()}", end="")
                if garden != gardens_list[-1]:
                    print(",", end="")
            print(f"\nTotal gardens managed: {GardenManager.total_gardens}")


def ft_gardens_init() -> None:
    """init list for gardens creation"""
    gardens: list[tuple[
        str, list[Plant | FloweringPlant | PrizeFlower]]] = [
        ("Jolyne", [
            Plant("bamboo", 450, 20),
            FloweringPlant("cherry tree", 320, 1, "pink"),
            PrizeFlower("mystherbe", 19, 0, "green", 120)]),
        ("Marine", [
            Plant("beeplant", 2, 0),
            FloweringPlant("tulip", 12, 1, "yellow"),
            FloweringPlant("peony", 16, 1, "pastel rose"),
            PrizeFlower("golden sweat", 28, 2, "dark red", 666)
        ])
        ]
    GardenManager.create_garden_network(gardens)
    GardenManager.grow_garden()
    GardenManager.GardenStats.print_report_garden(GardenManager.gardens_list)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    ft_gardens_init()
