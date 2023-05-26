import random

from SarServer import server
from SarModel import SearchAndRescue
# from SarUnit import Unit
from SarMissingPerson import MissingPerson

import pandas as pd

"""Deze booleans bepalen het type uit te voeren experiment, uitleg staat in de bijlage"""
experimenting = True
alle_scenarios = True
single_seed = False

deelvraag = False

if not experimenting and not single_seed:
    server.launch()

"""Gebruik deze waardes voor de booleans als je een x aantal replicaties van één scenario wilt uitvoeren"""
if experimenting and not single_seed and not alle_scenarios and not deelvraag:
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
    found_list = []
    actieduur_list = []

    for i in range(0, num_iterations):
        """Scenario x"""
        scenario = 1

        width = 100
        height = 60
        search_radius = 100
        max_current = 2.0

        seed_n = 1000
        seed = seed_n + i
        random.seed(seed)

        search_pattern = "Parallel Sweep"
        if scenario in [1,2,3,4,9,10,11,12]:
            upper_current = 0.41
        else:
            upper_current = 0.77
        if scenario in [1,2,7,8,11,12,13,14]:
            wind = 10
        else:
            wind = 8
        if scenario in [1,3,5,7,9,11,13,15]:
            swimming_ability = "GOED"
        else:
            swimming_ability = "SLECHT"
        if scenario in [1,2,5,6,9,10,13,14]:
            profile = 1
        else:
            profile = 2
        if scenario in [1,2,3,4,13,14,15,16]:
            tijd_melding = 5
        else:
            tijd_melding = 15
        if scenario in [1,4,6,7,9,12,14,15]:
            wind_richting = "OOST"
        else:
            wind_richting = "ZUID"

        """Zelf invullen"""
        upper_current = 0.41
        wind = 10
        profile = 1
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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding * 60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

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
                "Locatie eind": location_list,
                "Gevonden": found_list,
                "Actieduur": actieduur_list
                }

    df = pd.DataFrame(raw_data)
    filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_Deelvraag2.txt'
    df.to_csv(filepath)

"""Gebruik deze waardes voor de booleans als alle scenarios wilt uitvoeren, uitleg over gebruik staat in de bijlage"""
if experimenting and not single_seed and alle_scenarios and not deelvraag:
    basis_seed = 10000
    num_iterations = 500

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
    found_list = []
    actieduur_list = []

    for i in range(1, num_iterations+1):
        scenario_counter = 0
        """Scenario 1"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.41
        wind = 10
        profile = 1
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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 2"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.41
        wind = 10
        profile = 1
        swimming_ability = "SLECHT"
        tijd_melding = 5
        wind_richting = "ZUID"

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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 3"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.41
        wind = 8
        profile = 2
        swimming_ability = "GOED"
        tijd_melding = 5
        wind_richting = "ZUID"

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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 4"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.41
        wind = 8
        profile = 2
        swimming_ability = "SLECHT"
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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 5"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.77
        wind = 8
        profile = 2
        swimming_ability = "GOED"
        tijd_melding = 15
        wind_richting = "ZUID"

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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 6"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.77
        wind = 8
        profile = 1
        swimming_ability = "SLECHT"
        tijd_melding = 15
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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 7"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.77
        wind = 10
        profile = 2
        swimming_ability = "GOED"
        tijd_melding = 15
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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 8"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.77
        wind = 10
        profile = 2
        swimming_ability = "SLECHT"
        tijd_melding = 15
        wind_richting = "ZUID"

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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 9"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.41
        wind = 8
        profile = 1
        swimming_ability = "GOED"
        tijd_melding = 15
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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 10"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.41
        wind = 8
        profile = 1
        swimming_ability = "SLECHT"
        tijd_melding = 15
        wind_richting = "ZUID"

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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 11"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.41
        wind = 10
        profile = 2
        swimming_ability = "GOED"
        tijd_melding = 15
        wind_richting = "ZUID"

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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 12"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.41
        wind = 10
        profile = 2
        swimming_ability = "SLECHT"
        tijd_melding = 15
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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 13"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.77
        wind = 10
        profile = 1
        swimming_ability = "GOED"
        tijd_melding = 5
        wind_richting = "ZUID"

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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 14"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.77
        wind = 10
        profile = 1
        swimming_ability = "SLECHT"
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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 15"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.77
        wind = 8
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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 16"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.77
        wind = 8
        profile = 2
        swimming_ability = "SLECHT"
        tijd_melding = 5
        wind_richting = "ZUID"

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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

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
                "Locatie eind": location_list,
                "Gevonden": found_list,
                "Actieduur": actieduur_list
                }

    df = pd.DataFrame(raw_data)
    filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_Replicaties2.txt'
    df.to_csv(filepath)

elif experimenting and single_seed and not deelvraag:
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
                "Vind tijd": tijd_list,

                }

    df = pd.DataFrame(raw_data)
    filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_seed'
    df.to_csv(filepath)

elif not experimenting and single_seed and not deelvraag:
    print("In Sar Model doen!!")


if deelvraag:
    basis_seed = 1000000
    num_iterations = 500

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
    found_list = []
    actieduur_list = []

    for i in range(1, num_iterations+1):
        scenario_counter = 16
        """Scenario 17"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.77
        wind = 8
        profile = 2
        swimming_ability = "SLECHT"
        tijd_melding = 15
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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 2"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.77
        wind = 10
        profile = 2
        swimming_ability = "SLECHT"
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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

        """Scenario 3"""
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0

        search_pattern = "Parallel Sweep"

        upper_current = 0.77
        wind = 10
        profile = 1
        swimming_ability = "SLECHT"
        tijd_melding = 15
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
        found_list.append(model.found)
        actieduur = "Niet gevonden"
        if model.found:
            actieduur = (model.step_counter - tijd_melding*60)
            actieduur = "{:.2f}".format(actieduur)
        actieduur_list.append(actieduur)

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
                "Locatie eind": location_list,
                "Gevonden": found_list,
                "Actieduur": actieduur_list
                }

    df = pd.DataFrame(raw_data)
    filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_Deelvraag2.txt'
    df.to_csv(filepath)



