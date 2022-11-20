import mesa

from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import SingleGrid

from DiffusionAgent import Environment

class Diffusion(Model):

    def __init__(self, height=50, width=50, evaporate=0.07, diffusion=0.3,
                 initdrop=500,  lowerbound=0.01):
        super().__init__()

        self.evaporate = evaporate
        self.diffusion = diffusion
        self.initdrop = initdrop
        self.lowerbound = lowerbound

        self.schedule = SimultaneousActivation(self)

        self.grid = SingleGrid(height, width, torus=True)

        for (contents, x, y) in self.grid.coord_iter():
            cell = Environment((x,y), self)
            self.grid.place_agent(cell, (x,y))
            self.schedule.add(cell)

            if self.random.random() < 0.01:
                cell.add(self.initdrop)

        self.running = True

    def step(self):
        self.schedule.step()





