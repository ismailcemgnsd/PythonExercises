def getPentagonalNumber(n):
    pentagonalNumber = int(n * (3 * n - 1) / 2)
    return pentagonalNumber

def main():
    
    count = 0
    for i in range(101):
        print(getPentagonalNumber(i), end=" ")
        count += 1
        if count % 10 == 0:
            print()

main()