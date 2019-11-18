def reverse(number):
    reverse = ""
    while number != 0:
        reverse += str(number % 10)
        number //= 10
    return reverse

def isPalindrome(number):
    if number == int(reverse(number)):
        return True
    return False

def main():
    number = int(input("Enter an integer: "))
    print("The reversed number is {}".format(reverse(number)))
    print(number, "is a palindrome" if (isPalindrome(number)) else "is not a palindrome")
main()