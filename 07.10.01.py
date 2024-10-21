"Python Program to count occurrence of a given characters in string"

s="venkatesh"
char="n"
c=0
for i in s:
    if i==char:
        c+=1
print(c)

"Python Program to check if two Strings are Anagram"

s="vinay"
s1="nagu"
if set(s)==set(s1) and len(s)==len(s1):
    print("anagram")
else:
    print("not")