# dzialajacy skrypt do lotto ze stronki z wynikami
# pierwsza wersja jest w pliku .ipynb

import json
from operator import index

import pandas as pd

# flattening the data in dict
data = json.load(open('by-gametype-sandbox.json'))
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + "_")
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + "_")
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out
wyniki = flatten_json(data)
#print(wyniki)
df = pd.DataFrame(wyniki, index=list(range(len(wyniki))))
#print(data)
print(df)
df.to_csv("df.csv")