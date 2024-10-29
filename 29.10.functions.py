## Functions :

# 1.Define a function called `greet` that takes a name as an argument and -
# - prints a greeting message like:" "Hello, [name]!"


def greet(name):
    print(f"Hello, {name}!")

greet("vinay")

# 2.Write a function `add_numbers` that takes two numbers as arguments and -
# - returns their sum. Test the function by passing different numbers.

def add_numbers(num1, num2):
    return num1 + num2

print(add_numbers(5, 3))   
print(add_numbers(-1, 4))   
print(add_numbers(10.5, 4.5)) 


# 3.Create a function `is_even` that takes a number as an argument and -
# - returns 'True' if the number is even, and `False` otherwise.

def is_even(number):
    return number % 2 == 0

print(is_even(4))   
print(is_even(7))   
print(is_even(0))   
print(is_even(-2)) 

# 4.Write a function `factorial` that takes a positive integer as input and returns the factorial of -
# - that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  
print(factorial(0))  
print(factorial(6))  

# 5.Define a function `find_max` that takes three numbers as input and returns -
# - the largest of the three. Test the function with various sets of numbers.

def find_max(num1, num2, num3):
    return max(num1, num2, num3)

print(find_max(3, 7, 5))   
print(find_max(-1, -5, -3)) 
print(find_max(10, 20, 15)) 
print(find_max(0, 0, 0))    


# 6.Write a function `count_vowels` that takes a string as input and returns the -
# - number of vowels (a, e, i, o, u) in the string.

def count_vowels(s):
    vowels = "aeiou"
    count = sum(1 for char in s if char in vowels)
    return count

print(count_vowels("Hello, World!"))  
print(count_vowels("Python Programming"))  
print(count_vowels("aeiou"))  
print(count_vowels(""))  


# 7.Create a function `is_prime` that takes a number as input and -
#-returns `True` if the number is prime, and `False` otherwise.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(2))   
print(is_prime(4))   
print(is_prime(17))
print(is_prime(20))  


# 8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns -
# - the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` should return \(1 + 2 + 3 + 4 + 5 = 15\).

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)

print(recursive_sum(5))  
print(recursive_sum(10)) 
print(recursive_sum(1))  


# 9.Write a function `calculator` that takes three parameters: two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`). 
# - The function should perform the operation on the two numbers and return the result.

def calculator(num1, num2, operator):          
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2

print(calculator(5, 3, "+"))  
print(calculator(5, 3, "-"))  
print(calculator(5, 3, "*"))  
print(calculator(5, 3, "/"))


# 10.Write a function `find_common_elements` that takes two lists as input and returns a -
# - list of elements that are present in both lists.


def find_common_elements(list1, list2):

    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = find_common_elements(list1, list2)
print(common_elements)  

# 11.Write a function `reverse_string` that takes a string as input and returns the string reversed.

def reverse_string(string):
    return string[::-1]

string = "hello world"
reversed_string = reverse_string(string)
print(reversed_string)  


def reverse_string(s):
    return s[::-1]

print(reverse_string("python is easy to learn"))
print(reverse_string(""))           


# 12.Write a function `sort_dict_by_value` that takes a dictionary as input and returns a list of -
# - tuples sorted by the dictionary values in ascending order.

def sort_dict_by_value(d):
    return sorted(d.items(), key=lambda item: item[1])

sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
print(sort_dict_by_value(sample_dict)) 

another_dict = {'x': 10, 'y': 5, 'z': 15}
print(sort_dict_by_value(another_dict))  
