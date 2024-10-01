import json
import pandas as pd
with open("by-gametype.json") as my_file:
    #print(my_file.read())
    data = json.load(my_file)
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
print(wyniki)

with open("/home/PycharmProjects/Lotto_nowy/by-gametype-flat.json", "w") as f:
    json.dump(wyniki, f)
f.close()

df = pd.read_json('/home/PycharmProjects/Lotto_nowy/by-gametype-flat.json', typ='frame', convert_dates=True, orient='index')
# df = pd.DataFrame('/home/sanczo/PycharmProjects/Lotto_nowy/by-gametype-flat.json')

print(df)
print(type(df))