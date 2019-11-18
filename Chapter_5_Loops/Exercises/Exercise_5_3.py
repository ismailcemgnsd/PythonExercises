
print("{0:<15s}{1:>10s}".format("Kilograms", "Pounds"))
for i in range(1, 200, 2):
    print('{0:<20d}{0:<10.1f}'.format(i, i * 2.2))
