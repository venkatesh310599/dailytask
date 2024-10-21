"Python program to replace the string space with a given character"

s = "python learning"  
c = " is easy to "  
s1 = ""  
for i in s:
    if i == " ":
        s1 += c
    else:
        s1 += i
print(" string:", s1)


