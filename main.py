from SarServer import server
from SarModel import SearchAndRescue

import pandas as pd

# Set to True if  you want to experiment and to False if you want to see the running server
Experimenting = False
# Run the server and do manual experiments

if not Experimenting:
    server.launch()
else:
    time_till_drowning = 500
    for i in range(0,5):
        nr_steps = 0

        width = 90
        height = 60
        search_pattern = "Parallel sweep"
        num_units = 1
        search_radius = 10
        max_current = 2
        model = SearchAndRescue(width, height, search_pattern, num_units, search_radius, max_current)
        while model.running and nr_steps <= time_till_drowning:
            model.step()
            nr_steps += 1
            print(nr_steps)

        if nr_steps == time_till_drowning:
            time = 0
        else:
            time = nr_steps

        raw_data = {"Search pattern": [search_pattern],
                    "Num_units": [num_units],
                    "Search radius": [search_radius],
                    "Max_current": [max_current],
                    "Time": [time]}

        version = f'{i}'
        df = pd.DataFrame(raw_data)
        filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_test' + version

        df.to_csv(filepath)

    # for i in range(0, 3):
    #     search_pattern = "Parallel sweep"
    #     num_units = 1
    #     search_radius = 3
    #     max_current = 10
    #     time = 5
    #     raw_data = {"Search pattern": [search_pattern],
    #                 "Num_units": [num_units],
    #                 "Search radius": [search_radius],
    #                 "Max_current": [max_current],
    #                 "Time": [time]}
    #
    #     print(f"running experiment {i}")
    #     version = f'{i}'
    #     df = pd.DataFrame(raw_data)
    #     filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_test' + version
    #
    #     df.to_csv(filepath)