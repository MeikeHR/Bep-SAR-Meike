import random
import numpy as np
import math

from mesa import Agent
from SarEnvironment import Environment


class MissingPerson(Agent):
    def __init__(self, unique_id, x, y, model, profile):
        super().__init__(unique_id, model)
        self.stamina = self.model.stamina
        self.profile = profile

        self.x = x*20
        self.y = y*20

    def xy_to_cell(self):
        x = int(self.x/20)
        y = int(self.y/20)
        return x, y

    def move_current(self):
        """Defines the influence of the current of the cell the person is in, on its position"""
        cell_now = self.xy_to_cell()
        # print(cell_now)

        for obj in self.model.grid.get_cell_list_contents(cell_now):
            if isinstance(obj, Environment):
                current_y = obj.current_y
                current_x = obj.current_x
                # print(f"current at MP location in x richting: {current_x}")
                # print(f"current at MP location in y richting: {current_y}")

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
                self.x += 1
                self.stamina -= 1

            if x_cell >= 23 + 2:
                self.y -= 1
                self.stamina -= 1

        if self.profile == 2:
            seed = self.model.seed
            random.seed(seed)
            self.x += (random.randrange(-10, 10, 1) / 10)
            self.y += (random.randrange(-10, 10, 1) / 10)

        if self.profile == 3:
            self.y -= 1
            self.stamina -= 3

        # print(f'x, y after swimming{self.x, self.y}')



    def step(self):
        if self.stamina > 0:
            """How will the person move due to the current in the given cell"""
            self.move_current()
            """How will the person move due to its own swimming and choices"""
            self.move_swim()

            cell = self.xy_to_cell()
            x,y = cell
            # print(x,y, self.model.grid.width)

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
            # print(self.stamina)
        else:
            self.model.running = False
            print(f'Person ran out of stamina')
