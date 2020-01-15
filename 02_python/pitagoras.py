def pit(a, b):
    c = (a ** 2 + b ** 2) ** .5
    return c


przeciwprostokatna = pit(3, 4)
print(przeciwprostokatna)


# zad1: napisz funkcję liczącą średnią arytmetyczną (przyjmuje 1 argument: listę)
# zad2: napisz funkcję liczącą pierwiastki równania kwadratowego (przyjmuje 3 argumenty: a, b, c)
#       ax^2 + bx + c -> delta = b^2 - 4ac, x1 = (sqrt(delta) - b) / 2a
#                                           x2 = (-sqrt(delta) - b) / 2a
# zad3: zaimplementuj silnię rekurencyjnie
def silnia(n):
    if n == 1:
        return 1
    else:
        return n * silnia(n - 1)
