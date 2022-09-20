"""
Write a recursive python function to calculate sum of 
first N odd natural numbers 
"""

def sumOfOdd(n):
    if n == 1:
        return 1
    s = (n * 2 - 1) + sumOfOdd(n - 1)
    return s

print()
print("Sum of first N odd natural numbers is:",sumOfOdd(5))
print()
