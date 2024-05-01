import pandas as pd
import os

df = pd.read_excel('TPB_CP4I_Namespace_Servers_Details_v0.22.xlsx', sheet_name='ace-esb-ex')

# To get columns I and J from rows 1 to 10
min_replicas_values = df.iloc[0:9, 7].fillna(2).tolist()
max_replicas_values = df.iloc[0:9, 9].fillna(2).tolist()
namespace_values = df.iloc[0:9, 1].tolist()
instance_name_values = df.iloc[0:9, 2].tolist()

# Write output to file
with open('output.txt', 'w') as f:
    for ns, intance, i, j in zip(namespace_values,instance_name_values , min_replicas_values, max_replicas_values):
        f.write(f"{ns.lower()} {intance.lower()} {int(i)} {int(j)}\n")

# Run script genrate file 
os.system('scripts.sh')