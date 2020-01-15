# 1
# komputer losuje liczbę z zakresu 1..100
# człowiek musi zgadnąć, korzystając ze wskazówek komputera, jaka to liczba

import random
liczba = random.randint(1, 100)

zgadniecie = 9999
proby = 1

while (zgadniecie != liczba and proby <= 7):
    try:
        zgadniecie = int(input("Zgadnij liczbę: "))
    except ValueError:
        print("Podaj prawdziwą liczbę")
        continue

    if not (1 <= zgadniecie <= 100):
        print("Oszukujesz!")
    elif zgadniecie > liczba:
        print("MNIEJ")
    elif zgadniecie < liczba:
        print("WIECEJ")
    proby += 1


# 2
# napisz program, który ma pętlę nieskończoność i nie da się go wyłączyć
# użyj łapania wyjątków i wyjątku KeyboardInterrupt
