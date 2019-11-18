def reverse(number):
    reverse = ""
    while number != 0:
        reverse += str(number % 10)
        number //= 10
    return reverse

def main():
    number = int(input("Enter an integer: "))
    print("{0}'s reverse is {1}".format(number, reverse(number)))

main()