import math
print("{0:<10s}{1:<15s}{2:<15s}".format("Degree", "Sin", "Cos"))
for i in range(0, 361, 10):
    print('{0:<10d}{1:<15.4f}{2:<15.4f}'.format(i, math.sin(math.radians(i)), math.cos(math.radians(i))))