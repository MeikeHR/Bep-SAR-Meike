import random

from mesa import Model
from mesa.time import SimultaneousActivation
# from mesa.time import RandomActivation
from mesa.space import SingleGrid
# from mesa.datacollection import DataCollector

from SarAgent import Unit
from SarAgent import MissingPerson
# from SarEnvironment import Environment

class SearchAndRescue(Model):

    def __init__(self, width=90, height=60, search_pattern_slider='Parallel Sweep', num_units=1, search_radius=3, max_current=10):
        super().__init__()

        self.search_pattern_slider = search_pattern_slider
        self.search_radius = search_radius
        self.num_units = num_units
        # self.max_current = max_current

        self.grid = SingleGrid(height, width, torus=False)

        # elke grid cell een current waarde geven, obv max_current

        # for (contents, x, y) in self.grid.coord_iter():
        #     cell =
        #     pass


        self.schedule = SimultaneousActivation(self)

        for i in range(num_units):
            a = Unit(i, (i*10, i*10), self)
            self.schedule.add(a)
            self.grid.place_agent(a, (i*10, i*10))

        pos_mp = (random.randrange(0, self.grid.width), random.randrange(self.grid.height/5, self.grid.height/2))
        missing_person = MissingPerson(999, pos_mp, self, 100)
        self.schedule.add(missing_person)
        self.grid.place_agent(missing_person, pos_mp)

        self.running = True

    def step(self):
        if self.running:
            self.schedule.step()
