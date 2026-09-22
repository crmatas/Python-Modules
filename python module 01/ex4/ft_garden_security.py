#! /usr/bin/env python3
class Plant:
    def __init__(
        self,
        name,
        height,
        age
    ) -> None:
        self._name = name.capitalize()

        if height >= 0:
            self._height = height
        else:
            print("Error, height cant be negative")
            print("Height update rejected")
            self._height = 0

        if age >= 0:
            self._age = age
        else:
            print("Error, age can't be negative")
            print("Age update rejected")
            self._age = 0

    def set_height(self, height) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm")
        else:
            print(f"{self._name}: Error, height cant be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: "
              f"{round(self._height, 1)}cm, {self._age} days old")


def ft_garden_security() -> None:
    rose = Plant("rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-23)
    rose.show
    rose.set_age(-30)
    rose.show
    print("")
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    print("=== Garden Security System  ===")
    ft_garden_security()
