# set

zbior = {'a', 'b', 1, 2, 5, 'C'}
inny_zbior = {'b', 1, 5, 'D', 'X', 3}

# operacje matematyczne na zbiorach
zbior.isdisjoint(inny_zbior)  # zbiory nie mają el. wspólnych
zbior < inny_zbior  # .issubset(inny_zbior), mocny warunek, podzbiór
zbior <= inny_zbior  # lekki warunek
zbior > inny_zbior  # .issuperset(inny_zbior), mocny warunek, nadzbiór
zbior >= inny_zbior  # lekki warunek
zbior == inny_zbior

zbior | inny_zbior  # suma zbiorów
zbior & inny_zbior  # iloczyn zbiorów (tylko el. wspólne)
zbior - inny_zbior  # różnica zbiorów
zbior ^ inny_zbior  # symetryczna różnica zbiorów
