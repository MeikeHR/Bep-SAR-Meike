import random
import math
import numpy as np
from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from SarUnit import Unit
from SarMissingPerson import MissingPerson
from SarEnvironment import Environment
import SarServer

import random


class SearchAndRescue(Model):

    def __init__(self,
                 width=90, height=60,
                 search_pattern='Parallel Sweep',
                 num_units=1,
                 search_radius=3,
                 max_current=1.5,
                 upper_current=0.5,
                 stamina=200,
                 profile=1,
                 tijd_melding=10,
                 # seed=205140,
                 seed=random.randint(0,50000)
                 ):
        super().__init__()

        self.search_pattern = search_pattern
        self.search_radius = search_radius
        self.num_units = num_units
        self.max_current = max_current
        self.upper_current = upper_current
        self.stamina = stamina
        self.profile = profile
        self.seed = seed
        self.tijd_melding_sec = tijd_melding * 60


        self.grid = MultiGrid(height, width, torus=False)
        self.schedule = SimultaneousActivation(self)

        """Create the environment, containing the values and directions of the currents"""
        for (contents, x, y) in self.grid.coord_iter():
            current_x, current_y = self.init_current(x, y)
            cell = Environment((x, y), current_x, current_y, False, self)
            self.grid.place_agent(cell, (x, y))

        """Place the missing person in the grid"""
        random.seed(self.seed)
        # pos_mp = (random.randrange(18, 24), random.randrange(5, 10))
        pos_mp = (random.randrange(30,50), random.randrange(30,60))

        missing_person = MissingPerson(999, pos_mp[0], pos_mp[1], self, self.profile)

        # self.schedule.add(missing_person)
        self.grid.place_agent(missing_person, pos_mp)

        self.A, self.B, self.C, self.D = self.zoekgebied()
        print(self.A, self.B, self.C, self.D)

        """Create the SAR Unit"""
        unit = Unit(1,self.A[0], self.A[1],self)
        self.schedule.add(unit)
        self.grid.place_agent(unit, (self.A[0], self.A[1]))

        self.datacollector = DataCollector(model_reporters={}, agent_reporters={})

        self.running = True

    def init_current(self, x, y):
        breedte = 6
        links = 17
        rechts = 24
        lengte = 10

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
        "Inital zoekgebied"
        A = [200,100]
        B = [900,100]
        C = [200,550]
        D = [900,550]

        "Invloed van tijd en stroming"
        a_tijd = int(((self.upper_current+(self.max_current/2)/2) * self.tijd_melding_sec)/(math.sqrt(2)))
        a_stroming = int(((self.upper_current - 0.41) / (0.77-0.41))*200)

        B[0] += a_tijd + a_stroming
        D[0] += a_tijd + a_stroming
        D[1] += a_tijd
        C[1] += a_tijd

        A[0] = int(A[0] / 20)
        A[1] = int(A[1] / 20)
        B[0] = int(B[0] / 20)
        B[1] = int(B[1] / 20)
        C[0] = int(C[0] / 20)
        C[1] = int(C[1] / 20)
        D[0] = int(D[0] / 20)
        D[1] = int(D[1] / 20)

        print(f"Zoekgebied - A: {A},B: {B}, C:{C}, D: {D}")
        return A,B,C,D


    def step(self):
        if self.running:
            self.schedule.step()
        self.datacollector.collect(self)
