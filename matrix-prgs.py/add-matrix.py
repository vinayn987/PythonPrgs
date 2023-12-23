import numpy as np

def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Take user input for each element
            element = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
            row.append(element)
        matrix.append(row)
    return matrix


# Input for the first matrix
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
print("Enter elements for the first matrix:")
matrix1 = input_matrix(rows1, cols1)

# Input for the second matrix
rows2 = int(input("\nEnter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))
print("Enter elements for the second matrix:")
matrix2 = input_matrix(rows2, cols2)

# Display the matrices
print("\nFirst Matrix:")
for row in matrix1:
    print(row)

A = np.array([matrix1])
print("\nSecond Matrix:")
for row in matrix2:
    print(row)

B = np.array([matrix2])

print("Matrix Addition:")
add = A+B
result = add[0] # this reduces number of brackets
print(result)
    
