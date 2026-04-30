#!/usr/bin/env python3

"""Filename : data_stream.py

Date: 2026-04-08
Description: This program is an adaptative stream processing workflow
that can handle multiple data types simultaneously.
It introduces to polymorphic behavior.
"""
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Class DataProcessor inheriting from ABC.
    Abstract methods: validate() and ingest().
    Concrete method: output().
    """
    def __init__(self) -> None:
        self.data_processed: list[str] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Function template to validate type of data."""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Function template to ingest data."""
        pass

    def output(self) -> tuple[int, str]:
        """Concrete function to ouput ingested data."""
        if self.data_processed == []:
            raise Exception
        else:
            extracted_data: tuple[int, str] = \
                (self.rank, self.data_processed[0])
            self.rank += 1
            del self.data_processed[0]
            return extracted_data


class NumericProcessor(DataProcessor):
    """Class NumericProcessor inheriting from DataProcessor.
    Abstract methods: validate() and ingest().
    """
    def validate(self, data: Any) -> bool:
        """Overridden method to validate if data is numeric. Return True or
        False.
        """
        if isinstance(data, int | float):
            return True
        elif (isinstance(data, list) and
              all(isinstance(value, int | float) for
                  value in data)):
            return True
        else:
            return False

    def ingest(self, data: int | float | complex |
               list[int] | list[float] | list[complex] |
               list[int | float | complex]) -> None:
        """Overridden method to ingest numeric data and store it in
        list data_processed in DataProcessor. Check if the data is numeric
        and raise an error is it's not the case.
        """
        if (isinstance(data, list) and
                all(isinstance(value, int | float) for value in data)):
            self.data_processed.extend(list(map(str, data)))
        elif isinstance(data, int | float):
            self.data_processed.append(str(data))
        else:
            raise ValueError


class TextProcessor(DataProcessor):
    """Class TextProcessor inheriting from DataProcessor.
    Abstract methods: validate() and ingest().
    """
    def validate(self, data: Any) -> bool:
        """Overridden method to validate if data is str. Return True or
        False.
        """
        if isinstance(data, str):
            return True
        elif (isinstance(data, list) and
              all(isinstance(value, str) for value in data)):
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        """Overridden method to ingest str data and store it in
        list data_processed in DataProcessor. Check if the data is str
        and raise an error is it's not the case.
        """
        if self.validate(data) is False:
            raise ValueError
        else:
            if (isinstance(data, list) and
                    all(isinstance(value, str) for value in data)):
                self.data_processed.extend(data)
            elif isinstance(data, str):
                self.data_processed.append(data)


class LogProcessor(DataProcessor):
    """Class LogProcessor inheriting from DataProcessor.
    Abstract methods: validate() and ingest().
    """
    def validate(self, data: Any) -> bool:
        """Overridden method to validate if data is dict type. Return True or
        False.
        """
        if isinstance(data, dict) is True:
            for key in data.keys():
                if "log_level" not in key and "log_message" not in key:
                    return False
            return True
        elif isinstance(data, list) is True:
            for dictionnary in data:
                if isinstance(dictionnary, dict) is False:
                    return False
                for key in dictionnary.keys():
                    if "log_level" not in key and "log_message" not in key:
                        return False
            return True
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        """Overridden method to ingest dict data and store it in
        list data_processed in DataProcessor. Check if the data is dict
        and raise an error is it's not the case.
        """
        if self.validate(data) is False:
            raise ValueError
        else:
            data_list = data if isinstance(data, list) else [data]
            for item in data_list:
                self.data_processed.append(f"{item["log_level"]}:"
                                           f" {item["log_message"]}")


class DataStream:
    """Class DataStream
    Concrete methods: register_processor(), process_stream() and
    print_processor_stats()
    """
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """Method to register a new data processor to process
        the data stream
        """
        self.processors.append(proc)
        print(f"Registering {proc.__class__.__name__}")

    def process_stream(self, stream: list[Any]) -> None:
        """Method to analyze each element of the list received as parameter
        and send it to the appropriate registered data processor"""
        if stream == []:
            print("Error - empty stream")
        for element in stream:
            for processor in self.processors:
                if processor.validate(element) is True:
                    processor.ingest(element)
                    break
            else:
                print("DataStream error - Can't process element in stream: "
                      f"{element}")

    def print_processors_stats(self) -> None:
        """Method to print processors stats"""
        initial_length: int = 0
        print("\n== DataStream statistics ==")
        if self.processors == []:
            print("No processor found, no data\n")
        for processor in self.processors:
            initial_length = (len(processor.data_processed) + processor.rank)
            print(f"{processor.__class__.__name__}: total {initial_length} "
                  f"items processed, remaining {len(processor.data_processed)}"
                  " on processor")


def main() -> None:
    """Entry point of the program"""
    stream: list[Any] = ["Hello world", [3.14, -1, 2.71],
                         [{"log_level": "WARNING",
                           "log_message": "Telnet access! Use ssh instead"},
                          {"log_level": "INFO",
                           "log_message": "User wil is connected"}],
                         42, ["Hi", "five"]]
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    data_stream: DataStream = DataStream()
    data_stream.print_processors_stats()
    data_stream.register_processor(NumericProcessor())
    print(f"Send first batch of data on stream: {stream}")
    data_stream.process_stream(stream)
    data_stream.print_processors_stats()
    print()
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())
    print("Send the same batch again")
    data_stream.process_stream(stream)
    data_stream.print_processors_stats()
    print("\nConsume some elements from the data processors: Numeric 3, Text 2"
          ", Log 1")
    for _ in range(0, 3):
        data_stream.processors[0].output()
    for _ in range(0, 2):
        data_stream.processors[1].output()
    data_stream.processors[2].output()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
