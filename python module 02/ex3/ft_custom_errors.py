#! /usr/bin/env python3
class GardenError(Exception):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


def check_plant() -> None:
    raise PlantError("the tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Garden Error types Demo ===")
    print("")
    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print("Caught PlantError: ", e)
    print("")
    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as e:
        print("Caught WaterError:", e)
    print("")
    print("Testing catching all garden errors...")
    try:
        check_plant()
    except GardenError as e:
        print("Caught GardenError: ", e)
    try:
        check_water()
    except GardenError as e:
        print("Caught GardenError: ", e)
    print("")
    print("All custom error types work correctly!")
