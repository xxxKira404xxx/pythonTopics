# 1. Create a 3x3 matrix (2D list) with numbers 1-9
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. Print the matrix row by row using nested loops
print("Matrix:")
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

# 3. Calculate and print the sum of each row
print("\nRow sums:")
for i in range(len(matrix)):
    row_sum = sum(matrix[i])
    print(f"Row {i+1} sum:", row_sum)

# 4. Calculate and print the sum of each column
print("\nColumn sums:")
for col in range(len(matrix[0])):
    col_sum = 0
    for row in range(len(matrix)):
        col_sum += matrix[row][col]
    print(f"Column {col+1} sum:", col_sum)

# 5. Find and print the diagonal elements (1, 5, 9)
print("\nDiagonal elements:")
for i in range(len(matrix)):
    print(matrix[i][i], end=" ")

# 6. Print a 5-row right triangle star pattern
print("\n\nRight triangle pattern:")
for i in range(1, 6):
    print("*" * i)