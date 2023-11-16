"""File to define Fish class."""

__author__ = "730664291"


class Fish:
    """Fish Class."""
    
    age: int 

    def __init__(self, age: int = 0) -> None:
        """Constructor."""
        self.age = age
        
    def one_day(self) -> None:
        """Age of fish increases by one after a day."""
        self.age += 1