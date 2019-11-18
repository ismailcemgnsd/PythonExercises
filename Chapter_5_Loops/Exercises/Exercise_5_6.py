print("{0:<15s}{1:<10s}   |   {2:<15s}{3:<10s}".format("Miles", "Kilometers", "Kilometers", "Miles"))
kilometers = 20
for i in range(1, 11):
    print('{0:<15d}{1:<8.3f}     |   {2:<15d}{3:<10.3f}'.format(i, i * 1.609, kilometers, kilometers * 0.621))
    kilometers += 5