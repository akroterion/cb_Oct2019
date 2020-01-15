# pobierz od użytkownika 6 liczb losowych do losowania totolotka
# 1. użyj pętli while
# 2. upewnij się, że liczby się nie powtarzają
# 3. upewnij się, że liczby są w zakresie 1-49
# 4*. jeżeli liczba jest poza zakresem [1, 49], przerwij pętlę

# składnia petli while
# while WARUNEK:
#     pass

# pamiętajcie o poleceniach:
# break  # przerywa obecne wykonanie pętli
# continue  # przerywa obecne wykonanie pętli i przechodzi do nast. iteracji


# rozwiązanie:

lotek = []

while len(lotek) < 6:
    liczba = int(input('Podaj liczbę: '))

    if not (1 <= liczba <= 49):
        print("Nie probuj mnie oszukać!")
        break

    if liczba not in lotek:
        lotek.append(liczba)

print("Wylosowane dzisiaj liczby:")
print(lotek)
