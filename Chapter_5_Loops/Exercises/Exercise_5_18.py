number = int(input("Enter an integer: "))
factor = 2
while number / factor != 1:
    if number % factor == 0:
        print(factor, end=", ")
        number /= factor
    else:
        factor += 1
print(int(number))
