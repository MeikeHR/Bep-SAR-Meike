import random

from SarServer import server
from SarModel import SearchAndRescue
# from SarUnit import Unit
from SarMissingPerson import MissingPerson

import pandas as pd

# Set to True if  you want to experiment and to False if you want to see the running server
Experimenting = True
single_seed = False

if not Experimenting and not single_seed:
    server.launch()
elif Experimenting and not single_seed:
    num_iterations = 50

    seed_list = []
    search_pattern_list = []
    search_radius_list = []
    max_current_list = []
    upper_current_list = []
    wind_list = []
    profile_list = []
    tijd_melding_list = []
    swimming_ability_list = []
    wind_richting_list = []
    tijd_list = []
    stamina_eind_list = []
    location_list = []
    location_begin_list = []
    stamina_begin = []

    for i in range(0, num_iterations):

        width = 100
        height = 60
        search_radius = 100
        seed_n = 100
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.41
        wind = 10
        profile = 2
        swimming_ability = "GOED"
        tijd_melding = 5
        wind_richting = "OOST"

        print(f"running experiment {i} with seed {seed}")

        model = SearchAndRescue(width, height,
                                search_pattern,
                                search_radius,
                                max_current,
                                upper_current,
                                wind,
                                profile,
                                swimming_ability,
                                tijd_melding,
                                wind_richting,
                                seed
                                )

        while model.running:
            model.step()

        seed_list.append(seed)
        search_pattern_list.append(search_pattern)
        search_radius_list.append(search_radius)
        max_current_list.append(max_current)
        upper_current_list.append(upper_current)
        profile_list.append(profile)
        tijd_melding_list.append(tijd_melding)
        swimming_ability_list.append(swimming_ability)
        wind_list.append(wind)
        wind_richting_list.append(wind_richting)
        tijd_list.append(model.step_counter)
        stamina_begin.append(model.stamina)
        stamina_eind = [a.stamina for a in model.schedule.agents if isinstance(a, MissingPerson)]
        location_eind = [a.xy_to_cell() for a in model.schedule.agents if isinstance(a, MissingPerson)]
        location_list.append(location_eind[0])
        location_begin_list.append(model.pos_mp_begin)
        stamina_eind_list.append(int(stamina_eind[0]))

    raw_data = {"Seed": seed_list,
                "Search pattern": search_pattern_list,
                "Search radius": search_radius_list,
                "Max_current": max_current_list,
                "Upper current": upper_current_list,
                "Profile": profile_list,
                "Zwemvaardgheid": swimming_ability_list,
                "Windrichting": wind_richting_list,
                "Windsnelheid": wind_list,
                "Uitruktijd": tijd_melding_list,
                "Stamina begin": stamina_begin,
                "Overgebleven conditie": stamina_eind_list,
                "Vind tijd": tijd_list,
                "Locatie begin": location_begin_list,
                "Locatie eind": location_list
                }

    df = pd.DataFrame(raw_data)
    filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_1.txt'
    # version = f'{i}'
    # filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_test' + version
    df.to_csv(filepath)

elif Experimenting and single_seed:
    seed = 300
    width = 100
    height = 60
    search_pattern = "Parallel Sweep"
    search_radius = 125
    max_current = 1.5
    upper_current = 0.5
    wind = 8
    profile = 1
    swimming_ability = "GOED"
    tijd_melding = 10
    wind_richting = "ZUID"

    model = SearchAndRescue(width, height,
                            search_pattern,
                            search_radius,
                            max_current,
                            upper_current,
                            wind,
                            profile,
                            swimming_ability,
                            tijd_melding,
                            wind_richting,
                            seed
                            )

    while model.running:
        model.step()

    seed_list = [seed]
    search_pattern_list = [search_pattern]
    search_radius_list = [search_radius]
    max_current_list = [max_current]
    upper_current_list = [upper_current]
    profile_list = [profile]
    tijd_melding_list = [tijd_melding]
    swimming_ability_list = [swimming_ability]
    wind_list = [wind]
    wind_richting_list = [wind_richting]
    tijd_list = [model.step_counter]
    stamina_eind_list = [a.stamina for a in model.schedule.agents if isinstance(a, MissingPerson)]

    raw_data = {"Seed":seed_list,
                "Search pattern": search_pattern_list,
                "Search radius": search_radius_list,
                "Max_current": max_current_list,
                "Upper current": upper_current_list,
                "Profile": profile_list,
                "Zwemvaardgheid": swimming_ability_list,
                "Windrichting": wind_richting_list,
                "Windsnelheid": wind_list,
                "Uitruktijd": tijd_melding_list,
                "Overgebleven conditie": stamina_eind_list,
                "Vind tijd": tijd_list
                }

    df = pd.DataFrame(raw_data)
    filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_seed'
    df.to_csv(filepath)

elif not Experimenting and single_seed:
    print("In Sar Model doen!!")





