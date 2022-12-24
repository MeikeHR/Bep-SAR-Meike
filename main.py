from SarServer import server
import pandas as pd
from SarModel import SearchAndRescue
# import gini

# Run the server and do manual experiments
server.launch()

# Run a batch of experiments with different parameter values
# for i in range(0,10):
#     nr_steps = 0
#
#     width = 90
#     height = 60
#     search_pattern = "Parallel sweep"
#     num_units = 1
#     search_radius = 3
#     max_current = 10
#     model = SearchAndRescue(width, height, search_pattern, num_units, search_radius, max_current)
#     while model.running or nr_steps <= 500:
#         model.step()
#         nr_steps += 1
#
#         gini.to_csv("model_data.csv")
#
#
#     for agent in model.schedule.agents:
#         all_wealth.append(agent.wealth)

# results = "hallo"
# results_df = pd.DataFrame(results)
# results_df.to_csv(filepath)
#
# from pathlib import Path
# filepath = Path('folder/subfolder/out.csv')
# filepath.parent.mkdir(parents=True, exist_ok=True)
# df.to_csv(filepath)
#
# res = {'name': ['Raphael', 'Donatello'],
#                    'mask': ['red', 'purple'],
#                    'weapon': ['sai', 'bo staff']}
# df = pd.DataFrame(res)
# df.to_csv(index=False)

# raw_data = {"city": ['Tripoli','Rome','Sydney'],
#             "rank":['3rd','2nd','1st'],
#             "name": ['Adam','Kevin','Pieter']}
# # df = pd.DataFrame(raw_data, colums=['city','rank','name'])
# df = pd.DataFrame(raw_data)
# df.to_csv('C:/Users/mhrb0/OneDrive/Documenten/Delf/TB/BEP/Resultaten/test19-12.txt')

