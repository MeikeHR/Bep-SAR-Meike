import random

from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid

from SarAgent import Unit
from SarAgent import MissingPerson
from SarEnvironment import Environment


class SearchAndRescue(Model):

    def __init__(self,
                 width=90, height=60,
                 search_pattern='Parallel Sweep',
                 num_units=1,
                 search_radius=3,
                 max_current=10):
        super().__init__()

        self.search_pattern = search_pattern
        self.search_radius = search_radius
        self.num_units = num_units
        self.max_current = max_current

        self.grid = MultiGrid(height, width, torus=False)

        # rip current is 1/5 of the model width and has a left and right boundary in the middle of the grid
        rc_width = self.grid.width / 5
        left_rc = self.grid.width / 2 - (rc_width / 2)
        right_rc = self.grid.width / 2 + (rc_width / 2)
        # current is 2/3 of the model height
        length_rc = self.grid.height * 2 / 3

        # Create the environment, containing the values and directions of the currents
        for (contents, x, y) in self.grid.coord_iter():
            if right_rc > x > left_rc and y < length_rc:
                if (x - left_rc) <= rc_width/2:
                    current = (x - left_rc) * self.max_current / (width / 2)
                    cell = Environment((x, y), current, self)
                    self.grid.place_agent(cell, (x, y))
                else:
                    current = (right_rc - x) * self.max_current / (width / 2)
                    cell = Environment((x, y), current, self)
                    self.grid.place_agent(cell, (x, y))
            else:
                current = 0
                cell = Environment((x, y), current, self)
                self.grid.place_agent(cell, (x, y))

        self.schedule = SimultaneousActivation(self)

        for i in range(num_units):
            a = Unit(i, (i*10, i*10), self)
            self.schedule.add(a)
            self.grid.place_agent(a, (i*10, i*10))

        pos_mp = (random.randrange(0, self.grid.width), random.randrange(0, int(self.grid.height / 3)))
        missing_person = MissingPerson(999, pos_mp, self, 100)
        self.schedule.add(missing_person)
        self.grid.place_agent(missing_person, pos_mp)

        self.running = True

    def step(self):
        if self.running:
            self.schedule.step()
