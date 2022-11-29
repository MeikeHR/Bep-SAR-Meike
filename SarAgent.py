import numpy as np
from mesa import Agent

from SarEnvironment import Environment


class Unit(Agent):

    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.pos = pos

        self.going_up = False
        self.going_right = True
        self.going_left = False
        self.step_nr = 0

    def move_ps(self):
        """
        1. Is the agent still looking or did they spot the missing person?
        2. After that, check in what direction the boat should be moving and change the booleans accordingly
        3. Lastly, check these booleans and perform the actual movement of the agent
        """

        # 1
        x, y = self.pos
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

    def look(self, radius):
        # get neighbors radius range
        field = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False, radius=radius)

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
            agents = self.model.grid.get_cell_list_contents(new_pos)
            if any(isinstance(agent, MissingPerson) for agent in agents):
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
            agents = self.model.grid.get_cell_list_contents(new_pos)
            if any(isinstance(agent, MissingPerson) for agent in agents):
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
            agents = self.model.grid.get_cell_list_contents(new_pos)
            if any(isinstance(agent, MissingPerson) for agent in agents):
                # if isinstance(self.model.grid.get_cell_list_contents(new_pos), MissingPerson):
                # if not self.model.grid.is_cell_empty(new_pos):
                self.model.running = False
                return print(f"Stop de tijd, persoon is gevonden! Feestje")
            self.model.grid.move_agent(self, new_pos)

    def step(self):
        loc = self.model.grid.get_cell_list_contents(self.pos)
        print(loc)
        for obj in loc:
            if isinstance(obj, Environment):
                obj.path = True

        pos_mp = self.look(self.model.search_radius)
        print(f"pos_mp = {pos_mp}")
        if pos_mp is not ():
            self.move_to(pos_mp)
        else:
            if self.model.search_pattern == 'Parallel Sweep':
                self.move_ps()


class MissingPerson(Agent):
    def __init__(self, unique_id, pos, model, stamina=800):
        super().__init__(unique_id, model)
        self.stamina = stamina
        self.pos = pos

    def move(self):
        for object in self.model.grid.get_cell_list_contents(self.pos):
            if isinstance(object, Environment):
                current = object.current

        x, y = self.pos
        y += int(current)
        self.model.grid.move_agent(self, (x, y))

        "Still need to add random or non-random choice of movement"

        # current = (object.current if isinstance(object, Environment) for object in self.model.grid.get_cell_list_contents(self.pos))

        # possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center="False")
        # new_position = random.choice(possible_steps)
        # self.model.grid.move_agent(self, new_position)

    def step(self):
        # stroming
        # eigenschappen
        # tijd tot verdrinking
        if self.stamina != 0:
            self.move()
        self.stamina -= 1
        # test



