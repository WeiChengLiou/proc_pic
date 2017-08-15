##
import re
df = {}

with open('meta.log', 'r') as f:
    key = None
    for ln in f.readlines():
        ln = ln.strip()
        if ':' in ln:
            k, v = re.search('(^.*?) +: (.*)', ln).groups()
            df[key][k] = v
        else:
            key = ln
            df[key] = {}

##
import pandas as pd
df = pd.DataFrame(df)
df = df.T.reset_index(drop=True)
df.to_pickle('meta.pkl')

##
