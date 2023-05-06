import random
import numpy as np
import math

from mesa import Agent
from SarEnvironment import Environment


class MissingPerson(Agent):
    def __init__(self, unique_id, x, y, model,stamina, profile, swimming_speed):
        super().__init__(unique_id, model)
        self.stamina = stamina
        self.profile = profile
        self.swimming_speed = swimming_speed
        self.wind = self.model.wind
        self.wind_richting = self.model.wind_richting

        self.x = x*20
        self.y = y*20

        self.tick = 0

    def xy_to_cell(self):
        x = int(self.x/20)
        y = int(self.y/20)
        return x, y

    def move_current(self):
        """Defines the influence of the current of the cell the person is in, on its position"""
        cell_now = self.xy_to_cell()

        for obj in self.model.grid.get_cell_list_contents(cell_now):
            if isinstance(obj, Environment):
                # print(f"current at MP location in x richting: {current_x}")
                # print(f"current at MP location in y richting: {current_y}")
                current_y = obj.current_y
                current_x = obj.current_x

        self.y += current_y
        self.x += current_x

    def move_swim(self):
        """Defines the persons swimming choices, will later be defined by personal traits"""
        cell_now = self.xy_to_cell()
        x_cell, y_cell = cell_now

        # print(f'x, y before swimming{self.x, self.y}')

        "Vermiste laat zich meevoeren en zwemt vervolgens naar het strand terug"
        if self.profile == 1:
            if 23 > x_cell > 18:
                if 0 < y_cell < 10:
                    pass
            elif y_cell >= 10 and 23 + 2 > x_cell > 18 - 2:
                self.x += self.swimming_speed
                self.stamina -= 1
                print(f'zwemsnelheid: {self.swimming_speed}, x: {self.x}, y: {self.y}')
            else:
                self.y -= self.swimming_speed
                self.stamina -= 1
                print(f'INELSE: zwemsnelheid: {self.swimming_speed}, x: {self.x}, y: {self.y}')
            print(f"profile = {self.profile}, y_cell = {y_cell}, x_cell = {x_cell}")

        """Vermiste persoon zwemt in paniek willekeurig rond"""
        if self.profile == 2:
            seed = self.model.seed + self.stamina
            random.seed(seed)
            x_random = random.randrange(-10, 10, 1)
            y_random = random.randrange(-10, 10, 1)
            self.x += (x_random / 10)
            self.y += (y_random / 10)

        if self.profile == 3:
            self.y -= self.swimming_speed
            self.stamina -= 3

    def move_wind(self):
        seed = self.model.seed + self.stamina
        # random.seed(seed)

        if self.wind_richting == "NOORD":
            graden = 180
        else:
            graden = 0

        factor = random.randrange(70, 90) / 10000
        leeway_speed = self.wind * factor

        richting = random.randrange((graden - 20), (graden + 20))
        leeway_x = leeway_speed * math.cos(math.radians(richting))
        leeway_y = leeway_speed * math.sin(math.radians(richting))

        self.x += leeway_x
        self.y += leeway_y

        print(f'richting: {self.wind_richting}, snelheid: {self.wind}')
        print(f'orig graden: {graden}, richting_stap: {richting}graden, factor: {factor}')
        print(f'x_meters {leeway_x}, y_meters {leeway_y}')

    def step(self):
        self.tick += 1
        print(f'stamina: {self.stamina}')
        if self.stamina > 0:
            """How will the person move due to the current in the given cell"""
            if self.tick < self.model.tijd_melding_sec:
                self.move_current()
            """How will the person move due to its own swimming and choices"""
            self.move_swim()
            """How will the person move due to the wind in the model"""
            # self.move_wind()

            cell = self.xy_to_cell()
            x, y = cell

            """Out of Bounds"""
            if x >= self.model.grid.width or y >= self.model.grid.height or x < 0 :
                print("Person left the  field and will not be found")
                self.model.running = False
            elif y < 0:
                print("Person swam back to the beach")
                self.model.running = False
            else:
                self.model.grid.move_agent(self, cell)

            """Stamina neemt altijd af, dit zal meer zijn bij slechtere weersomstandigheden"""
            stamina_stap = (self.wind - 7)/3 + 1
            self.stamina -= stamina_stap
        else:
            self.model.running = False
            print(f'Person ran out of stamina')
