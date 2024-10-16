# decleration of elements :

t = (1, "Hello", 3.14, True)
print(t)

t = (42,)
print(t)

t = ()
print(type(t))
t = (1,2,3,4,5)
print(type(t))

# accessing of elements from tuple :

t = (10, 20, 30, 40, 50)
f1 = t[0] 
s2 = t[1] 
l1 = t[-1]   
print(f1,s2,l1)

t = ("ramu",10,20,22.50,True)
print(type(t))
print(t[2])

#operation in the tuple :

t = (1,2,3,4)
t1 = (5,6,7,8,9)
print(t + t1)

t = (1,2,3,4,5)
t1 = (6,7,8,9)
print(t * 10)

#modifying of tuple elements :

t = (10,20,30,40,50)
l = list(t)
print(1)


t = (1, 2, 3)
temp_list = list(t)
temp_list[0] = 10
modify_tuple = tuple(temp_list)
print(t)  
print(modify_tuple) 

# tuple comprehension :

t = [x for x in range(1,21) if x % 2 == 0]
print(t)
print(type(t))

#  decleration :

s = {1,2,3,4,5,"string",95.99,True}
print(3)
print(type(t))



