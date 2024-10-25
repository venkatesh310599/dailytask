
def add(a,b):
    return a+b
 
print(add(10,9))
 
 
##keywords
## In the modules we use the import and from and as keywords
 
def get_odd(s):
    l = []
    for i in s:
        if i % 2 == 1:
            l.append(i)
    return l
 
s = [1, 3, 6, 9, 33, 55, 99]    
print(get_odd(s))  
 
 
 
def factorial(x):
    if x<0:
        return x
    fact=1
    for i in range(1,x+1):
        fact*=i
    return fact
x=4
print(factorial(x))
     