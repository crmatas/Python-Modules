#! usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(test_data: str) -> None:
    print(f"Input data is '{test_data}'")

    try:
        result = input_temperature(test_data)
        print(f"Temperature now is {result}ºC")
    except ValueError as e:
        # as e, Captures the exact error messege of python
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature("25")
    test_temperature("abd")
    print("All tests complited - program didn't crash!")
