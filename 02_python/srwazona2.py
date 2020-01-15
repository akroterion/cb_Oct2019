liczby = [5, 7, 11, 15, 18, 24, 32]
wagi = [1, 3, 2, 1, 3, 3, 1]

licznik = 0
mianownik = 0

for liczba, waga in zip(liczby, wagi):
    licznik += liczba * waga
    mianownik += waga

print(licznik / mianownik)
