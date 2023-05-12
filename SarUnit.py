import random
import numpy as np
import math

from mesa import Agent
from SarMissingPerson import MissingPerson
from SarEnvironment import Environment


class Unit(Agent):

    def __init__(self, unique_id, x, y, model, seed):
        super().__init__(unique_id, model)
        self.x = x * 20
        self.y = y * 20

        self.x_cell, self.y_cell = self.xy_to_cell()

        self.speed = 12.86 * 2 / 3

        self.tick = 0

        "Parallel sweep variables"
        self.tick_pattern = 0
        self.lang_kort_ps = "LANG"
        self.richting_ps = 'RECHTS'

        "Expanding square variables"
        self.factor_ES = 1
        self.baan = "EERSTE"

        "Sector search variables"
        self.hoek = 60
        self.eerste = "JA"
        self.baan_SS = "KORT"

        "Random search variables"
        random_x = random.randrange(self.model.A[0], self.model.B[0])
        random_y = random.randrange(self.model.A[1], self.model.C[1])
        self.new_point = (random_x, random_y)

        self.reached_middle = False

    def xy_to_cell(self):
        x = int(self.x/20)
        y = int(self.y/20)
        return x, y

    def move_search(self):
        pos_mp = self.look(self.model.search_radius)
        if pos_mp != ():
            self.move_to(pos_mp)
        else:
            if self.model.search_pattern == "Parallel Sweep":
                self.move_ps()
            elif self.model.search_pattern == 'Expanding Square':
                self.move_es()
            elif self.model.search_pattern == 'Sector Search':
                self.move_ss()
            elif self.model.search_pattern == 'Random Search':
                self.move_rs()

    def move_current(self):
        for obj in self.model.grid.get_cell_list_contents(self.xy_to_cell()):
            if isinstance(obj, Environment):
                current_y = obj.current_y
                current_x = obj.current_x

        self.y += current_y
        self.x += current_x

    """The following functions will define the way of movement through the water due to the chosen search pattern."""

    def move_ps(self):
        """Defines the Parallel Sweep search pattern"""
        # print(f'Moving due to PS pattern')
        self.tick_pattern += 1
        track_spacing = self.model.search_radius * 2

        ticks_lang = int((((self.model.B[0] - self.model.A[0])*20) / self.speed))
        ticks_kort = int(track_spacing*20 / self.speed)
        print(f'With ticks: {self.tick_pattern}, max ticks lang: {ticks_lang}, kort: {ticks_kort}, en baan: {self.lang_kort_ps}')

        if self.lang_kort_ps == "LANG":
            "Is de boot bij het eind van de slag?"
            if self.tick_pattern == ticks_lang:
                self.tick_pattern = 0
                self.lang_kort_ps = "KORT"
                if self.richting_ps == "RECHTS":
                    self.x += self.speed
                    self.richting_ps = "LINKS"
                else:
                    self.x -= self.speed
                    self.richting_ps = "RECHTS"

            else:
                if self.richting_ps == "RECHTS":
                    self.x += self.speed
                else:
                    self.x -= self.speed

        else:
            "Is de boot bij het eind van de slag?"
            if self.tick_pattern == ticks_kort:
                self.lang_kort_ps = "LANG"
                self.y += self.speed
                self.tick_pattern = 0
            else:
                self.y += self.speed

    def move_es(self):
        """Defines the Expanding Square search pattern"""
        afstand = self.model.search_radius * 20

        if not self.reached_middle:
            self.go_to_middle()
        else:
            self.tick_pattern += 1
            ticks = int(afstand * self.factor_ES / self.speed)

            if self.tick_pattern == ticks:
                if self.baan == "EERSTE":
                    self.baan = "TWEEDE"
                    self.tick_pattern = 0
                    if self.factor_ES % 2 == 0:
                        self.x += self.speed
                    else:
                        self.x -= self.speed
                else:
                    self.baan = "EERSTE"
                    self.tick_pattern = 0
                    self.factor_ES += 1
                    if self.factor_ES % 2 == 0:
                        self.y -= self.speed
                    else:
                        self.y += self.speed
            else:
                if self.baan == "EERSTE":
                    if self.factor_ES % 2 == 0:
                        self.x += self.speed
                    else:
                        self.x -= self.speed
                else:
                    if self.factor_ES % 2 == 0:
                        self.y -= self.speed
                    else:
                        self.y += self.speed

    def move_ss(self):
        """Defines the Sector Search search pattern"""
        v_x = self.speed * math.cos(math.radians(self.hoek))
        v_y = self.speed * math.sin(math.radians(self.hoek))

        hoogte_zoekgebied = (self.model.D[1] - self.model.B[1]) * 20

        lange_kant = hoogte_zoekgebied / math.sin(math.radians(60))
        korte_kant = hoogte_zoekgebied / math.tan(math.radians(60))

        ticks_kort = int(korte_kant / self.speed)  # (berekenen)
        ticks_lang = int(lange_kant / self.speed)  # (berekenen)

        if not self.reached_middle:
            self.go_to_middle()
        else:
            self.tick_pattern += 1
            if self.eerste == "JA":
                if self.tick_pattern == ticks_kort:
                    self.eerste = "NEE"
                    self.x += v_x
                    self.y += v_y
                    self.tick_pattern = 0
                    self.hoek += 120
                else:
                    self.x += v_x
                    self.y += v_y
            else:
                if self.baan_SS == "KORT":
                    if self.tick_pattern == ticks_kort:
                        self.x += v_x
                        self.y += v_y
                        self.tick_pattern = 0
                        self.hoek += 120
                        self.baan_SS = "LANG"
                    else:
                        self.x += v_x
                        self.y += v_y
                else:
                    if self.tick_pattern == ticks_lang:
                        self.x += v_x
                        self.y += v_y
                        self.tick_pattern = 0
                        self.hoek += 120
                        self.baan_SS = "KORT"
                    else:
                        self.x += v_x
                        self.y += v_y

    def move_rs(self):
        """Defines the Random Search pattern"""
        print(f'RS zoekpatroon: cell: x,y = {self.new_point} en zelf: x,y = {self.xy_to_cell()}')

        self.move_to(self.new_point)

        if self.new_point in self.model.grid.get_neighborhood((self.x_cell, self.y_cell), moore=True,
                                                              include_center=False, radius=1):
            random_x = random.randrange(self.model.A[0], self.model.B[0])
            random_y = random.randrange(self.model.A[1], self.model.C[1])
            self.new_point = (random_x, random_y)

    def go_to_middle(self):
        midden_x = int((self.model.B[0] + self.model.A[0]) / 2)
        midden_y = int((self.model.D[1] + self.model.B[1]) / 2)
        midden_zoekgebied = (midden_x, midden_y)

        self.move_to(midden_zoekgebied)
        if midden_zoekgebied in self.model.grid.get_neighborhood((self.x_cell, self.y_cell), moore=True,
                                                                 include_center=False, radius=1):
            self.reached_middle = True

    def look(self, radius):
        """Does the searching unit have the person in its search radius,
        will they spot them according to assigned finding probability, determined by wind and wave height."""
        field = self.model.grid.get_neighborhood(self.xy_to_cell(), moore=True, include_center=False, radius=radius)
        print(f'Unit is now at: {self.xy_to_cell()}')
        agents_in_range = {}
        for cell in field:
            agents = self.model.grid.get_cell_list_contents(cell)
            for agent in agents:
                if isinstance(agent, Environment):
                    agents_in_range["env"] = cell
                if isinstance(agent, MissingPerson):
                    agents_in_range["mp"] = cell

        if any(agent_key == "mp" for agent_key in agents_in_range.keys()):
            position_missing_person = agents_in_range["mp"]
            chance = random.randrange(0, 100)
            print(f'{chance} < of > {self.model.finding_prob}')
            if chance < self.model.finding_prob:
                print(f'Unit found agent at {position_missing_person}, now')
                return position_missing_person
        return ()

    def move_to(self, cell):
        """With a given position, try moving there (shortest path).
        If the position is one of the agents neighbors, stop the model (running = False)"""
        position = self.xy_to_cell()
        x, y = position
        x_mp, y_mp = cell

        dx = np.absolute(x_mp - x)
        dy = np.absolute(y_mp - y)

        if dy > dx:
            if (y_mp - y) > 0:
                self.y += self.speed
            else:
                self.y -= self.speed

            agents = self.model.grid.get_cell_list_contents((self.xy_to_cell()))
            if any(isinstance(agent, MissingPerson) for agent in agents):
                print(f'Person was found at {self.tick}')
                self.model.found = True
                self.model.running = False

        elif dx > dy:
            if (x_mp - x) > 0:
                self.x += self.speed
            else:
                self.x -= self.speed
            agents = self.model.grid.get_cell_list_contents((self.xy_to_cell()))
            if any(isinstance(agent, MissingPerson) for agent in agents):
                self.model.running = False
                print(f'Person was found at {self.tick}')
                self.model.found = True

        else:
            if x_mp - x > 0:
                self.x += self.speed
            else:
                self.x -= self.speed
            if y_mp - y > 0:
                self.y += self.speed
            else:
                self.y -= self.speed
            agents = self.model.grid.get_cell_list_contents((self.xy_to_cell()))
            if any(isinstance(agent, MissingPerson) for agent in agents):
                self.model.running = False
                print(f'Person was found at {self.tick}')
                self.model.found = True

    def step(self):
        self.tick += 1
        self.x_cell, self.y_cell = self.xy_to_cell()
        # tijd_test = 0
        tijd_test = self.model.tijd_melding_sec
        print(f'agent now moving?: {self.tick} > {tijd_test}')
        if self.tick > tijd_test:
            print(f'Yes, unit is moving')
            cell_new = self.xy_to_cell()
            loc = self.model.grid.get_cell_list_contents(cell_new)
            for obj in loc:
                if isinstance(obj, Environment):
                    obj.path = True

            """How does the unit move according to the search state (still looking or moving to a position)"""
            self.move_search()
            """How does the unit move due to the current"""
            # self.move_current()

            x, y = self.xy_to_cell()
            print(f'max x: {self.model.width}, max y: {self.model.height}')
            print(f'location of unit {x, y}')
            if x < 0 or x >= self.model.width or y < 0 or y >= self.model.height:
                self.model.running = False
                print(f'Unit left the field at {x}, {y}')
            else:
                self.model.grid.move_agent(self, (x, y))
