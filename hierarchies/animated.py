import pandas as pd
df = pd.read_csv("data/employee-manager.csv", header=0).convert_dtypes()

import formats
root = formats.getJson(df)

with open("animated/collapsible-tree-template.html", "r") as file:
    content = file.read()

import json
content = content.replace('"{{data}}"', json.dumps(root, indent=2))

import os
filename = os.path.abspath("animated/collapsible-tree.html")
with open(filename, "w") as file:
    file.write(content)

import webbrowser
webbrowser.open(filename)