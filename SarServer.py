from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.UserParam import UserSettableParameter

import math

from SarModel import SearchAndRescue
from SarUnit import Unit
from SarEnvironment import Environment
from SarMissingPerson import MissingPerson

width = 100
height = 60

params = {
    "height": height,
    "width": width,
    "search_pattern": UserSettableParameter('choice', "Zoekpatroon", value='Parallel Sweep',
                                            choices=['Parallel Sweep',
                                                     'Expanding Square',
                                                     'Sector Search',
                                                     'Random Search']),
    "wind_richting": UserSettableParameter('choice', "Wind richting", value='ZUID',
                                           choices=['NOORD',
                                                    'ZUID']),
    "swimming_ability": UserSettableParameter('choice', "Zwemvaardigheid", value='GOED',
                                           choices=['GOED',
                                                    'SLECHT']),
    "max_current": UserSettableParameter("slider", "Maximum current in riptide (m/s)", 1.5, 1, 2.5, 0.5),
    "upper_current": UserSettableParameter("slider", "Upper current, northern direction (m/s)", 0.5, 0.41, 0.77, 0.01),
    "search_radius": UserSettableParameter("slider", "Search radius (m)", 125, 50, 125, 25),
    "wind": UserSettableParameter("slider", "Windsnelheid (m/s)", 8, 8, 10, 1),
    "stamina": UserSettableParameter("slider", "Conditie (-)", 1800, 900, 3600, 100),
    "profile": UserSettableParameter("slider", "Profiel (-)", 1, 1, 2, 1),
    "tijd_melding": UserSettableParameter("slider", "Uitruktijd (min)", 5, 0, 15, 5),
    "seed":UserSettableParameter('number', 'Seed', value=100)
}


def portrayal_method(agent):
    """ Defines how a cell in the grid will be portrayed. All cells contain an environment agent with an attribute for
    the current. According to this parameter the cell will be shown in a certain shade of blue. If a cell also contains
    an unit agent of missing person agent, in a higher layer this will be shown with a circle. Black for the missing
    person and red for the looking unit"""
    rg_init = 240
    blue = '#%02x%02x%02x' % (rg_init, rg_init, 255)

    portrayal = {"Shape": "rect",
                 "w": 1, "h": 1,
                 "Color": blue,
                 "Filled": "true",
                 "Layer": 0
                 }

    if isinstance(agent, Environment):

        if agent.path:
            grey = '#%02x%02x%02x' % (100, 100, 100)
            portrayal["Color"] = grey
            portrayal["Layer"] = 1

        if agent.current_y != 0 or agent.current_x != 0:
            if agent.path is False:
                # fraction = agent.current_y / SearchAndRescue.max_current
                cell_current = math.sqrt((agent.current_x**2 + agent.current_y**2))
                """"Bepaal dichtheid van de kleuren (factor4 4)"""
                fraction = cell_current/4
                rg = int(rg_init - rg_init * fraction)
                blue_tint = '#%02x%02x%02x' % (rg, rg, 255)
                portrayal["Color"] = blue_tint
                portrayal["Layer"] = 0

    if isinstance(agent, Unit):
        portrayal["Shape"] = "circle"
        portrayal["Color"] = 'red'
        portrayal["Layer"] = 2
        portrayal["r"] = 0.8

    if isinstance(agent, MissingPerson):
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "black"
        portrayal["Layer"] = 2
        portrayal["r"] = 0.8

    return portrayal


grid = CanvasGrid(portrayal_method, 100, 60, 1000, 600)

server = ModularServer(SearchAndRescue, [grid], "Sar Model", params)
