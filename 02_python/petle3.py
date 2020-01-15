slownik = {1: "Beata", 2: "Miłosz", 3: "Marek", 4: "Marcin", 5: "Łukasz"}
for klucz, wartosc in slownik.items():
    print(klucz, wartosc)

lista = ["Beata", "Miłosz", "Marek", "Marcin", "Łukasz"]
for miejsce, imie in enumerate(lista):
    print(miejsce, imie)

lista2 = [
    ('a', 1),
    ('b', 2),
]
for literka, cyferka in lista2:
    print(literka, cyferka)


for i in range(100):
    pass

# dla liczb 1-100
# wypisz "Fizz" dla podzielnych przez 3
# wypisz "Buzz" dla podzielnych przez 5
# wypisz "FizzBuzz" dla podzielnych przez 15

if "Piotr" in "Piotr Banaszkiewicz":
    print("tak")
