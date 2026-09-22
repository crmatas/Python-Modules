#! /usr/bin/env python3
import sys
weapons: dict[str, int] = {}


def main():

    for arg in (sys.argv[1:]):
        if ':' not in arg:
            print(f"Error - Invalid parameter '{arg}'")
            continue
        parts = arg.split(':', 1)
        item_name = parts[0]
        item_index = parts[1]
        try:
            item_index = int(item_index)
        except ValueError:
            print(f"Quantity error for '{item_name}': invalid literal for"
                  f" int() woth base 10: '{item_index}'")
            continue
        if item_name in weapons:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        weapons[item_name] = item_index
    print(f"Got inventory: {weapons}")
    item_list = list(weapons.keys())
    print(f"Item list: {item_list}")
    total_quantity = sum(weapons.values())
    print(f"Total quantity of the {len(item_list)} items: {total_quantity}")
    # create the percerntage
    for item, qty in weapons.items():
        percentage = (qty / total_quantity) * 100
        percentage_rounded = round(percentage, 1)
        print(f"Item {item} represents {percentage_rounded}%")
    # least and most
    most_item = ""
    most_quantity = -1
    least_item = ""
    least_quantity = float('inf')
    for item, qty in weapons.items():
        if qty > most_quantity:
            most_quantity = qty
            most_item = item
    for item, qty in weapons.items():
        if qty < least_quantity:
            least_quantity = qty
            least_item = item
    print(f"Item most abundant: {most_item} with quantity {most_quantity}")
    print(f"Item least abundant: {least_item} with quantity {least_quantity}")
    weapons.update({'magic item': 1})
    print(f"Updated inventory: {weapons}")


if __name__ == '__main__':
    print("=== Inventory System Analysis ===")
    main()
