from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[str] = []
        self._counter = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    # this method does not ovewrite the kids classes.
    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("Triying to validate input: '{}'")
        oldest = self._storage.pop(0)
        self._counter += 1
        return (self._counter, oldest)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        # It is a only number int or float
        if isinstance(data, (int, float)):
            return True
        # It is a list and all the elements are int or float.
        if (
            isinstance(data, list)
            and all(isinstance(x, (int, float)) for x in data)
        ):
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Got exception: Improper numeric data")
        # if is valid, woulf take each element and stores it as a string.
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
        # if it is just one element.
        else:
            self._storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        # It is a only number int or float
        if isinstance(data, (str)):
            return True
        # It is a list and all the elements are int or float.
        if isinstance(data, list) and all(isinstance(x, (str)) for x in data):
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Got exception: Improper text data")
        # if is valid, would take each element and stores it as a string.
        if isinstance(data, list):
            for item in data:
                self._storage.append(item)
        # if it is just one element.
        else:
            self._storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        # internal funtion to verify dict str-str.

        def validate_dict(data: Any) -> bool:
            if not isinstance(data, dict):
                return False
            return (
                isinstance(data, dict) and
                all(isinstance(k, str) and
                    isinstance(v, str) for k, v in data.items())
            )
        if validate_dict(data):
            return True
        if isinstance(data, list) and all(validate_dict(x) for x in data):
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("")
        if isinstance(data, list):
            for item in data:
                log_str = f"{item['log_level']}: {item['log_message']}"
                self._storage.append(log_str)
        else:
            log_str = f"{data['log_level']}: {data['log_message']}"
            self._storage.append(log_str)


def main() -> None:
    num_p = NumericProcessor()
    text_p = TextProcessor()
    log_p = LogProcessor()
    print("")
    print("Testing Numeric Processor...")
    print(" Trying to validate input '42':", num_p.validate(42))
    print(" Trying to validate input 'Hello':", num_p.validate("Hello"))
    print(" Test invalid ingestion of string 'foo' witout prior validation:")
    try:
        num_p.ingest("foo")  # type: ignore[arg-type]
    except ValueError as e:
        print(" ", e)
    print(" Processing data: [1, 2, 3, 4, 5]")
    num_p.ingest([1, 2, 3, 4, 5])
    print(" Extracting 3 values...")
    for i in range(3):
        extract = num_p.output()
        print(" Numeric value", f"{i}: {extract[1]}")
    print("")
    print(" Testing Text Processor")
    print(" Trying to validate input '42': ", text_p.validate(42))
    print(" Processing data: ['Hello', 'Nexus', 'World']")
    text_p.ingest(["Hello", "Nexus", "World"])
    print(" Extracting 1 value...")
    extract_t = text_p.output()
    print(" Text value 0:", extract_t[1])
    print("")
    print(" Testing Log Processor...")
    print(" Trying to validate input 'Hello':", log_p.validate("Hello"))
    print("Processing data: [{'log_level': 'NOTICE',"
          "'log_message': 'Connection to server'}, "
          "{'log_level': 'ERROR','log_message': 'Unauthorized access!!'}]")
    log_p.ingest([
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server"
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!"
        }
    ])
    print(" Extracting 2 values...")
    for i in range(2):
        extract_l = log_p.output()
        print(" Log entry", f"{i}, {extract_l[1]}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    main()
