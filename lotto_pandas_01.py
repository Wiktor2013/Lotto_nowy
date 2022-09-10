import urllib.request, json
from fake_useragent import UserAgent
ua = UserAgent()
#print(ua.chrome)
header = {'User-Agent':str(ua.chrome)}
with urllib.request.urlopen("https://www.lotto.pl/api/lotteries/draw-results/by-gametype?game=Lotto&index=1&size=6800&sort=drawDate&order=DESC") as url:
    data = json.loads(url.read().decode())
print(data)