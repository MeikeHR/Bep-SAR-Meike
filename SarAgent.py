import numpy as np
from mesa import Agent
import random

# from SarModel import SearchAndRescue

class Unit(Agent):

    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos
        # self.looking = True
        # self.found = False

        self.going_up = False
        self.going_right = True
        self.going_left = False
        self.step_nr = 0

    def move_PS(self):
        "Is the agent still looking or did they spot the missing person?" #1
        "After that, check in what direction the boat should be moving and change the booleans accordingly" #2
        "Lastly, check these booleans and perform the actual movement of the agent" #3
        print(f"trying to move in PS pattern")
        #1
        x, y = self.pos
        max_x = self.model.grid.width - 1
        steps_up = self.model.grid.height / 6

        #2
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

        #3
        if self.going_up is False:
            if self.going_left is True:
                new_pos = (x-1, y)
                print(f"moving from {self.pos} to {new_pos} (going left)")
                self.model.grid.move_agent(self, new_pos)
                self.step_nr += 1
            elif self.going_right is True:
                new_pos = (x+1, y)
                print(f"moving from {self.pos} to {new_pos} (going right)")
                self.model.grid.move_agent(self, new_pos)
                self.step_nr += 1
        else:
            new_pos = (x, y+1)
            print(f"moving from {self.pos} to {new_pos} (going up)")
            self.model.grid.move_agent(self, new_pos)
            self.step_nr += 1

    # print(f"moved right = {self.going_right}, moved up = {self.going_up}, moved left = {self.going_left}, nr step: {self.step_nr}")


    def look(self, range):
        #get neigbors radius range
        field = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False, radius=range)
        if not all(self.model.grid.is_cell_empty(cell_range) for cell_range in field):
            self.found = True
            self.looking = False
            for cell in field:
                if not self.model.grid.is_cell_empty(cell):
                    position_missing_person = cell
            return position_missing_person
        return ()


    def move_to(self, position):
        print(f"trying to move to mp")
        x, y = self.pos
        x_mp, y_mp = position

        dx = np.absolute(x_mp - x)
        dy = np.absolute(y_mp - y)

        if dy > dx:
            if (y_mp - y) > 0:
                new_y = y + 1
            else:
                new_y = y - 1
            new_pos = (x, new_y)
            print(f"moving from {self.pos} to {new_pos} for dy > dx")
            if not self.model.grid.is_cell_empty(new_pos):
                self.model.running = False
                return print(f"Stop de tijd, persoon is gevonden! Feestje")
            self.model.grid.move_agent(self, new_pos)

        elif dx > dy:
            if (x_mp - x) > 0:
                new_x = x + 1
            else:
                new_x = x - 1
            new_pos = (new_x, y)
            print(f"moving from {self.pos} to {new_pos} for dx > dy")
            if not self.model.grid.is_cell_empty(new_pos):
                self.model.running = False
                return print(f"Stop de tijd, persoon is gevonden! Feestje")
            self.model.grid.move_agent(self, new_pos)

        else:
            if x_mp - x > 0:
                new_x = x + 1
            else:
                new_x = x - 1
            if y_mp - y > 0:
                new_y = y + 1
            else:
                new_y = y - 1
            new_pos = (new_x, new_y)
            print(f"moving from {self.pos} to {new_pos} for dy = dx")
            if not self.model.grid.is_cell_empty(new_pos):
                self.model.running = False
                return print(f"Stop de tijd, persoon is gevonden! Feestje")
            self.model.grid.move_agent(self, new_pos)


    def step(self):
        pos_mp = self.look(self.model.search_radius)
        print(f"pos_mp = {pos_mp}")
        if pos_mp is not ():
            self.move_to(pos_mp)
        else:
            if self.model.search_pattern_slider == 'Parallel Sweep':
                self.move_PS()


class MissingPerson(Agent):
    def __init__(self, unique_id, pos, model, stamina):
        super().__init__(unique_id, model)
        self.stamina = stamina
        self.pos = pos

    def move(self):
        pass
        # possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center="False")
        # new_position = random.choice(possible_steps)
        # self.model.grid.move_agent(self, new_position)

    def step(self):
        # stroming
        # eigenschappen
        # tijd tot verdrinking
        if self.stamina != 0:
            self.move()


