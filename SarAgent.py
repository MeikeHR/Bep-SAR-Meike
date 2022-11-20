from mesa import Agent
import random

# from SarModel import SearchAndRescue

class Unit(Agent):

    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos
        self.looking = True
        self.found = False
        self.going_up = False
        self.going_right = True
        self.going_left = False
        self.step_nr = 0

    def move(self):
        "Is the agent still looking or did they spot the missing person?" #1
        "After that, check in what direction the boat should be moving and change the booleans accordingly" #2
        "Lastly, check these booleans and perform the actual movement of the agent" #3

        #1
        if self.looking:
            x, y = self.pos
            max_x = self.model.grid.width - 1

            #2
            if self.going_left is True and self.going_up is True and self.step_nr == 5:
                self.going_left = False
                self.going_up = False
                self.going_right = True
                self.step_nr = 0
            if self.going_right is True and self.going_up is True and self.step_nr == 5:
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
                    self.model.grid.move_agent(self, new_pos)
                    self.step_nr += 1
                elif self.going_right is True:
                    new_pos = (x+1, y)
                    self.model.grid.move_agent(self, new_pos)
                    self.step_nr += 1
            else:
                new_pos = (x, y+1)
                self.model.grid.move_agent(self, new_pos)
                self.step_nr += 1

        # print(f"moved right = {self.going_right}, moved up = {self.going_up}, moved left = {self.going_left}, nr step: {self.step_nr}")


    def step(self):
        if self.model.search_pattern_slider == 'Parallel Sweep':
            self.move()

class MissingPerson(Agent):
    def __init__(self, unique_id, pos, model, stamina):
        super().__init__(unique_id, model)
        self.stamina = stamina
        self.pos = pos

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center="False")
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)


