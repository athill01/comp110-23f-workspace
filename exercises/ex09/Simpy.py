"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730664291"


class Simpy:
    """Defining class Simpy."""

    values: list[float]

    def __init__(self, input: list[float]):
        """Constructor."""
        self.values = input
    
    def __str__(self) -> str:
        """Converts class instance to string."""
        return f"Simpy({self.values})"
    
    def fill(self, value: float, num_values: int) -> None:
        """Fills in self.values list with one number (value) so many times (num_values)."""
        self.values = []
        for x in range(0, num_values):
            self.values.append(value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Starts at a point in self.values and adds (step) until it reaches stop."""
        assert step != 0.0
        self.values = []
        value = start
        if step > 0.0:
            while value < stop:
                self.values.append(value)
                value += step
        else:
            while value > stop:
                self.values.append(value)
                value += step

    def sum(self) -> float:
        """Sums up all of self.values and returns a float."""
        result: float = 0.0
        for x in self.values:
            result += x
        return result
    
    def __add__(self, value: Union[float, Simpy]) -> Simpy:
        """Adds to self.values by the indexes in Simpy or all by the same float and returns a new instance of Simpy."""
        new_simpy: Simpy = Simpy([])
        if isinstance(value, Simpy):
            assert len(self.values) == len(value.values)
            for i in range(0, len(self.values)):
                new_simpy.values.append(self.values[i] + value.values[i])
        else:
            for x in range(0, len(self.values)):
                new_simpy.values.append(self.values[x] + value)
        return new_simpy
    
    def __pow__(self, value: Union[float, Simpy]) -> Simpy:
        """Exponentiates self.values by the respective indexes of other Simpy or all by the same float and returns a new instance of Simpy."""
        new_simpy: Simpy = Simpy([])
        if isinstance(value, Simpy):
            assert len(self.values) == len(value.values)
            for i in range(0, len(self.values)):
                new_simpy.values.append(self.values[i] ** value.values[i])
        else:
            for x in range(0, len(self.values)):
                new_simpy.values.append(self.values[x] ** value)
        return new_simpy

    def __eq__(self, value: Union[float, Simpy]) -> list[bool]:
        """Returns a list of booleans depending on if the matched indexes of self.values and value.values match or self.values matches given float."""
        return_list: list[bool] = []
        if isinstance(value, Simpy):
            assert len(self.values) == len(value.values)
            for x in range(0, len(self.values)):
                if self.values[x] == value.values[x]:
                    return_list.append(True)
                else:
                    return_list.append(False)
        else:
            for x in range(0, len(self.values)):
                if self.values[x] == value:
                    return_list.append(True)
                else:
                    return_list.append(False)
        return return_list
    
    def __gt__(self, value: Union[float, Simpy]) -> list[bool]:
        """Returns a list of booleans depending on if self.values matching indices of value.values is greater than or greater than given float."""
        return_list: list[bool] = []
        if isinstance(value, Simpy):
            assert len(self.values) == len(value.values)
            for x in range(0, len(self.values)):
                if self.values[x] > value.values[x]:
                    return_list.append(True)
                else:
                    return_list.append(False)
        else:
            for x in range(0, len(self.values)):
                if self.values[x] > value:
                    return_list.append(True)
                else:
                    return_list.append(False)
        return return_list
    
    def __getitem__(self, value: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returns requested index of self.values or creates a new Simpy consisting of matched indices of self.values where value.values index is True."""
        if isinstance(value, int):
            item = self.values[value]
            return item
        else:
            new_simpy: Simpy = Simpy([])
            for x in range(0, len(self.values)):
                if value[x] is True:
                    new_simpy.values.append(self.values[x])
            return new_simpy
    
    