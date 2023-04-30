import pandas as pd

# raw_data = {"city": ['Tipoli', 'Rome', 'Sydney'],
#             "rank": ['3rd', '2nd', '1st'],
#             "name": ['Adam', 'Kevin', 'Pieter']}
# df = pd.DataFrame(raw_data)
# # filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_test'
# filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_test_new'
#
# df.to_csv(filepath)


for i in range(0,3):
    search_pattern = "Parallel sweep"
    num_units = 1
    search_radius = 3
    max_current = 10
    time = 5
    raw_data = {"Search pattern": [search_pattern],
                "Num_units": [num_units],
                "Search radius": [search_radius],
                "Max_current": [max_current],
                "Time": [time]}

    print(f"running experiment {i}")
    version = f'{i}'
    df = pd.DataFrame(raw_data)
    filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_test'+version

    df.to_csv(filepath)
#
