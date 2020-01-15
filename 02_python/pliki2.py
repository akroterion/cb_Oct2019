import csv
import math

lata = []
wyniki = []
tytuly = []

# 1. odczyt
with open('przykladowy.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # 2. przetworzenie na zjadliwą formę
        lata.append(int(row['Year']))
        wyniki.append(int(row['Score']))
        tytuly.append(row['Title'])

# 1. odczyt danych (jw.)
# 2. przetworzenie na zjadliwą formę (proponuję 3 listy: lat, wyników i tytułów)
#    (nie zapomnijcie o int())
# 3. znajdź tytuł z najniższym wynikiem, najwyższym, znajdź średnią wyników, medianę

max = wyniki[0]
max_i = 0
min = wyniki[0]
min_i = 0
for i, wynik in enumerate(wyniki):
    if wynik > max:
        max = wynik
        max_i = i
    if wynik < min:
        min = wynik
        min_i = i

print(min, max)
print(wyniki[min_i], wyniki[max_i])
print(min_i, max_i)

s_wyniki = sorted(wyniki)  # posortuj wyniki, żeby móc obliczyć medianę

index = (len(s_wyniki) - 1) // 2
mediana = s_wyniki[index]

index_dolny = int(math.floor(index))
index_gorny = int(math.ceil(index))
mediana = (s_wyniki[index_dolny] + s_wyniki[index_gorny]) / 2
print(mediana)
# jeżeli liczba elementów w liście `s_wyniki` jest nieparzysta
# to indeks środkowego elementu: (len(s_wyniki) - 1) / 2

# jeżeli liczba elementów w liście `s_wyniki` jest parzysta,
# to indeksy środkowych elementów: floor((len(s_wynik) - 1) / 2), ceil((len(s_wynik) - 1) / 2)

