"""
Write a recursive python function to print 
binary of a given decimal number.
"""

def binary(n):
    if n == 1:
        return 1
    t1 = binary(n // 2)
    t2 = n % 2
    s = str(t1) + str(t2)
    return s

print()
print("Binary of a given decimal number is:",binary(25))
print()
