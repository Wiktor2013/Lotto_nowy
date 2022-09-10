"""sciagnanie danych ze strony lotto"""
import pandas as pd
import json
from fake_useragent import UserAgent
import requests
ua = UserAgent()
# print(ua.chrome)
header = {'User-Agent': str(ua.chrome)}
url = 'https://www.lotto.pl/api/lotteries/draw-results/by-gametype?game=Lotto&index=1&size=6800&sort=drawDate&order=DESC'
response = requests.get(url, headers=header)
# print(response.content)
data = json.loads(response.content)
data = data["items"]


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

with open("/home/sanczo/PycharmProjects/Lotto_nowy/by-gametype.json", "w") as f:
    json.dump(data, f)
f.close()

with open("/home/sanczo/PycharmProjects/Lotto_nowy/by-gametype-flat.json", "w") as f:
    json.dump(wyniki, f)
f.close()

df = pd.read_json('/home/sanczo/PycharmProjects/Lotto_nowy/by-gametype-flat.json', typ='frame', convert_dates=True, orient='index')
# df = pd.DataFrame('/home/sanczo/PycharmProjects/Lotto_nowy/by-gametype-flat.json')

print(df)
print(type(df))


