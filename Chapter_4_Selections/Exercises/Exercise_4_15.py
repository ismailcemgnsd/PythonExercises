import random
# Generate a lottery number
lottery = random.randint(0, 999)
# Prompt the user to enter a guess
print(lottery)
guess = eval(input("Enter your lottery pick (three digits): "))

# Get digits from lottery
lotteryDigit1 = lottery // 100
remainingLotteryDigit = lottery % 100
lotteryDigit2 = remainingLotteryDigit // 10
lotteryDigit3 = remainingLotteryDigit % 10
# Get digits from guess
guessDigit1 = guess // 100
remainingGuessDigit = guess % 100
guessDigit2 = remainingGuessDigit // 10
guessDigit3 = remainingGuessDigit % 10
print("The lottery number is", lottery)
# Check the guess
if guess == lottery:
    print("Exact match: you win $10,000")
elif (guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2 or guessDigit1 == lotteryDigit3) and (guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2 or guessDigit2 == lotteryDigit3) and (guessDigit3 == lotteryDigit1 or guessDigit3 == lotteryDigit2 or guessDigit3 == lotteryDigit3):
    print("Match all digits: you win $3,000")
elif guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2 or guessDigit1 == lotteryDigit3 or guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2 or guessDigit2 == lotteryDigit3 or guessDigit3 == lotteryDigit1 or guessDigit3 == lotteryDigit2 or guessDigit3 == lotteryDigit3:
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")