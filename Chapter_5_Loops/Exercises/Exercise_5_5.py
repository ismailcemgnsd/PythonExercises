print("{0:<15s}{1:<10s}   |   {2:<15s}{3:<10s}".format("Kilograms", "Pounds", "Pounds", "Kilograms"))
pounds = 20
for i in range(1, 200, 2):
    print('{0:<15d}{1:<9.1f}    |   {2:<18d}{3:<10.2f}'.format(i, i * 2.2, pounds, pounds * 0.4545))
    pounds += 5