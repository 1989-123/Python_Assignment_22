"""
Write a recursive python function to calculate sum of 
first N even natural numbers 
"""

def sumOfEven(n):
    if n == 1:
        return 2
    s = (n * 2) + sumOfEven(n - 1)
    return s

print()
print("Sum of first N even natural numbers is:",sumOfEven(7))
print()
