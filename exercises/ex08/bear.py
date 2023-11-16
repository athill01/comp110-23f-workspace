"""File to define Bear class."""

__author__ = "730664291"


class Bear:
    """Bear Class."""
    
    age: int
    hunger_score: int

    def __init__(self, age: int = 0, hunger_score: int = 0):
        """Constructor."""
        self.age = age
        self.hunger_score = hunger_score
        
    def one_day(self):
        """Increase age and decrease hunger_score for every day."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """After eating, the hunger_score will increase by the number of fish consumed."""
        self.hunger_score += num_fish