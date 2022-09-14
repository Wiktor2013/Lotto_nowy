#!usr/bin/env python3
# -*- coding: utf-8 -*-
import random

ilosc_losowan = int(input("Podaj liczbę losowań "))
def lotto_generator(x, y):
    x = 6
    y = 49
    liczby = []
    i = 0
    while i < x:
        liczba = random.randint(1, y)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i = i + 1
    return liczby


for i in range(1, ilosc_losowan+1):
    print(f'Typuję 6 z 49 liczb, Losuję {i} raz')
    print(lotto_generator(6, 49))
    print()



