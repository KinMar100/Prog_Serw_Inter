import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import requests
from bs4 import BeautifulSoup

"""ZADANIE 1
Przygotować funkcję check_url(url: str) -> bool, która przyjmie adres URL i zwróci wartość logiczną informującą o tym
czy serwer zwrócił odpowiedź poprawną. Za odpowiedź poprawną należy uznać taką, której kod mieści się w zakresie
200-299."""


def check_url(url: str) -> bool:
    response = requests.get(url)
    stat_code = response.status_code
    if 200 <= stat_code <= 299:
        return True
    else:
        return False


print(check_url('https://www.sinsay.com/pl/pl/sale/woman/clothes/view-all?baner=P1_sale-aw21_W&place=promobar'))
print(check_url('https://www.facebook.com'))


""" ZADANIE 2
Przygotować kod, który dla wskazanej nazwy miejscowości wygeneruje liniowy wykres temperatury dla najbliższych godzin.
Jako źródło danych można wykorzystać adres: https://www.meteoprog.pl/pl/weather/NazwaMiasta/,
gdzie frazę NazwaMiasta należy zastąpić właściwą nazwą miasta/miejscowości.
Przy implementacji rozwiązania proszę wykorzystać bibliotekę BeautifulSoup. Do wizualizacji można wykorzystać dowolne
narzędzie."""

city = 'Olsztyn'
url = f'https://www.meteoprog.pl/pl/weather/{city}/'
resp = requests.get(url)

soup = BeautifulSoup(resp.content, features='html.parser')
table = soup.find_all('span', class_='today-hourly-weather__temp')

tablica_temp = []
ilosc = 0

for temp in table:
    bez_plusC = int(temp.text.replace("°", "").replace("+", ""))
    tablica_temp.append(bez_plusC)
    ilosc = ilosc + 1


x = 0.5 + np.arange(ilosc)

y = tablica_temp

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.5, color='blueviolet')
ax.set(xlim=(0, 6), xticks=np.arange(1, 6),
       ylim=(0, 20), yticks=np.arange(1, 20))


plt.xlabel("Kolejne pory dla temperatur")
plt.ylabel("Wartość")
plt.title(f'Wykres temperatur dla miejscowości: {city}')
plt.show()

# print(table)

""" ZADANIE 3 
Przygotować kod, który wygeneruje wieloserjny wykres liniowy wartości odczytów wybranych czujników wybranej stacji
 pomiarowej z ostatnich godzin. Jako źródło danych wykorzystać API GIOŚ."""



""" ZADANIE 4
Która z automatycznych metod ekstrakcji informacji z aplikacji internetowych jest wygodniejsza?"""
