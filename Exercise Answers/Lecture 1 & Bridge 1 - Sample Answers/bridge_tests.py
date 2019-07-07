import math

for i in [abs(5), abs(-5), 10**(1/2), pow(10, 1/2), 5**3, pow(5, 3), 25**(1/2),
          math.sqrt(25), round(25.51), round(25.49), bin(10), hex(10), "4,200".isdigit(),
          "Regal Title".istitle(), "PeasantTitle".istitle(), str(10), int(10),
          float(10), len("string"), bool(10 % 2)]:
    print(i)
    print(type(i))
