a, b, c = eval(input("Enter three edges: "))

if a + b > c and a + c > b and b + c > a:
    print("The perimeter is", a + b +c)
else:
    print("The input is invalid")