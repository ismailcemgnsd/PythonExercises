today = eval(input("Enter today's day:"))
elapsedDay = eval(input("Enter the number of days elapsed since today:"))

futureDay = (today + elapsedDay) % 7

if today == 0:
    today = "Sunday"
elif today == 1:
    today = "Monday"
elif today == 2:
    today = "Tuesday"
elif today == 3:
    today = "Wednesday"
elif today == 4:
    today = "Thursday"
elif today == 5:
    today = "Friday"
else:
    today = "Saturday"

if futureDay == 0:
    futureDay = "Sunday"
    print("Today is", today, "and the future day is", futureDay)
elif futureDay == 1:
    futureDay = "Monday"
    print("Today is", today, "and the future day is", futureDay)
elif futureDay == 2:
    futureDay = "Tuesday"
    print("Today is", today, "and the future day is", futureDay)
elif futureDay == 3:
    futureDay = "Wednesday"
    print("Today is", today, "and the future day is", futureDay)
elif futureDay == 4:
    futureDay = "Thursday"
    print("Today is", today, "and the future day is", futureDay)
elif futureDay == 5:
    futureDay = "Friday"
    print("Today is", today, "and the future day is", futureDay)
else:
    futureDay = "Saturday"
    print("Today is", today, "and the future day is", futureDay)
