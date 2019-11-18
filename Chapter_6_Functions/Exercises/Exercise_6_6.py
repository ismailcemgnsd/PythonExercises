def displayPattern(n):
    for i in range(1, n + 1):
        for space in range(n - i, 0, -1):
            print(" ", end="")
        for number in range(i, 0, -1):
            print(number, end="")
        print()

def main():
    number = eval(input("Enter the number: "))
    displayPattern(number)

main()