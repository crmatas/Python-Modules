#! /usr/bin/env python3
class Plant:
    def __init__(
        self,
        name,
        height,
        age
    ) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name}: "
              f"{round(self.height, 1)}cm, {self.age} days old")


def ft_plant_factory() -> None:
    rose = Plant("rose", 25.0, 30)
    oak = Plant("oak", 200.0, 365)
    cactus = Plant("cactus", 5.0, 90)
    sunflower = Plant("sunflower", 80.0, 45)
    fern = Plant("fern", 15.0, 120)
    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    ft_plant_factory()
