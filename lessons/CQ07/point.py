"""Defining Point Class."""

from __future__ import annotations

__author__ = "730664291"


class Point:
    """This is my class to represent point!"""

    # attributes
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int):
        """Updating an already established point by scaling by factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creating a new point from previous point."""
        new_scale: Point = Point(self.x * factor, self.y * factor)
        return new_scale
    
    def __str__(self) -> str:
        """Convert point to string."""
        my_string: str = f"x: {self.x}; y: {self.y}"
        return my_string
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiply point by factor to create a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Add point by factor to create a new point."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point