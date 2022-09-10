#!usr/bin/env python3
# -*- coding: utf-8 -*-
import random

ileliczb = int(input("Podaj ilosc liczb do wylosowania "))
maksliczba = int(input("Podaj maksymalną liczbę do wylosowania "))
print()
print(f'Wytypuj {ileliczb} z {maksliczba} liczb')
liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1
print(f'Wylosowane liczby: {liczby}')