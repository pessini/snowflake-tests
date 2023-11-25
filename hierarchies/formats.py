import pandas as pd
import json

def getJson(df):

    nodes = {}
    for _, row in df.iterrows():
        name = row.iloc[0]
        nodes[name] = { "name": name }

    root = None
    for _, row in df.iterrows():
        node = nodes[row.iloc[0]]
        isRoot = pd.isna(row.iloc[1])
        if isRoot:
            root = node
        else:
            parent = nodes[row.iloc[1]]
            if "children" not in parent:
                parent["children"] = []
            parent["children"].append(node)
    return root

df = pd.read_csv("data/employee-manager.csv", header=0).convert_dtypes()

root = getJson(df)
with open("data/employee-manager.json", "w") as f:
    f.writelines(json.dumps(root, indent=2))
