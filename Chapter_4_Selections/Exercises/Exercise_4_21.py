y = eval(input("Enter year: (e.g., 2008): "))
m = eval(input("Enter month: 1-12: "))
q = eval(input("Enter the day of the month: 1-31: "))

if m in (1,2):
    m = m + 12
    y = y - 1

j = y / 100
k = y % 100
h = (q + (26 * (m + 1)) / 10 + k + k / 4 + j / 4 + 5 * j) % 7

if h == 0:
    print("Day of the week is Saturday")
elif h == 1:
    print("Day of the week is Sunday")
elif h == 2:
    print("Day of the week is Monday")
elif h == 3:
    print("Day of the week is Muesday")
elif h == 4:
    print("Day of the week is Wednesday")
elif h == 5:
    print("Day of the week is Thursday")
else:
    print("Day of the week is Friday")