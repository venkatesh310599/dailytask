# built in function :

l = [10,20,30,40,50]
total = 0
for i in l :
    total = total + 1
    print(total)
    print(len(l))


dict = {'a':1,'b':2,'c':3,'d':4}
print(len(dict))


# recursive :

def factorial(n):
    if n == 0:
        return 1  
    else:
        return n * factorial(n - 1)  
print(factorial(5)) 


def factorial(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 1  
    else:
        return n * factorial(n - 1)
print(factorial(5))
print(factorial(0))


# lambda function :

add = lambda x, y: x + y
print(add(3, 5)) 


l = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, l))
print(squared) 

# reduse() function :

from functools import reduce 

l = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, l)
print(total) 

from functools import reduce 

l = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, l)
print(product)


