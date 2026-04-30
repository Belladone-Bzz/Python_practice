#!/usr/bin/env python3

"""Filename : data_processor.py

Date: 2026-04-06
Description: This program introduce to processing system.
It uses base processor architecture and demonstrate how different data types
can share common processing interfaces while maintaining their unique
characteristics. To do that, abstract methods were used.
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


def testing_numeric_processor() -> None:
    """Function to test numeric processor
    Try to validate invalid and valid numeric data.
    Test to ingest invalid data to check error raising.
    Ingest valid data and output it.
    """
    num_process: NumericProcessor = NumericProcessor()
    numeric_list: list[int] = [1, 2, 3, 4, 5]
    print("Testing Numeric Processor...")
    print("Trying to validate input '42': ", end="")
    validation: bool = num_process.validate(42)
    print(validation)
    print("Trying to validate input 'Hello': ", end="")
    validation = num_process.validate("Hello")
    print(validation)
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_process.ingest("foo")
    except ValueError:
        print("Got exception: Improper numeric data")
    print("Test valid ingestion with prior validation:")
    if num_process.validate(numeric_list) is True:
        print(f"Processing data: {numeric_list}")
        num_process.ingest(numeric_list)
        print("Extracting 3 values...")
        try:
            for i in range(0, 3):
                extracted_data: tuple[int, str] = num_process.output()
                print(f"Numeric value {extracted_data[0]}:"
                      f" {extracted_data[1]}")
        except Exception:
            print("Error extracting value: data ingested is empty")


def testing_text_processor() -> None:
    """Function to test text processor
    Try to validate invalid and valid str data.
    Test to ingest invalid data to check error raising.
    Ingest valid data and output it.
    """
    txt_process: TextProcessor = TextProcessor()
    text_list: list[str] = ["Hello", "Nexus", "World"]
    print("Testing Text Processor...")
    print("Trying to validate input '42': ", end="")
    validation: bool = txt_process.validate(42)
    print(validation)
    print("Trying to validate input '['Hello', 'Nexus', 'World']': ", end="")
    validation = txt_process.validate(text_list)
    print(validation)
    print("Test invalid ingestion of int '42' without prior validation:")
    try:
        txt_process.ingest(42)
    except ValueError:
        print("Got exception: Improper text data")
    print("Test valid ingestion with prior validation:")
    if txt_process.validate(text_list) is True:
        print(f"Processing data: {text_list}")
        txt_process.ingest(text_list)
        print("Extracting 1 value...")
        try:
            for i in range(0, 1):
                extracted_data: tuple[int, str] = txt_process.output()
                print(f"Text value {extracted_data[0]}: {extracted_data[1]}")
        except Exception:
            print("Error extracting value: data ingested is empty")


def testing_log_processor() -> None:
    """Function to test log processor
    Try to validate invalid and valid dict data.
    Test to ingest invalid data to check error raising.
    Ingest valid data and output it.
    """
    log_process: LogProcessor = LogProcessor()
    list_dict: list[dict[str, str]] = [{"log_level": "NOTICE",
                                        "log_message": "Connection to server"},
                                       {"log_level": "ERROR",
                                        "log_message": "Unauthorized access!!"}
                                       ]
    print("Testing Log Processor...")
    print("Trying to validate input 'Hello': ", end="")
    validation: bool = log_process.validate("Hello")
    print(validation)
    print("Trying to validate input '[{'log_level':'NOTICE',"
          "'log_message':'Connection to server'},"
          " {'log_level':'ERROR', 'log_message':"
          "'Unauthorized access!!'}]': ", end="")
    validation = log_process.validate(list_dict)
    print(validation)
    print("Test invalid ingestion of int '42' without prior validation:")
    try:
        log_process.ingest(42)
    except ValueError:
        print("Got exception: Improper dict data")
    print("Test valid ingestion with prior validation:")
    if log_process.validate(list_dict) is True:
        print(f"Processing data: {list_dict}")
        log_process.ingest(list_dict)
        print("Extracting 2 value...")
        try:
            for i in range(0, 2):
                extracted_data: tuple[int, str] = log_process.output()
                print(f"Log entry {extracted_data[0]}: {extracted_data[1]}")
        except Exception:
            print("Error extracting value: data ingested is empty")


def main() -> None:
    """Entry point of the program"""
    print("=== Code Nexus - Data Processor ===\n")
    testing_numeric_processor()
    print()
    testing_text_processor()
    print()
    testing_log_processor()


if __name__ == "__main__":
    main()
