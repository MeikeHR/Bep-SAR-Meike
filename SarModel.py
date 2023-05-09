import math

from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from SarUnit import Unit
from SarMissingPerson import MissingPerson
from SarEnvironment import Environment

import random


class SearchAndRescue(Model):

    def __init__(self,
                 width=100, height=60,
                 search_pattern='Parallel Sweep',
                 search_radius=125,
                 max_current=1.5,
                 upper_current=0.5,
                 wind=8,
                 profile=1,
                 swimming_ability="GOED",
                 tijd_melding=5,
                 wind_richting='ZUID',
                 seed=100,
                 # seed=random.randint(0,50000)
                 ):
        super().__init__()

        self.width = width
        self.height = height

        self.search_pattern = search_pattern
        self.max_current = max_current
        self.upper_current = upper_current
        self.wind = wind
        self.wind_richting = wind_richting

        self.search_radius = int(search_radius / 20)
        self.tijd_melding_sec = tijd_melding * 60
        self.finding_prob = self.finding_probability()
        self.A, self.B, self.C, self.D = self.zoekgebied()

        self.grid = MultiGrid(width, height, torus=False)
        self.schedule = SimultaneousActivation(self)

        random.seed(seed)

        """Create the environment, containing the values and directions of the currents"""
        for (contents, x, y) in self.grid.coord_iter():
            current_x, current_y = self.init_current(x, y)
            cell = Environment((x, y), current_x, current_y, False, self)
            self.grid.place_agent(cell, (x, y))

        """Place the missing person in the grid"""
        pos_mp = (random.randrange(15, 45), random.randrange(5, 15))
        # pos_mp = (random.randrange(30, 60), random.randrange(30, 50))
        swimming_speed = 0.4
        stamina = random.randrange (1800, 3600)
        self.stamina = stamina
        missing_person = MissingPerson(999, pos_mp[0], pos_mp[1], self, stamina, profile,
                                       swimming_speed, swimming_ability, seed)
        self.pos_mp_begin = pos_mp
        self.schedule.add(missing_person)
        self.grid.place_agent(missing_person, pos_mp)

        """Create the SAR Unit"""
        unit = Unit(1, self.A[0], self.A[1], self, seed)
        self.schedule.add(unit)
        print(f'schedule: {self.schedule}')
        self.grid.place_agent(unit, (self.A[0], self.A[1]))

        self.datacollector = DataCollector(model_reporters={}, agent_reporters={})

        self.step_counter = 0
        self.running = True

    def finding_probability(self):
        if self.wind == 8.0:
            return 90
        elif self.wind == 9.0:
            return 75
        else:
            return 60

    def init_current(self, x, y):
        breedte = 6
        links = 17
        rechts = 24
        lengte = 5

        current_x = 0
        current_y = 0

        """Rip current values"""
        if rechts > x > links and y < lengte:
            if (x - links) <= breedte / 2:
                current_x += 0
                current_y += (x - links) * self.max_current / (breedte / 2)
            else:
                current_x += 0
                current_y += (rechts - x) * self.max_current / (breedte / 2)
        else:
            current_x += 0
            current_y += 0

        """Upper current values"""
        if y >= lengte:
            current_x += self.upper_current

        return current_x, current_y

    def zoekgebied(self):
        "Initiele zoekgebied"
        A = [200, 60]
        B = [1300, 60]
        C = [200, 720]
        D = [1300, 720]

        "Invloed van tijd en stroming"
        dx = int(self.tijd_melding_sec * self.upper_current)
        dy = dx * 600 / 1000

        B[0] += dx
        D[0] += dx
        D[1] += dy
        C[1] += dy

        A[0] = int(A[0] / 20)
        A[1] = int(A[1] / 20)
        B[0] = int(B[0] / 20)
        B[1] = int(B[1] / 20)
        C[0] = int(C[0] / 20)
        C[1] = int(C[1] / 20)
        D[0] = int(D[0] / 20)
        D[1] = int(D[1] / 20)

        print(f"Zoekgebied - A: {A}, B: {B}, C:{C}, D: {D}")
        return A, B, C, D

    def step(self):
        self.step_counter += 1
        if self.running:
            self.schedule.step()
        else:
            print(f'tijd: {self.step_counter}')
            print(f'stamina eind: {[agent.stamina for agent in self.schedule.agents if isinstance(agent, MissingPerson)]}')
        self.datacollector.collect(self)
