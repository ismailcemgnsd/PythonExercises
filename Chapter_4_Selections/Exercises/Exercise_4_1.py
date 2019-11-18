print("Enter a, b, c:")
a = eval(input())
b = eval(input())
c = eval(input())

discriminant = b ** 2 - 4 * a * c
if(discriminant > 0):
    r1 = (- b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
    r2 = (- b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
    print("The roots are", r1, "and", r2)
elif(discriminant == 0):
    r = - b / 2 * a
    print("The root is", r)
else:
    print("The equation has no real roots")

