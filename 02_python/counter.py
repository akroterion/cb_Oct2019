tekst = "lorumipsemsitdolor"
# policz wystąpienia każdej literki
# wynik w słowniku

# slownik = {}
# slownik = dict()

# "a" in slownik
# slownik["a"] = 1
# slownik["a"] += 1  # slownik["a"] = slownik["a"] + 1

# 3 sposoby na rozwiązanie:
# 1. liczenie + słownik + warunki jw.
# 2. collections.defaultdict
# 3. collections.Counter
slownik = {}
for literka in tekst:
    if literka in slownik:
        slownik[literka] += 1
    else:
        slownik[literka] = 1

print(slownik)
