import random
from SarServer import server
from SarModel import SearchAndRescue
# from SarUnit import Unit
from SarMissingPerson import MissingPerson
import pandas as pd

inklap_var = True

"Run deze file voor het experimenteren op basis van de scenarios uit deelvraag 2"
basis_seed = 10000
num_iterations = 500

if inklap_var:
    seed_list = []
    label_list = []
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

    width = 100
    height = 60
    search_radius = 100
    max_current = 2.0

for i in range(1, num_iterations+1):
    scenario_counter = 0
    """Scenario 1"""
    label = "Alles 0"
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

    if inklap_var:
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

    if inklap_var:
        seed_list.append(seed)
        label_list.append(label)
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
    label = "Wind -10"
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
    wind = 9
    profile = 1
    swimming_ability = "GOED"
    tijd_melding = 5
    wind_richting = "OOST"

    if inklap_var:
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

    if inklap_var:
        seed_list.append(seed)
        label_list.append(label)
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
    label = "Wind +10"
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
    wind = 11
    profile = 1
    swimming_ability = "GOED"
    tijd_melding = 5
    wind_richting = "OOST"

    if inklap_var:
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

    if inklap_var:
        seed_list.append(seed)
        label_list.append(label)
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
    label = "Stroming -10"
    scenario_counter += 1
    width = 100
    height = 60
    search_radius = 100
    seed_n = scenario_counter * basis_seed
    seed = seed_n + i
    random.seed(seed)
    max_current = 2.0

    search_pattern = "Parallel Sweep"

    upper_current = 0.41 * 0.9
    wind = 10
    profile = 1
    swimming_ability = "GOED"
    tijd_melding = 5
    wind_richting = "OOST"

    if inklap_var:
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

    if inklap_var:
        seed_list.append(seed)
        label_list.append(label)
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
    label = "Stroming +10"
    scenario_counter += 1
    width = 100
    height = 60
    search_radius = 100
    seed_n = scenario_counter * basis_seed
    seed = seed_n + i
    random.seed(seed)
    max_current = 2.0

    search_pattern = "Parallel Sweep"

    upper_current = 0.41 * 1.1
    wind = 10
    profile = 1
    swimming_ability = "GOED"
    tijd_melding = 5
    wind_richting = "OOST"

    if inklap_var:
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

    if inklap_var:
        seed_list.append(seed)
        label_list.append(label)
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
    label = "Uitruktijd - 10"
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
    tijd_melding = 5 * 0.9
    wind_richting = "OOST"

    if inklap_var:
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

    if inklap_var:
        seed_list.append(seed)
        label_list.append(label)
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
    label = "Uitruktijd +10"
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
    tijd_melding = 5 * 1.1
    wind_richting = "OOST"

    if inklap_var:
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

    if inklap_var:
        seed_list.append(seed)
        label_list.append(label)
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
    label = "Zoekradius -10"
    scenario_counter += 1
    width = 100
    height = 60
    search_radius = 100 * 0.9
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

    if inklap_var:
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

    if inklap_var:
        seed_list.append(seed)
        label_list.append(label)
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
    label = "Zoekradius +10"
    scenario_counter += 1
    width = 100
    height = 60
    search_radius = 100 * 1.1
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

    if inklap_var:
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

    if inklap_var:
        seed_list.append(seed)
        label_list.append(label)
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
        label = "muistroom -10"
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0 * 0.9

        search_pattern = "Parallel Sweep"

        upper_current = 0.41
        wind = 10
        profile = 1
        swimming_ability = "GOED"
        tijd_melding = 5
        wind_richting = "OOST"

        if inklap_var:
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

        if inklap_var:
            seed_list.append(seed)
            label_list.append(label)
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

        """Scenario 11"""
        label = "muistroom +10"
        scenario_counter += 1
        width = 100
        height = 60
        search_radius = 100
        seed_n = scenario_counter * basis_seed
        seed = seed_n + i
        random.seed(seed)
        max_current = 2.0 * 1.1

        search_pattern = "Parallel Sweep"

        upper_current = 0.41
        wind = 10
        profile = 1
        swimming_ability = "GOED"
        tijd_melding = 5
        wind_richting = "OOST"

        if inklap_var:
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

        if inklap_var:
            seed_list.append(seed)
            label_list.append(label)
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
            "Label": label_list,
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
filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_GevoeligheidsAnalyse.txt'

df.to_csv(filepath)