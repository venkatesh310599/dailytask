"Remove all occurrences of the number 3 from a list of integers"

l = [1,2,3,4,3,5,3,6]
print(l)
l = (num for num in l if num != 3)
print(l)
