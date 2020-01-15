# sprawdz czy string jest palindromem

slowo = "kajac"
dl = len(slowo)  # długość stringa

czy_palindrom = True

for i in range(dl):
    if slowo[0] != slowo[dl - (i + 1)]:
        print("to nie jest palindrom")
        czy_palindrom = False
        break

if czy_palindrom:
    print("To jest palindrom")
