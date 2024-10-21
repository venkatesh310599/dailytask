"prite a Python program to create a 3x3 matrix (nested list) and print the matrix. Then, access and print the element at row 2, column 3"

x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in x:
    print(row)
    print("Element at row 2, column 3:", x[2][2])