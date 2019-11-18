rate = eval(input("Enter the exchange rate from dollars to RMB: " ))
option = int(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))

if option == 0:
    amount = eval(input("Enter the dollar amount: "))
    print("$ " + str(amount) + " is " + str(amount*rate) + " yuan")
elif option == 1:
    amount = eval(input("Enter the RMB amount: "))
    print(str(amount) + " yuan is " + str(amount/rate) + " dollars")
else:
    print("Incorrect input!")