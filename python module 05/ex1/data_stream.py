from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage = []
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
            raise IndexError("No data available")
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
        # if is valid, woulf take each element and stores it as a string.
        if isinstance(data, list):
            for item in data:
                self._storage.append(item)
        # if it is just one element.
        else:
            self._storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        # internal funtion to verify dict str-str.

        def validate_dict(d: Any) -> bool:
            if not isinstance(d, dict):
                return False
            return (
                isinstance(d, dict) and
                all(isinstance(k, str) and
                    isinstance(v, str) for k, v in d.items())
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
                self._storage.append(str(item))
        else:
            self._storage.append(str(data))


class DataStream():
    def __init__(self):
        # I do _processors because is an internal atribute.
        self._processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    break
            else:
                print(f"DataStream error - "
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        if not self._processors:
            print("No processor found, no data")
            return
        for processor in self._processors:
            name = processor.__class__.__name__
            total = processor._counter + len(processor._storage)
            remaining = len(processor._storage)
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


def main():
    print("=== Code Nexus - Data Stream ===")
    print("")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    print("")
    print("Registering Numeric Processor")
    print("")
    numeric = NumericProcessor()
    stream.register_processor(numeric)
    data = ["Hello world",
            [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
             'log_message': 'Tenet access! Use ssh instead'},
             {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
            42,
            ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data}")
    stream.process_stream(data)
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("")
    print("Registering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    print("== DataStream statistics ==")
    stream.process_stream(data)
    stream.print_processors_stats()
    print("")
    print("Consume some elements from the data processors:"
          " Numeric 3, Text 2, Log 1")
    print("== DataStream statistics ==")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    for _ in range(1):
        log.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()

# The _ on the for, is a python convention
# that means not interested on this value
