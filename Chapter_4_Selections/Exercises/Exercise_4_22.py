x, y = eval(input("Enter a point with two coordinates: "))
RADIUS = 10
d = ((x - 0) ** 2 + (y - 0) ** 2) ** 0.5
if d <= 10:
    print("Point ({}, {}) is in the circle".format(x, y))
else:
    print("Point ({}, {}) is not in the circle".format(x, y))