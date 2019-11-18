def sumDigits(n):
    temp = abs(n)
    sum = 0
    while temp != 0:
        sum += temp % 10
        temp = temp // 10
    return sum

def main():
    number = int(input("Enter an integer: "))
    print(sumDigits(number))
    
main()


