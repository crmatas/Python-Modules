#! /usr/bin/env python3
def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existen/file")
    elif operation_number == 3:
        "garden" + 5
    else:
        print("Operation completed succesfully")


def test_error_types() -> None:

    print("testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print("testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    print("testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    print("testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as e:
        print(f"TypeError: {e}")
    print("testing operation 4...")
    garden_operations(4)
    print("testing all error in one try")
    try:
        garden_operations(4)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught error: {e}")


if __name__ == "__main__":
    print("=== Garden Error types Demo ===")
    test_error_types()
    print("")
    print("All tests complited - program didn't crash!")
