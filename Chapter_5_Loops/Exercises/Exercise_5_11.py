numberOfStudents = int(input("Enter the number of students: "))
firstScore = 0
secondScore = 0
firstStudent = 0
secondStudent = 0

for i in range(numberOfStudents):
    score = eval(input("Student "+ str(i + 1) + " has the score: "))
    if score > secondScore:
        if score > firstScore:
            firstScore = score
            firstStudent = i
        else:
            secondScore = score
            secondStudent = i
print("The first student is Student", firstStudent + 1, "and the student's score is", firstScore)
print("The second student is Student", secondStudent + 1, "and the student's score is", secondScore)