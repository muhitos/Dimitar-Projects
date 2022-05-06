# Алгоритъм Евклид

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b


print("НОД число 30, 18 = ", gcd(30, 18))

#---------------------------------------------
import math

print(math.gcd(30,18))
