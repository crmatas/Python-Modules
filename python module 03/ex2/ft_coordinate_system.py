#! /usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        print("Enter new coordinates as floats in format 'x,y,z':")
        coordinates = input()
        try:
            x_str, y_str, z_str = coordinates.split(",")
        except ValueError:
            print("Invalid syntax")
            print("Enter new coordinates as floats in format 'x,y,z':")
            continue
        try:
            x = float(x_str)
        except ValueError as error:
            print(f"Error on parameter '{x_str}': {error}")
            continue
        try:
            y = float(y_str)
        except ValueError as error:
            print(f"Error on parameter '{y_str}': {error}")
            continue
        try:
            z = float(z_str)
        except ValueError as error:
            print(f"Error on parameter '{z_str}': {error}")
            continue
        break
    return x, y, z


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("")
    print("Get a first set of coordinates")
    x1, y1, z1 = get_player_pos()
    print(f"Got a first tuple: ({x1}, {y1}, {z1})")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    center = math.sqrt(
        x1 ** 2 +
        y1 ** 2 +
        z1 ** 2
    )
    print(f"Distance to center: {center:.4f}")
    print("")
    print("Get a second set of coordinates")
    x2, y2, z2 = get_player_pos()
    print(f"Got a second tuple: ({x2}, {y2}, {z2})")
    print(f"It includes: X={x2}, Y={y2}, Z={z2}")
    distance_f = math.sqrt(
        (x2 - x1)**2 +
        (y2 - y1)**2 +
        (z2 - z1)**2
    )
    print(f"Distance between the 2 sets of coordinates: {distance_f:.4f}")
