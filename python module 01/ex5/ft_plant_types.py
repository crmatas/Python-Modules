#! /usr/bin/env python3
class Plant:
    def __init__(
        self,
        name,
        height,
        age
    ) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age

    def grow(self, days=1) -> None:
        self._height += days

    def age_days(self, days=1) -> None:
        self._age += days

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: "
              f"{round(self._height, 1)}cm, {self._age} days old")


class Flower(Plant):
    def __init__(
        self,
        name,
        height,
        age,
        color,
        bloomed: bool
    ) -> None:

        super().__init__(name, height, age)
        self._color = color
        self._bloomed = bloomed

    def bloom(self, status: bool) -> None:
        self._bloomed = status
        if self._bloomed:
            print(f" {self._name} has not bloomed yet!")
        else:
            print(f" {self._name} is blooming beatifully!")

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")


class Tree(Plant):
    def __init__(
            self,
            name,
            height,
            age,
            trunk_diameter
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces shade "
              f"of {self._height}cm long and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
            self,
            name,
            height,
            age,
            harvest_season,
            nutritional_value
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def age_days(self, days=1) -> None:
        super().age_days(days)
        self._nutritional_value += days


def ft_plant_types() -> None:
    rose = Flower("rose", 15.0, 10, "red", False)
    print("=== Flower")
    rose.show()
    rose.bloom(True)
    print("[asking the rose to bloom]")
    rose.show()
    rose.bloom(False)
    print("")
    print("===Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("")
    tomato = Vegetable("tomato", 5.0, 10, "April", 0)
    print("=== Vegetable")
    tomato.show()
    tomato.grow()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(41)
    tomato.age_days(20)
    tomato.show()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    ft_plant_types()
