"""
Write a recursive python function to print 
octal of a given decimal number.
"""

def Oct(n):
    if n == 1:
        return 1
    t1 = Oct(n // 8)
    t2 = n % 8
    s = str(t1) + str(t2)
    return s

print()
print("Octal of a given decimal number is:",Oct(89))
print()
