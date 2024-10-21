"Create a nested list representing a list of students' names and their respective grades. Write a Python program to print each student's name along with their grade"



students = [
    ["Ram", 85, 90, 78],
    ["Shiva", 92, 88, 95],
    ["Narayan", 70, 80, 90],
    ["Krishna", 90, 85, 92]
]
for student in students:
    print("Student:", student[0])
    print("Grades:", student[1:])