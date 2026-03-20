# Student Grade Management Program

# 1. Store at least 5 students with 4 quiz scores each
students = [
    ["Alice", [85, 90, 78, 92]],
    ["Bob", [70, 75, 80, 65]],
    ["Charlie", [95, 85, 88, 90]],
    ["David", [60, 68, 72, 70]],
    ["Eva", [88, 92, 85, 91]]
]

# 2. Display all students and their grades in a table format
print("Student Grades:")
print("Name      Quiz1  Quiz2  Quiz3  Quiz4")
for student in students:
    name = student[0]
    grades = student[1]
    print(f"{name:<9}", end=" ")
    for grade in grades:
        print(f"{grade:<7}", end=" ")
    print()

# 3. Calculate and display each student's average
print("\nStudent Averages:")
highest_avg = 0
top_student = ""
for student in students:
    name = student[0]
    grades = student[1]
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)
    print(f"{name}: {average:.2f}")
    
    # Track highest average
    if average > highest_avg:
        highest_avg = average
        top_student = name

# 4. Display the student with the highest average
print(f"\nTop student: {top_student} with average {highest_avg:.2f}")

# 5. Find the highest and lowest scores across all quizzes
highest_score = -1
lowest_score = 101
for student in students:
    for grade in student[1]:
        if grade > highest_score:
            highest_score = grade
        if grade < lowest_score:
            lowest_score = grade

print(f"Highest score across all quizzes: {highest_score}")
print(f"Lowest score across all quizzes: {lowest_score}")

# 6. Add a new student to the gradebook
new_student_name = "Frank"
new_student_grades = [82, 77, 90, 85]
students.append([new_student_name, new_student_grades])
print(f"\nAdded new student: {new_student_name}")

# 7. Update a specific student's quiz score
student_to_update = "Bob"
quiz_index = 2  
new_score = 95
for student in students:
    if student[0] == student_to_update:
        student[1][quiz_index] = new_score
        print(f"Updated {student_to_update}'s Quiz{quiz_index+1} score to {new_score}")

# Display updated gradebook
print("\nUpdated Student Grades:")
print("Name      Quiz1  Quiz2  Quiz3  Quiz4")
for student in students:
    name = student[0]
    grades = student[1]
    print(f"{name:<9}", end=" ")
    for grade in grades:
        print(f"{grade:<7}", end=" ")
    print()