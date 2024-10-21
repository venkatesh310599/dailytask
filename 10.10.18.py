"Write a Python program that reads a list of integers and returns a new list containing only the unique elements (i.e., removing duplicates)."
"Given a list of tuples representing (name, age), sort the list by age in ascending order"

numbers = [int(x) for x in input("Enter a list of integers (space-separated):").split()]
unique_numbers = list(set(numbers))
print(unique_numbers)
people = [
("Rama", 25),
("Sita", 30),
("Shiva", 20),
("Krishna", 28)
]
people_sorted = sorted(people, key=lambda x: x[1])
print( people_sorted)






