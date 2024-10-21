"create a list of numbers. Assign the list to another variable and modify the original list. Check if the second list also changes. Then, create a copy of the original list and show that modifying the copy does not affect the original list"

l = [1,2,3,4,5]
s1 = l
l.append(6)
print(l.append,l)
s2 = l
l.append(7)
print(l,l.append)



