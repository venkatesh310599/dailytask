"Create a list of numbers from 1 to 20. Write a Python program to generate two separate list:"


numbers = list(range(1, 21))
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print( even_numbers)
print(odd_numbers)