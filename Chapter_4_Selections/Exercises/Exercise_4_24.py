import random

rank = random.randint(1, 13)
suit = random.randint(1, 4)

if rank == 1:
    rank = "Ace"
elif rank == 11:
    rank = "Jack"
elif rank == 12:
    rank = "Quenn"
elif rank == 13:
    rank = "King"


if suit == 1:
    suit = "Clubs"
elif suit == 2:
    suit = "Diamonds"
elif suit == 3:
    suit = "Hearts"
elif suit == 4:
    suit = "Spades"



print("The card you picked is the {} of {}".format(rank, suit))