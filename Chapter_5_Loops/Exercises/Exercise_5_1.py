
number = int(input("Enter an integer, the input ends if it is 0: "))
total = 0
countPos = 0
countNeg = 0
count = 0

if number == 0:
    print("You didn't enter any number")
else:
    while number != 0:
        if number > 0:
            countPos += 1
        else:
            countNeg += 1
        count += 1
        total += number
        number = int(input("Enter an integer, the input ends if it is 0: "))
    average = total / count


    print("The number of positives is", countPos)
    print("The number of positives is", countNeg)
    print("The total is", total)
    print("The average is", average)