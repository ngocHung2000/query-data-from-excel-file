import pandas as pd

file_name_input="input.txt"
file_name_output="output.txt"
with open(file_name_input, 'r') as f:
    data = f.readlines()
data = [x.strip().split(' ') for x in data]
df = pd.DataFrame(data[1:], columns=data[0])

df = df.reset_index(drop=True)
df.columns = [f"Col_{i}" for i in range(len(df.columns))]

def highlight_cells(x):
    return ['background-color: yellow' if cell == '' else '' for cell in x]

styler = df.style.apply(highlight_cells, axis=0)
styler = styler.set_properties(**{'border': '1px solid black'})

styler.to_excel(file_name_output, index=False)