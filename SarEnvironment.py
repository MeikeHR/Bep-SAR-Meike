from mesa import Agent


class Environment(Agent):

    def __init__(self, pos, current_x, current_y, path, model):
        super().__init__(pos, model)
        self.current_x = current_x
        self.current_y = current_y
        self.path = path
