# interpreted language

print("hello world")
x = 10
y = 20
print(x,y)


# different data types:

number = 10
x = 100
print(number)


int = 42
f = 3.14
c = 3 + 4j
print(int)
print(f)
print(c)
sum_value = int + f
print("Sum of Int and F:", sum_value)

# string:

name = "kiran"
print(type(name))



#list: 

details = ["ram" ,99,85,99,True]
print(details)
print(type(details))

# tuple :

t = (10,20,30,"teju",99,89,True)
print(type(t))
print(t)

# dictionary :

d = {"name":"ram","roll no":95,"marks":88.2,"pass":True}
print(type(t))
print(t)


# set :

s = {1,2,3,4,5,7,1,2,3}
print(type(s))
print(s)


# membership checking in string :

s = "learning python is very easy"
print("easy" in s)
print("java" in s)
print("is" not in  s)


# arithematic operations :

print(10 < 20)
print(10 > 20)
print(10 <= 20)
print(10 >= 20)
print(10 == 20)
print(10 != 20)


# logical operations :

x = 10 > 20
y = 10 < 20
print(x,y)
 

# input and output :


name = input("praveen")
print(name)
x = input("enter your x:")
y = input("enter your y:")
print(x + y)


# Break and Continue :

# Membership learning :

s = "python"
s1 = "learning"
print(s + s1)
print(s + "10")
print((s +" ") *10)
print(s+s1)

# split :

s = "learning python is very easy"
ss = s.split()
print(ss)
print(len(ss))


# Comparing of two strings :


s1 = "ram"
s2 = "raju"
print(s1 == s2)
print(s1 < s2)
print(s1 > s2)


# adding elements :
# append 
# insert

# append:

l = []

for i in range(10):
    l.append(i)
    print(l)
    l.append(10)
    l.append(11)
    print(l)


# insert :

l = [0,1,2,3,4,5,6,7,8,9,10,11]
print(l)



