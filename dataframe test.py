import pandas as pd
from pathlib import Path

raw_data = {"city": ['Tripoli','Rome','Sydney'],
            "rank":['3rd','2nd','1st'],
            "name": ['Adam','Kevin','Pieter']}
df = pd.DataFrame(raw_data, columns=['city','rank','name'])
# df = pd.DataFrame(raw_data)
# df.to_csv('C:\Users\mhrb0\OneDrive\Documenten\Delft\TB\BEP\Resultaten')
# filepath = Path('C:\Users\mhrb0\PycharmProjects\MesaPractise\kest.csv')
# df.to_csv(filepath)

# filepath = r'C:\Users\mhrb0\OneDrive\Documenten\Delft\TB\BEP\Resultaten'
filepath = r'C:\Users\mhrb0\PycharmProjects\MesaPractise'
df.to_csv(filepath)
# df.to_csv (r'C:\Users\John\Desktop\export_dataframe.csv', index = None, header=True)


# from pathlib import Path
# filepath = Path('folder/subfolder/out.csv')
# filepath.parent.mkdir(parents=True, exist_ok=True)
# df.to_csv(filepath)