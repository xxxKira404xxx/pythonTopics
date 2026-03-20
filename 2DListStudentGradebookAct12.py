# 1. Create a 2D list called gradebook with 4 students
# Each row: [name, quiz1, quiz2, quiz3]
gradebook = [
    ["Ana", 85, 90, 88],
    ["Ben", 78, 82, 80],
    ["Carl", 92, 87, 91],
    ["Dina", 88, 85, 84]
]

# 3. Print the entire gradebook
print("Gradebook:")
for student in gradebook:
    print(student)

# 4. Access and print the 2nd student's quiz2 score
print("\n2nd student's quiz2 score:", gradebook[1][2])

# 5. Update the 3rd student's quiz1 score to 100
gradebook[2][1] = 100

# 6. Add a new student row to the gradebook
gradebook.append(["Eli", 90, 93, 89])

# 7. Print the updated gradebook
print("\nUpdated Gradebook:")
for student in gradebook:
    print(student)