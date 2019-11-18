amount = eval(input("Enter an amount, for example, 11.56: "))

remainingAmount = int(amount * 100)

numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

numberOfPennies = remainingAmount

print("Your amount", amount, "consists of", numberOfOneDollars, "dollar" if (numberOfOneDollars == 1) else "dollars", numberOfQuarters, "quarter" if (numberOfQuarters == 1) else "quarters", numberOfDimes, "dime" if (numberOfDimes == 1) else "dimes", numberOfNickels, "nickle" if (numberOfNickels == 1) else "nickles", numberOfPennies, "penny" if (numberOfPennies == 1) else "pennies")