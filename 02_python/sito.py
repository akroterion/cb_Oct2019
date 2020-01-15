lista = list(range(2, 101))
L = len(lista)

usuniete = []

for i in range(0, L):
    for n in range(2, 50):
        usuniete.append(lista[i] * n)

print(set(lista) - set(usuniete))

# inny sposób: lista wartości bool
lista = [False] * 101
for i in range(2, 100):  # przechodzimy przez liczby 2..100
    for n in range(2, 50):  # przechodzimy przez mnożniki tych liczb
        if i * n <= 100:
            lista[i * n] = True

# wyświetlamy indeksy tylko dla elementów, które nie zostały wykreślone
# (czyli nie mają wartości True)
for k, v in enumerate(lista):
    if not v:
        print(k, end=' ')
