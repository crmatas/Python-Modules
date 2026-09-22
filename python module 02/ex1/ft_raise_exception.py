#! /usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}ºC is too cold for plants (min 0ºC)")
    if temp > 40:
        raise ValueError(f"{temp}ºC is too hot for plants (max 40ºC)")
    return int(temp)


def test_temperature(test_data: str) -> None:
    print(f"Input data is '{test_data}'")

    try:
        result = input_temperature(test_data)
        print(f"Temperature now is {result}ºC")
    except ValueError as e:
        # as e, Captures the exact error messege of python
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print("")
    test_temperature("25")
    print("")
    test_temperature("abd")
    print("")
    test_temperature("100")
    print("")
    test_temperature("-50")
    print("")
    print("All tests complited - program didn't crash!")
