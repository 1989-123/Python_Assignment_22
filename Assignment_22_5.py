"""
Write a recursive python function to calculate sum of 
cubes of first N natural numbers 
"""

def sumOfCubes(n):
    if n == 1:
        return 1
    s = (n ** 3) + sumOfCubes(n - 1)
    return s

print()
print("Sum of cubes of first N odd natural numbers is:",sumOfCubes(3))
print()
