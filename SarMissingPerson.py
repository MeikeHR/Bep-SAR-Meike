import random
import numpy as np
import math

from mesa import Agent
from SarEnvironment import Environment


class MissingPerson(Agent):
    def __init__(self, unique_id, x, y, model,stamina, profile, swimming_speed, swimming_ability,seed):
        super().__init__(unique_id, model)
        self.profile = profile
        self.swimming_speed = swimming_speed
        self.swimming_ability = swimming_ability
        self.wind = self.model.wind
        self.wind_richting = self.model.wind_richting

        self.stamina = self.init_stamina(stamina)

        self.x = x*20
        self.y = y*20

        self.tick = 0

    def init_stamina(self, stamina):
        if self.swimming_ability == "GOED":
            return stamina
        else:
            return stamina * 2 / 3

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

        "Vermiste laat zich meevoeren en zwemt vervolgens naar het strand terug"
        if self.profile == 1:
            if 23 > x_cell > 18:
                if 0 < y_cell < 5:
                    pass
            elif y_cell >= 5 and 23 + 2 > x_cell > 18 - 2:
                self.x += self.swimming_speed
                self.stamina -= 1
                # print(f'zwemsnelheid: {self.swimming_speed}, x: {self.x}, y: {self.y}')
            else:
                self.y -= self.swimming_speed
                self.stamina -= 1
                # print(f'INELSE: zwemsnelheid: {self.swimming_speed}, x: {self.x}, y: {self.y}')
            # print(f"profile = {self.profile}, y_cell = {y_cell}, x_cell = {x_cell}")

        """Vermiste persoon zwemt in paniek willekeurig rond"""
        if self.profile == 2:
            x_random = random.randrange(-10, 10, 1)
            y_random = random.randrange(-10, 10, 1)
            self.x += (x_random / 10)
            self.y += (y_random / 10)

        if self.profile == 3:
            self.y -= self.swimming_speed
            self.stamina -= 3

    def move_swim_new(self):
        """Defines the persons swimming choices, will later be defined by personal traits"""
        cell_now = self.xy_to_cell()
        x_cell, y_cell = cell_now
        # print(f'profile: {self.profile}')

        """Persoon laat zich drijven en spaart krachten"""
        if self.profile == 1:
            pass

        """Persoon zwemt een willekeurige kant op, er vanuit gaande dat deze nauwelijks kan zien waar het strand is."""
        if self.profile == 2:
            x_random = 2 * random.randrange(-5, 5, 1) / 10
            y_random = 2 * random.randrange(-5, 1, 1) / 10

            self.x += x_random * self.swimming_speed
            self.y += y_random * self.swimming_speed

            self.stamina -= 1
            print(f'x_random * sw: {x_random * self.swimming_speed}, y_random * sw: {y_random*self.swimming_speed}')

    def move_wind(self):
        if self.wind_richting == "NOORD":
            graden = 180
        elif self.wind_richting == "ZUID":
            graden = 0
        elif self.wind_richting == "OOST":
            graden = 90
        else:
            graden = 270

        """Bereken de daadwerkelijke invloed van de windsnelheid op de drift snelheid"""
        factor = random.randrange(9, 12) / 1000
        leeway_speed = self.wind * factor

        richting = random.randrange((graden - 10), (graden + 10))
        leeway_x = leeway_speed * math.cos(math.radians(richting))
        leeway_y = leeway_speed * math.sin(math.radians(richting))

        self.x += leeway_x
        self.y += leeway_y

    def move_random(self):
        dx = random.randrange(-15, 20, 5) / 15 * self.swimming_speed / 2
        dy = random.randrange(-15, 20, 5) / 15 * self.swimming_speed / 2
        print(f'random movement mp --> dx: {dx}, dy: {dy}')
        self.x += dx
        self.y += dy
        pass

    def step(self):
        self.tick += 1
        # print(f'stamina: {self.stamina}')
        # print(f'tick < melding{self.tick} < {self.model.tijd_melding_sec}')
        if self.stamina > 0:
            """How will the person move due to the current in the given cell"""
            if self.tick < self.model.tijd_melding_sec:
                self.move_current()
            """How will the person move due to its own swimming and choices"""
            # self.move_swim()
            self.move_swim_new()
            """How will the person move due to the wind in the model"""
            self.move_wind()
            """How will the person move randomly"""
            self.move_random()

            cell = self.xy_to_cell()
            x, y = cell
            print(f'cell person: {cell}')

            """Out of Bounds"""
            if x >= self.model.width or y >= self.model.height or x < 0:
                print("Person left the  field and will not be found")
                self.model.running = False
            elif y < 0:
                print("Person swam back to the beach")
                self.model.running = False
            else:
                self.model.grid.move_agent(self, cell)

            """Stamina neemt altijd af, dit zal meer zijn bij slechtere weersomstandigheden"""
            stamina_stap = (self.wind - 8)/2 + 1
            self.stamina -= stamina_stap
        else:
            self.model.running = False
            print(f'Person ran out of stamina')
