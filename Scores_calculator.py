# You are going to write a program that calculates the highest score from a List of scores.
students_scores = input("please input the students scores: ").split()
for n in range(len(students_scores)):
    students_scores[n] = int(students_scores[n])

# assign a variable to the index of students scores
# max_score = students_scores[0]
max_score = 0
for score in students_scores:
    if score > max_score:
        max_score = score
print(max_score)