x, y = eval(input("Enter a point with two coordinates: "))
WIDTH = 10
HEIGHT = 5

d = ((x - 0) ** 2 + (y - 0) ** 2) ** 0.5
if (x ** 2) ** 0.5 <= WIDTH / 2 and (y ** 2) ** 0.5 <= HEIGHT / 2:
    print("Point ({}, {}) is in the circle".format(x, y))
else:
    print("Point ({}, {}) is not in the circle".format(x, y))
