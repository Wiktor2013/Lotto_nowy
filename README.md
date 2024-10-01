Początkowo skrypcik ściągał dane z https://www.lotto.pl/api/lotteries/draw-results/by-gametype?game=Lotto&index=1&size=6800&sort=drawDate&order=DESC do manipulowania nimi. 
Ale odkąd Lotto wprowadziło na tej stronie mechanizm weryfikacji Cloudflare, trzeba teraz ściągnąć sobie dane samemu do pliku by-gametype.json i się nimi bawić.
Pliki zawierają różne metody ściagania danych, urllib, selenium itp. Żaden obecnie nie działa w moich rękach.
