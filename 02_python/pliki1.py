# w - write (* - nadpisuje całą zawartość pliku)
# a - append
# r - read

# t - text
# b - binary

# 1. otwarcie pliku
# 2. działania na pliku
# 3. zamknięcie pliku

# f = open('dane.txt', 'r', encoding='utf-8')
# f.close()

tekst = "Nazywam sie Piotr Banaszkiewicz"

with open('dane2.txt', 'w', encoding='utf-8') as f:  # context manager
    f.write(tekst)

with open('dane2.txt', 'r', encoding='utf-8') as f:
    print(f.read())
