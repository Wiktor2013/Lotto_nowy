"""sciagnanie danych ze strony lotto"""
import json
from fake_useragent import UserAgent
import requests
ua = UserAgent()
print(ua.chrome)
header = {'User-Agent':str(ua.chrome)}
url = 'https://www.lotto.pl/api/lotteries/draw-results/by-gametype?game=Lotto&index=1&size=6625&sort=drawDate&order=DESC'
response = requests.get(url, headers=header)
#print(response.content)
#data = json.loads(response.content)
data = json.loads(response.content)["items"]

# def flatten_json(y):
#     out = {}
#     def flatten(x, name=''):
#         if type(x) is dict:
#             for a in x:
#                 flatten(x[a], name + a + "_")
#         elif type(x) is list:
#             i = 0
#             for a in x:
#                 flatten(a, name + str(i) + "_")
#                 i+=1
#         else:
#             out[name[:-1]] = x
#     flatten(y)
#     return out

with open("/home/sanczo/PycharmProjects/Lotto_nowy/by-gametype.json", "w") as f:
    json.dump(data, f)