numberOfStudent = int(input("Enter number of students: "))
maxScore = 0
maxScoreIndex = 0
for i in range(numberOfStudent):
    studentScores = int(input("Enter student's scores: "))
    if studentScores > maxScore:
        maxScore = studentScores
        maxScoreIndex = i

print("Student", maxScoreIndex + 1, "has maximum score:", maxScore)
