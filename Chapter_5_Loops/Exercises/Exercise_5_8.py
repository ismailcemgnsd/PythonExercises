import math
print("{0:<15s}{1:<15s}".format("Number", "Square Root"))

for i in range(0, 21, 2):
    print("{0:<15d}{1:<15.4f}".format(i, math.sqrt(i)))