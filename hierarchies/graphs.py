import pandas as pd
df = pd.read_csv("data/employee-manager.csv", header=0).convert_dtypes()

edges = ""
for _, row in df.iterrows():
    if not pd.isna(row.iloc[1]):
        edges += f'\t{row.iloc[0]} -> {row.iloc[1]}\n'
graph = f'digraph {{\n{edges}}}'
print(graph)

import webbrowser, urllib.parse
editor = 'http://magjac.com/graphviz-visual-editor/'
url = f'{editor}?dot={urllib.parse.quote(graph)}'
webbrowser.open(url)
