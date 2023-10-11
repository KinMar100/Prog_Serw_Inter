import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


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


city = 'Warszawa'
urll = f'https://www.meteoprog.pl/pl/weather/{city}/'
resp = requests.get(urll)

soup = BeautifulSoup(resp.content, features='html.parser')
names = soup.find_all('span', class_='today-hourly-weather__name')
print(names)
table = soup.find_all('span', class_='today-hourly-weather__temp')

tablica_temp = []
ilosc = 0
tablica_nazw = []
for name in names:
    print(name.text)
    tablica_nazw.append(name.text)

print(tablica_nazw)


for temp in table:
    bez_plusC = int(temp.text.replace("°", "").replace("+", ""))
    tablica_temp.append(bez_plusC)
    ilosc = ilosc + 1

x = 0.5 + np.arange(ilosc)

y = tablica_temp


fig, ax = plt.subplots()

# wykres slupkowy
'''ax.bar(x, y, width=1, edgecolor="white", linewidth=0.5, color='blueviolet')
ax.set(xlim=(0, 6), xticks=np.arange(1, 6),
       ylim=(0, 20), yticks=np.arange(1, 25))
       '''

# wykres liniowy

ax.plot(x, y, linewidth=2.0)
ax.set(xlim=(0, 6), xticks=np.arange(1, 6),
       ylim=(0, 20), yticks=np.arange(1, 25))
plt.xlabel("Kolejne pory dla temperatur")
plt.ylabel("Wartość")
plt.title(f'Wykres temperatur dla miejscowości: {city}')
plt.show()


""" ZADANIE 3 
Przygotować kod, który wygeneruje wieloserjny wykres liniowy wartości odczytów wybranych czujników wybranej stacji
 pomiarowej z ostatnich godzin. Jako źródło danych wykorzystać API GIOŚ."""


urlll = ""
""" ZADANIE 4
Która z automatycznych metod ekstrakcji informacji z aplikacji internetowych jest wygodniejsza?"""
