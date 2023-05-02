import random

from SarServer import server
from SarModel import SearchAndRescue

import pandas as pd

# Set to True if  you want to experiment and to False if you want to see the running server
Experimenting = False
single_seed = False
# Run the server and do manual experiments

time_till_drowning = 500

if not Experimenting and not single_seed:
    server.launch()
elif Experimenting and not single_seed:
    num_iterations = 10

    seed_list = []
    search_pattern_list = []
    num_units_list = []
    search_radius_list = []
    max_current_list=[]
    upper_current_list = []
    stamina_list = []
    profile_list = []
    time_list = []

    for i in range(0,num_iterations):
        nr_steps = 0
        seed = random.randint(0,500000)

        width = 90
        height = 60
        search_pattern = "Parallel sweep"
        num_units = 1
        search_radius = 5
        max_current = 5
        upper_current = 1
        stamina = 100
        profile = 1

        model = SearchAndRescue(width, height, search_pattern,
                                num_units, search_radius, max_current,
                                upper_current,stamina, profile, seed)
        while model.running and nr_steps <= time_till_drowning:
            model.step()
            nr_steps += 1
            print(nr_steps)

        if nr_steps == time_till_drowning:
            time = 0
        else:
            time = nr_steps

        seed_list.append(seed)
        search_pattern_list.append(search_pattern)
        num_units_list.append(num_units)
        search_radius_list.append(search_radius)
        max_current_list.append(max_current)
        upper_current_list.append(upper_current)
        stamina_list.append(stamina)
        profile_list.append(profile)
        time_list.append(time)


    raw_data = {"Seed":seed_list,
                "Search pattern": search_pattern_list,
                "Num_units": num_units_list,
                "Search radius": search_radius_list,
                "Max_current": max_current_list,
                "Upper current": upper_current_list,
                "Stamina": stamina_list,
                "Profile": profile_list,
                "Time": time_list}


    df = pd.DataFrame(raw_data)
    filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results'
    # version = f'{i}'
    # filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_test' + version

    df.to_csv(filepath)
elif Experimenting and single_seed:
    seed=205140
    nr_steps = 0

    width = 90
    height = 60
    search_pattern = "Parallel sweep"
    num_units = 1
    search_radius = 5
    max_current = 5
    upper_current = 1
    stamina = 100
    profile = 1

    model = SearchAndRescue(width, height, search_pattern, num_units, search_radius, max_current, upper_current,
                            stamina, seed)
    while model.running and nr_steps <= time_till_drowning:
        model.step()
        nr_steps += 1
        print(nr_steps)

    if nr_steps == time_till_drowning:
        time = 0
    else:
        time = nr_steps

    raw_data = {"Seed": [seed],
                "Search pattern": [search_pattern],
                "Num_units": [num_units],
                "Search radius": [search_radius],
                "Max_current": [max_current],
                "Upper current": [upper_current],
                "Stamina": [stamina],
                "Profile":  [profile],
                "Time": [time]}

    df = pd.DataFrame(raw_data)
    filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_seed'
    df.to_csv(filepath)

elif not Experimenting and single_seed:
    print("In Sar Model doen!!")
    # Doe dit in SarModel document: Seed aanpassen




