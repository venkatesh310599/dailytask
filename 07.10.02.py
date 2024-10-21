"Python Program to check if two Strings are Anagram"

s="venky"
s1="vinay"
if set(s)==set(s1) and len(s)==len(s1):
    print("anagram")
else:
    print("not")