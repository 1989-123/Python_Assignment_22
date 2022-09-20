"""
 Write a recursive python function to calculate 
sum of first N natural numbers 
"""


def sumNnumber(n):
    if n == 1:
        return 1
    s = n + sumNnumber(n - 1)
    return s


print()
print("Sum of first N natural number is:",sumNnumber(5))
print()
