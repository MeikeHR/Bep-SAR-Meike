import random

from mesa import Model
from mesa.time import SimultaneousActivation
# from mesa.time import RandomActivation
from mesa.space import SingleGrid
# from mesa.datacollection import DataCollector

from SarAgent import Unit
from SarAgent import MissingPerson

class SearchAndRescue(Model):

    def __init__(self, width=30, height=20, search_pattern_slider='Parallel Sweep', num_units=1):
        super().__init__()

        self.search_pattern_slider = search_pattern_slider
        self.num_units = num_units

        self.grid = SingleGrid(height, width, torus=False)

        self.schedule = SimultaneousActivation(self)

        for i in range(num_units):
            a = Unit(i, (i*10, i*10), self)
            self.schedule.add(a)
            self.grid.place_agent(a, (i*10, i*10))

        pos_mp = (random.randrange(self.grid.width), random.randrange(self.grid.height))
        missing_person = MissingPerson(999, pos_mp, self, 100)
        self.schedule.add(missing_person)
        self.grid.place_agent(missing_person, pos_mp)

        self.running = True

    def step(self):
        self.schedule.step()
