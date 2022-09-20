"""
Write a recursive python function to calculate sum of 
squares of first N natural numbers 
"""

def sumOfSquares(n):
    if n == 1:
        return 1
    s = (n ** 2) + sumOfSquares(n - 1)
    return s

print()
print("Sum of squares first N odd natural numbers is:",sumOfSquares(3))
print()
