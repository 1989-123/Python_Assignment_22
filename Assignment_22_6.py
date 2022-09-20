"""
Write a recursive python function to calculate 
the factorial of a number.
"""

def factorial(f):
    if f == 1:
        return 1
    t = f * factorial(f - 1)
    return t

print()
print("Factorial of a number is:",factorial(4))
print()
