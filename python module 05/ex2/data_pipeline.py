from abc import ABC, abstractmethod
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[Any] = []
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

        def validate_dict(data: Any) -> bool:
            if not isinstance(data, dict):
                return False
            return (isinstance(data, dict)
                    and all(isinstance(k, str)
                    and isinstance(v, str) for k, v in data.items())
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


class DataStream():
    def __init__(self) -> None:
        # I do _processors because is an internal atribute.
        self._processors: list[DataProcessor] = []

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if nb < 0:
            print("Error. nb can't be negative")
            return
        for processor in self._processors:
            data_list: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    data_list.append(processor.output())
                except IndexError:
                    break
            plugin.process_output(data_list)


# Comma-Separated Values
class CsvExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        array: list[str] = [item for _, item in data]
        output = ", ".join(array)
        print(output)


# JavaScript Object Notation
class JsonExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        dictionary: dict[str, str] = {f"item_{index}": item
                                      for index, item in data}
        output = f"{dictionary}"
        print(output)


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("")
    print("Initialize Data Stream...")
    print("")
    print("== DataStream statistics ==")
    stream = DataStream()
    stream.print_processors_stats()
    print("")
    print("Registering Processor")
    print("")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)
    data = ["Hello world",
            [3.14, -1, 2.71],
            [
                {
                    'log_level': 'WARNING',
                    'log_message': 'Tenet access! Use ssh instead'
                },
                {
                    'log_level': 'INFO',
                    'log_message': 'User wil is connected'
                }
            ],
            42,
            ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data}")
    stream.process_stream(data)
    print("")
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("")
    print("Send 3 processed data from each processor to a CVS plugin:")
    stream.output_pipeline(3, CsvExportPlugin())
    data2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE', 'log_message':
             'Certificateexpires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello']
    print("")
    print("== DataStream statistics ==")
    stream.print_processors_stats()  # this one is repeated on the sample.
    print("")
    print(f"Send the another batch of data: {data2}")
    stream.process_stream(data2)
    print("")
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("")
    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JsonExportPlugin())
    print("")
    print("== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
