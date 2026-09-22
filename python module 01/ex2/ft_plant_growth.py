#! /usr/bin/env python3
class Plant:
    def __init__(
        self,
        name,
        height,
        age_val
    ) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_val = age_val

    def show(self) -> None:
        print(f"{self.name}: "
              f"{round(self.height, 1)}cm, {self.age()} days old")

    def grow(self) -> None:
        self.height += 0.8
        self.age_val += 1

    def age(self) -> int:
        return self.age_val


def ft_plant_growth() -> None:
    rose = Plant("rose", 25.0, 30)
    initial_height = rose.height
    rose.show()
    for days in range(1, 8):
        print(f"=== Day {days} ===")
        rose.grow()
        rose.age()
        rose.show()
    growth = rose.height - initial_height
    print(f"Growth this week: {round(growth, 1)}cm")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    ft_plant_growth()
