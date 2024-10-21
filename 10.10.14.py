"Write a Python program to check if a specific element (e.g., 5) exists in a given list using the in operator. If it exists, print its position; otherwise, print Element not found"


numbers = [1, 2, 3, 4, 5]
if 5 in numbers:
    print( numbers.index(5))
else:
    print("Element not found")
students = ["John", "Sara", "Emily", "Michael"]
if "John" in students and "Sara" in students:
    print("Both John and Sara are in the list.")
else:
    print("One or both of John and Sara are not in the list")