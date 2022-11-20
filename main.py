# from MoneyModel import *
# import mesa
#

# def agent_portrayal(agent):
#     portrayal = {"Shape": "circle",
#                  "Filled": "true",
#                  "Layer": 0,
#                  "Color": "blue",
#                  "r": 0.5}
#     return portrayal
#
# grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)
# server = mesa.visualization.ModularServer(
#     MoneyModel, [grid], "Money Model", {"N": 100, "width": 10, "height": 10})
#
# server.port = 8521 # The default
# server.launch()

# from DiffusionServer import server
# server.launch()

from SarServer import server
server.launch()
