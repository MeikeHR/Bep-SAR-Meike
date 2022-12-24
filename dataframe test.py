import pandas as pd

raw_data = {"city": ['Tipoli', 'Rome', 'Sydney'],
            "rank": ['3rd', '2nd', '1st'],
            "name": ['Adam', 'Kevin', 'Pieter']}
df = pd.DataFrame(raw_data)
filepath = r'C:/Users/mhrb0/PycharmProjects/MesaPractise/Results/Results_test'
df.to_csv(filepath)
