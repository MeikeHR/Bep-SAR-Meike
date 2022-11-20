from mesa import Agent
# from DiffusionModel import Diffusion

class Environment(Agent):

    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.pos = pos
        self.amount = 0.0

    def step(self):
        # pattern = model var)
        all_p = self.amount
        neighbors = self.model.grid.get_neighbors(self.pos, True)
        for n in neighbors:
            all_p += n.amount
        ave_p = all_p / (len(neighbors) + 1)

        self._nextAmount =  (1 - self.model.evaporate) * \
                            (self.amount + (self.model.diffusion * (ave_p - self.amount)))
        if self._nextAmount < self.model.lowerbound:
            self._nextAmount = 0

    def advance(self):
        self.amount = self._nextAmount

    def add(self, amount):
        self.amount += amount

    def get_pos(self):
        return self.pos

    def look(self, range):
        # found = False
        # if ...:
        #     found = True
        # return found
        pass

    def move_pattern(self):
        pass

    def move_found(self):
        pass

