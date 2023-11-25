import pandas as pd
df = pd.read_csv("data/employee-manager.csv", header=0).convert_dtypes()
labels = df[df.columns[0]]
parents = df[df.columns[1]]
print(df)

import plotly.graph_objects as go

# see https://plotly.com/python/treemaps/
data = go.Treemap(
    ids=labels,
    labels=labels,
    parents=parents,
    root_color='lightgrey'
)
fig = go.Figure(data)
fig.write_html('charts/treemap.html')
fig.show()

# see https://plotly.com/python/sunburst-charts/
data = go.Sunburst(
    ids=labels,
    labels=labels,
    parents=parents,
    insidetextorientation='horizontal'
)
fig = go.Figure(data)
fig.write_html('charts/sunburst.html')
fig.show()
