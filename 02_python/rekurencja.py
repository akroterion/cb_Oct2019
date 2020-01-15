# napisz funkcję liczącą n-ty wyraz ciągu Fibonacciego
# fib(n) = fib(n-1) + fib(n-2) dla n > 1
# fib(n) = n                   dla n <= 1

def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return n

print(fib(6))
