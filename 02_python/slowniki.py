# dictionary
# dict()

slownik = {
    'klucz1': 'wartosc',
    (0, 4): 'wartosc',
}

print(slownik)
print(len(slownik))

# nowy element do slownika
slownik['a'] = 'A'
print(slownik)

# zmiana elementu w slowniku
slownik['a'] = 'B'
print(slownik)

# usuwanie elementu
del slownik['a']
print(slownik)

# sprawdzanie czy klucz jest w słowniku
print('a' in slownik)
print( (0, 4) in slownik)
