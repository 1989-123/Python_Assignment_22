"""
Write a recursive python function to calculate 
sum of the digits of a given number 
"""

def sumOfDigits(n):
    if n == 1:
        return 1
    s = (n % 10) + sumOfDigits(n // 10)
    return s

print()
print("Sum of the digits of a given number is:",sumOfDigits(16843))
print()
