#!/usr/bin/env python3

"""Filename : ft_inventory_system.py

Date: 2026-03-18
Description: This program manage data using dictionaries. For that, it uses
dict methods like keys(), values(), items(), get() and update().
"""


import sys


class InventoryManager:
    inventory: dict[str, int] = {}
    total_items_quantity: int = 0

    @classmethod
    def display_inventory_info(cls) -> None:
        """Class method to display general information of inventory"""
        item_list: list[str] = []
        for item, quantity in cls.inventory.items():
            item_list.append(item)
        print(f"Item list: {item_list}")
        for _, quantity in cls.inventory.items():
            cls.total_items_quantity += quantity
        print(f"Total quantity of the {len(cls.inventory.items())}"
              f" items: {cls.total_items_quantity}")

    @classmethod
    def display_inventory_details(cls) -> None:
        """Class method to display percentage of each key"""
        for item, quantity in cls.inventory.items():
            print(f"Item {item} represents "
                  f"{quantity / cls.total_items_quantity * 100:0.1f}%")

    @classmethod
    def display_inventory_stats(cls) -> None:
        """Class method to display most and least abundant item"""
        maximal_value: int = 1
        most_abundant: str = ""
        least_abundant: str = ""
        for item, quantity in cls.inventory.items():
            if quantity > maximal_value:
                maximal_value = quantity
                most_abundant = item
        print(f"Item most abundant: {most_abundant}"
              f" with quantity {maximal_value}")
        if maximal_value == 1:
            print("Item least abundant: The maximum number of items in your "
                  "inventory is 1. Therefore, there are no items in this"
                  " category.")
            return
        minimal_value: int = maximal_value
        for item, quantity in cls.inventory.items():
            if quantity < minimal_value:
                minimal_value = quantity
                least_abundant = item
        print(f"Item least abundant: {least_abundant}"
              f" with quantity {minimal_value}")


def ft_parsing_arguments(data: list[str]) -> None:
    """Function to parsed command-line arguments and create dictionary"""
    total_args: int = len(data)
    items: list[str] = []
    if total_args < 2:
        print(f"No inventory provided. You have to use python3 {data[0]}"
              f" <item1:quantity1> <item2:quantity2> <item3:quantity3> ...")
    else:
        for argument in data[1:]:
            try:
                item, quantity = argument.split(":")
                for obj in items:
                    if obj == item:
                        raise NameError
                items.append(item)
                try:
                    int(quantity)
                    if int(quantity) > 0:
                        InventoryManager.inventory[item.lower()] = \
                            InventoryManager.inventory.get(item.lower(), 0) \
                            + int(quantity)
                    else:
                        print("You tried to enter a zero or negative quantity:"
                              f" {argument} - ignored")
                except ValueError as error:
                    print(f"Quantity error for '{quantity}': ", error)
            except NameError:
                print(f"Redundant item '{item}' - discarding")
            except ValueError:
                print(f"Error: invalid parameter {argument} - ignored")
            except Exception as error:
                print(f"An error occured : {error}. Expected format:"
                      " <item:quantity>")
        print(f"Got inventory: {InventoryManager.inventory}")


def main() -> None:
    """Entry point of the program"""
    print("=== Iventory System Analysis")
    ft_parsing_arguments(sys.argv)
    if len(InventoryManager.inventory) > 0:
        InventoryManager.display_inventory_info()
        InventoryManager.display_inventory_details()
        InventoryManager.display_inventory_stats()
        InventoryManager.inventory.update({"magic_item": 1})
        print(f"Updated inventory: {InventoryManager.inventory}")
    else:
        print("Inventory is empty. The program stop here.")


if __name__ == "__main__":
    main()
