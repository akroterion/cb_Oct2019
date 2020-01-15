liczby = [5, 7, 11, 15, 18, 24, 32]
wagi = [1, 3, 2, 1, 3, 3, 1]

licznik = 0
mianownik = 0

for i in range(len(wagi)):
    licznik += liczby[i] * wagi[i]
    mianownik += wagi[i]

print(licznik / mianownik)
