# Your code appears to be designed to take a list of student heights as input,
# calculate the total height, the number of students, and then compute the average height

student_heights = input("provide a list of numbers seperated by a space or comma: ").split()
for n in range(len(student_heights)):
    student_heights[n] = int(student_heights[n])

# calculate the total height
total_height = 0
for height in student_heights:
    total_height += height
print(f"Total Height = {total_height}")

# calculate the number of students
num_students = 0
for num in student_heights:
    num_students += 1
print(f"Number of Students = {num_students}")

# calculate the average height of students
average_height = round(total_height / num_students)
print(f"Average height = {average_height}")
