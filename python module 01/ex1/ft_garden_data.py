#! usr/bin/env python3
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
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data()
