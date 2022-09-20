"""
Write a recursive python function to find the 
Nth term of the Fibonacci series
"""


def fib(n):
    a, b, c = -1, 1, 0
    if n == 0:
        return a, b, c
    else:
        i, j, k = fib(n - 1)
        k = i + j
        i = j
        j = k
        print(k, end=" ")
        return i, j, k

print()
fib(10)
