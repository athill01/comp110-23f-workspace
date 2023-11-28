"""Quiz 03 Practice."""

from __future__ import annotations

class ChristmasTreeFarm:
    
    plots = list[int]

    def __init__(self, plots: int, initial_planting: int):
        """Constructor."""
        self.plots: list[int] = []

        for x in range(0, initial_planting):
            self.plots.append(1)
        for x in range(0, (plots - initial_planting)):
            self.plots.append(0)

    def plant(self, plot_idx: int):
        self.plots[plot_idx] = 1

    def growth(self):
        for x in self.plots:
            if x != 0:
                x += 1
    
    def harvest(self, replant: bool) -> int:
        count = 0
        for i in self.plots:
            if self.plots[i] >= 5:
                count += 1
                if replant is True:
                    self.plots[i] = 1
                else:
                    self.plots[i] = 0
        return count

    def __add__(self, new_plot: ChristmasTreeFarm) -> ChristmasTreeFarm:
        trees: int = 0
        for x in self.plots:
            if x != 0:
                trees += 1
        for x in new_plot.plots:
            if x != 0:
                trees += 1
        return ChristmasTreeFarm((len(self.plots) + len(new_plot.plots)), trees)
    
class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int 
    prerequisites: list[str]

    def find_courses(courses: list[Course], prereq: str) -> list[str]:
        result = list[str]

        for x in courses:
            if x.level >= 400:
                for y in x.prerequisites:
                    if y == prereq:
                        result.append(x.name)
        
        return result
    
    def is_valid_course(self, prereq: str) -> bool:
        if self.level >= 400:
            for x in self.prerequisites:
                if x == prereq:
                    return True
        return False


