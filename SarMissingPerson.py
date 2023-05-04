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

        self.x = x*20
        self.y = y*20

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

            if y_cell >= 10:
                self.x += self.swimming_speed
                self.stamina -= 1

            if x_cell >= 23 + 2:
                self.y -= self.swimming_speed
                self.stamina -= 1
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
        # self.model.wind
        # x en y richting
        # in deze stap --> wind specifieke invloed (randomizerrr)
        # windsnelheid = 8.5, invloed is 0.80%
        pass


    def step(self):
        print(f'stamina: {self.stamina}')
        if self.stamina > 0:
            """How will the person move due to the current in the given cell"""
            self.move_current()
            """How will the person move due to its own swimming and choices"""
            self.move_swim()
            """How will the person move due to the wind in the model"""
            self.move_wind()

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
            # Weersomstandigheden toevoegen
            self.stamina -= 1
        else:
            self.model.running = False
            print(f'Person ran out of stamina')
