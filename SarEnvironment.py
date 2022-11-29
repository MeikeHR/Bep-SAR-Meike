from mesa import Agent


class Environment(Agent):

    def __init__(self, pos, current, path, model):
        super().__init__(pos, model)
        self.current = current
        self.path = path
