import random

import numpy as np
import math
from mesa import Agent

from SarEnvironment import Environment


class Unit(Agent):

    def __init__(self, unique_id, x, y, model):
        super().__init__(unique_id, model)
        self.x = x
        self.y = y

        self.speed = 1
        self.current_factor = 0.01

        self.going_up = False
        self.going_right = True
        self.going_left = False
        self.step_nr = 0

        self.reached_middle = False

    def xy_to_cell(self):
        x = int(self.x)
        y = int(self.y)
        return x, y

    def move_search(self):
        pos_mp = self.look(self.model.search_radius)
        if pos_mp is not ():
            self.move_to_new(pos_mp)
        else:
            if self.model.search_pattern == 'Parallel Sweep':
                self.move_ps()
            elif self.model.search_pattern == 'Expanding Square':
                self.move_es()
            elif self.model.search_pattern == 'Sector Search':
                self.move_ss()
            elif self.model.search_pattern == 'Random Search':
                self.move_rs()

    def move_current(self):
        for object in self.model.grid.get_cell_list_contents(self.xy_to_cell()):
            if isinstance(object, Environment):
                current_y = object.current_y
                current_x = object.current_x

        self.y += current_y * self.current_factor
        self.x += current_x * self.current_factor

    """The following functions will define the way of movement through the water due to the chosen search pattern."""

    def move_ps(self):
        """
        1. Is the agent still looking or did they spot the missing person?
        2. After that, check in what direction the boat should be moving and change the booleans accordingly
        3. Lastly, check these booleans and perform the actual movement of the agent
        """

        # 1
        max_x = self.model.grid.width - 1
        steps_up = self.model.grid.height / 6

        # 2
        if self.going_left is True and self.going_up is True and self.step_nr == steps_up:
            self.going_left = False
            self.going_up = False
            self.going_right = True
            self.step_nr = 0
        if self.going_right is True and self.going_up is True and self.step_nr == steps_up:
            self.going_left = True
            self.going_up = False
            self.going_right = False
            self.step_nr = 0

        if self.step_nr == max_x:
            self.going_up = True
            self.step_nr = 0

        # 3
        if self.going_up is False:
            if self.going_left is True:
                self.x -= self.speed
                self.step_nr += 1
            elif self.going_right is True:
                self.x += self.speed
                self.step_nr += 1
        else:
            self.y += self.speed
            self.step_nr += 1

    def move_es(self):
        """Defines the Expanding Square search pattern"""

        # First move to the middle, dan slagen van bepaalde lengte, + vaste lengte
        middle_grid = (self.model.grid.width // 2, self.model.grid.height // 2)
        print(middle_grid)
        if self.reached_middle:
            self.move_ps()
        else:
            self.move_to(middle_grid)
            if middle_grid in self.model.grid.get_neighborhood(self.xy_to_cell(), moore=True, include_center=False, radius=1):
                self.reached_middle = True

    def move_ss(self):
        """Defines the Sector Search search pattern"""
        pass

    def move_rs(self):
        """Defines the Random Search pattern"""
        pass

    def look(self, radius):
        # get neighbors radius range
        field = self.model.grid.get_neighborhood(self.xy_to_cell(), moore=True, include_center=False, radius=radius)

        agents_in_range = {}
        for cell in field:
            agents = self.model.grid.get_cell_list_contents((cell))
            for agent in agents:
                if isinstance(agent, Environment):
                    agents_in_range["env"] = cell
                if isinstance(agent, MissingPerson):
                    agents_in_range["mp"] = cell

        if any(agent_key == "mp" for agent_key in agents_in_range.keys()):
            position_missing_person = agents_in_range["mp"]
            return position_missing_person
        return ()

    def move_to_new(self, cell):
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
                self.model.running = False

        elif dx > dy:
            if (x_mp - x) > 0:
                self.x += self.speed
            else:
                self.x -= self.speed
            agents = self.model.grid.get_cell_list_contents((self.xy_to_cell()))
            if any(isinstance(agent, MissingPerson) for agent in agents):
                self.model.running = False

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

    def step(self):
        cell_new = self.xy_to_cell()
        loc = self.model.grid.get_cell_list_contents(cell_new)
        for obj in loc:
            if isinstance(obj, Environment):
                obj.path = True

        """How does the unit move according to the search state (still looking or moving to a position)"""
        self.move_search()
        """How does the unit move due to the current"""
        self.move_current()

        cell = self.xy_to_cell()
        self.model.grid.move_agent(self, cell)

        # print(f"real x: {self.x}, real y: {self.y}, cell position: {cell}")


class MissingPerson(Agent):
    def __init__(self, unique_id, x, y, model, profile):
        super().__init__(unique_id, model)
        self.stamina = self.model.stamina
        self.profile = profile

        self.x = x
        self.y = y

        self.current_factor = 0.05
        self.swimming_speed = 1

    def xy_to_cell(self):
        x = int(self.x)
        y = int(self.y)
        return x, y

    def move_current(self):
        """Defines the influence of the current of the cell the person is in, on its position"""
        cell_now = self.xy_to_cell()
        seed = self.model.seed
        random.seed(seed)

        for obj in self.model.grid.get_cell_list_contents(cell_now):
            if isinstance(obj, Environment):
                current_y = obj.current_y
                current_x = obj.current_x
                print(f"current at MP location in y richting: {current_y}")

        self.y += current_y * self.current_factor
        self.x += current_x * self.current_factor

        """Ïnvloed van stroming blijft stochastisch en niet te voorspellen"""
        self.x += (random.randrange(-1, 1, 0.1)) * current_x * self.current_factor
        self.y += (random.randrange(-1, 1, 0.1)) * current_y * self.current_factor

    def move_swim(self):
        """Defines the persons swimming choices, defined by personal traits"""
        cell_now = self.xy_to_cell()
        x, y = cell_now
        seed = self.model.seed
        random.seed(seed)

        "Vermiste laat zich meevoeren en zwemt vervolgens naar het strand terug"
        if self.profile == 1:
            if self.model.grid.width * 3/5 > x > self.model.grid.width * 2/5:
                if 0 < y < self.model.grid.height/3:
                    pass

            if y >= self.model.grid.height/3:
                self.x += self.swimming_speed
                self.stamina -= 1

            if x >= (self.model.grid.width * 3/5) + 2:
                self.y -= self.swimming_speed
                self.stamina -= 1

        if self.profile == 2:
            self.x += (random.randrange(-self.swimming_speed, self.swimming_speed, 4))
            self.y += (random.randrange(-self.swimming_speed, self.swimming_speed, 4))

        if self.profile == 3:
            self.y -= self.swimming_speed
            self.stamina -= 3




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
            print(self.stamina)
        else:
            self.model.running = False
            print(f'Person ran out of stamina')




