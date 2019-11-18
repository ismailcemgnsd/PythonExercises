tuition = 10000
total = 0
for i in range(1, 15):
    tuition += tuition * 0.05
    if i == 10:
        print("The cost of tuition in 10 years is $ {}".format(tuition))


    if i > 10:
        total += tuition

print("The total cost of 4 years tuition in 10 years is $ {}".format(total))