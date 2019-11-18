def displaySortedNumbers(num1, num2, num3):
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2
    return num1, num2, num3

def main():
    num1, num2, num3 = eval(input("Enter three numbers: "))
    print("The sorted numbers are", displaySortedNumbers(num1, num2, num3))

main()