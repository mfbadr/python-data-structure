__author__ = 'mikeybadr'

def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
