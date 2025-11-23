from os import remove

N = int(input("N = "))
a = int(input("a = "))
b = int(input("b = "))
import math

countA = N // a
countB = N // b
lcm_ab = a * b // math.gcd(a, b)
countAB = N // lcm_ab

# Số bóng vàng
yellow = N - countA - countB + countAB

print(yellow)