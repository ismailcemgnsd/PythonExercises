import random

number = random.randint(0, 2)

guess = int(input("scissor (0), rock (1), paper (2): "))

if guess == 0 and number == 0:
    print("The computer is scissor. You are scissor too. It is a draw.")
elif guess == 1 and number == 0:
    print("The computer is scissor. You are rock. You won.")
elif guess == 2 and number == 0:
    print("The computer is scissor. You are paper. You lost.")
elif guess == 1 and number == 1:
    print("The computer is rock. You are rock too. It is a draw.")
elif guess == 0 and number == 1:
    print("The computer is rock. You are scissor. You lost.")
elif guess == 2 and number == 1:
    print("The computer is rock. You are paper. You won.")
elif guess == 2 and number == 2:
    print("The computer is paper. You are paper too. It is a draw.")
elif guess == 0 and number == 2:
    print("The computer is paper. You are scissor. You won.")
elif guess == 1 and number == 2:
    print("The computer is paper. You are rock. You lost.")
