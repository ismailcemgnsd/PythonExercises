import random

flippedCoin = random.randint(0, 1)
guess = int(input("Guess the flipped coin: "))

if guess == flippedCoin:
    print("Flipped coin is", flippedCoin)
    print("Correct!")
else:
    print("Flipped coin is", flippedCoin)
    print("Sorry, incorrect!")