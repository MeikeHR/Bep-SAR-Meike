import random

from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid

from SarAgent import Unit
from SarAgent import MissingPerson
from SarEnvironment import Environment
import SarServer


class SearchAndRescue(Model):

    def __init__(self,
                 width=90, height=60,
                 search_pattern='Parallel Sweep',
                 num_units=1,
                 search_radius=3,
                 max_current=10,
                 upper_current=2):
        super().__init__()

        self.search_pattern = search_pattern
        self.search_radius = search_radius
        self.num_units = num_units
        self.max_current = max_current
        self.upper_current = upper_current

        self.grid = MultiGrid(height, width, torus=False)
        self.schedule = SimultaneousActivation(self)

        # Create the environment, containing the values and directions of the currents
        for (contents, x, y) in self.grid.coord_iter():
            current_x, current_y = self.init_current(x, y)
            cell = Environment((x, y), current_x, current_y, False, self)
            self.grid.place_agent(cell, (x, y))

        # Create the search and rescue units
        for i in range(self.num_units):
            a = Unit(i, i*10, i*10, self)
            self.schedule.add(a)
            self.grid.place_agent(a, (i*10, i*10))

        # pos_mp = (random.randrange(0, self.grid.width), random.randrange(0, int(self.grid.height / 3)))
        pos_mp = (85, 50)
        missing_person = MissingPerson(999, pos_mp[0], pos_mp[1], self, 100)
        self.schedule.add(missing_person)
        self.grid.place_agent(missing_person, pos_mp)

        self.running = True

    def init_current(self, x, y):
        rc_width = self.grid.width / 5
        left_rc = self.grid.width / 2 - (rc_width / 2)
        right_rc = self.grid.width / 2 + (rc_width / 2)
        length_rc = self.grid.height / 3

        current_x = 0
        current_y = 0

        # Fill in the values due to the rip current
        if right_rc > x > left_rc and y < length_rc:
            if (x - left_rc) <= rc_width / 2:
                current_x += 0
                current_y += (x - left_rc) * self.max_current / (rc_width / 2)
            else:
                current_x += 0
                current_y += (right_rc - x) * self.max_current / (rc_width / 2)
        else:
            current_x += 0
            current_y += 0

        # Fill in the values due to the upper current
        if y >= length_rc:
            current_x += self.upper_current

        return current_x, current_y

    def step(self):
        if self.running:
            self.schedule.step()
