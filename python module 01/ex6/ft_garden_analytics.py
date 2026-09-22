#! /usr/bin/env python3
class Plant:
    # Nested class / internal system of statistics
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
            self._shade_calls = 0

        # methods to increment 1
        def increment_grow(self): self._grow_calls += 1
        def increment_age(self): self._age_calls += 1
        def increment_show(self): self._show_calls += 1
        def increment_shade(self): self._shade_calls += 1

        # visualization of funtions
        def display(self) -> None:
            print(f"Stats {self._grow_calls} grow, {self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(
        self,
        name,
        height,
        age
    ) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age
    # everytime you create a plant this one creates the stats system on it
        self._stats = self._Stats()

    @classmethod
    def anonymous(cls):
        return cls(name="Unknown plant", height=0, age=0)

    @staticmethod
    def is_older_than_year_days(age: int) -> bool:
        return age > 365

    def grow(self, cm) -> None:
        self._stats.increment_grow()
        self._height += cm

    def age_days(self, days) -> None:
        self._stats.increment_age()
        self._age += days

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        self._stats.increment_show()
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


class Seed(Flower):
    def __init__(
        self,
        name,
        height,
        age,
        color,
        bloomed: bool,
        n_seed: int
    ) -> None:

        super().__init__(name, height, age, color, bloomed)
        self._n_seed = n_seed

    def show(self) -> None:
        super().show()
        if self._bloomed:
            print(f" Seeds: {self._n_seed}")
        else:
            print(" Seeds: 0")


class Tree(Plant):
    class _Treestats(Plant._Stats):
        def __init__(self):
            super().__init__()
            self._shade_calls = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(
            self,
            name,
            height,
            age,
            trunk_diameter
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = float(trunk_diameter)
        self._stats = self._Treestats()

    def produce_shade(self) -> None:
        self._stats.increment_shade()
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


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


def display_statistics(plant_obj) -> None:
    print(f"[statistics for {plant_obj._name}]")
    plant_obj._stats.display()


def ft_plant_types() -> None:
    print("=== Check year-old")
    print(f" Is 30 days more than a year? -> "
          f"{Plant.is_older_than_year_days(30)}")
    print(f" Is 400 days more than a year? -> "
          f"{Plant.is_older_than_year_days(400)}")
    print("")
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red", False)
    rose.show()
    rose.bloom(True)
    display_statistics(rose)
    print("[asking the rose to bloom]")
    rose.grow(8)
    rose.show()
    rose.bloom(False)
    display_statistics(rose)
    print("")
    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    print("")
    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow", False, 42)
    sunflower.show()
    sunflower.bloom(True)
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age_days(20)
    sunflower.show()
    sunflower.bloom(False)
    display_statistics(sunflower)
    print("")
    print("=== Anonymous")
    anonymous_plant = Plant.anonymous()
    anonymous_plant.show()
    print("[statistics for Unknown plant]")
    anonymous_plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    ft_plant_types()
