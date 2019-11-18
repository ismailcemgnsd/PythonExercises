print("Enter weight and price for package 1: ")
weight1 = eval(input())
price1 = eval(input())

print("Enter weight and price for package 2: ")
weight2 = eval(input())
price2 = eval(input())

if weight1 / price1 < weight2 / price2:
    print("Package 1 has the better price")
else:
    print("Package 2 has the better price")