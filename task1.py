import math
a = int(input())
b = int(input())
c = int(input())
if (a + b > c) and (b + c > a) and (a + c > b):
    p = a + b + c
    h = p / 2
    s = math.sqrt(h * (h - a) * (h - b) * (h - c))
    if s>0:
        print("Периметр:", p)
else:
    print("Невозможно построить! ")

