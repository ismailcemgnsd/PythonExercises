print("Enter a, b, c, d, e, f:")
a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
e = eval(input())
f = eval(input())

check = a * d - b * c

if check == 0:
    print("The equation has no solution")

else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print("x is", x, "and y is", y)