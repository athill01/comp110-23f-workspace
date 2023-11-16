"""File to define River class."""

__author__ = "730664291"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Class River."""
    
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of all bears and fish and drops bears older than 5 and drops fish older than 3."""
        new_bears: list[Bear] = []
        new_fish: list[Fish] = []
        for x in self.fish:
            if x.age <= 3:
                new_fish.append(x)
        for x in self.bears:
            if x.age <= 5:
                new_bears.append(x)
        self.bears = new_bears
        self.fish = new_fish
    
    def remove_fish(self, amount: int):
        """Removes the first {amount} fish in the Fish list."""
        for x in range(0, (amount)):
            self.fish.pop(0)

    def bears_eating(self):
        """Bears eat so many Fish, where those fish are removed from the river and Bears hunger_scores are increased."""
        for x in self.bears:
            if len(self.fish) >= 5:
                x.eat(3)
                self.remove_fish(3)
    
    def check_hunger(self):
        """Checks hunger of a bear and drops them if score is under 0."""
        alive_bears: list[Bear] = []
        for x in self.bears:
            if x.hunger_score < 0:
                pass
            else:
                alive_bears.append(x)
            self.bears = alive_bears
        
    def repopulate_fish(self):
        """Birth Rate of Fish."""
        for x in range(0, ((len(self.fish) // 2) * 4)):
            self.fish.append(Fish())
    
    def repopulate_bears(self):
        """Birth rate of Bears."""
        for x in range(0, (len(self.bears) // 2)):
            self.bears.append(Bear())
    
    def view_river(self):
        """Prints class River."""
        print(f"~~~ Day {self.day}: ~~~\n" + f"Fish population: {len(self.fish)}\n" + f"Bear population: {len(self.bears)}")
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        
    def one_river_week(self):
        """Runs the method one_river_day seven times."""
        for i in range(0, 7):
            self.one_river_day()
