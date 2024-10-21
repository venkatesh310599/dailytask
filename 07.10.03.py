"Python program to check a String is palindrome or not"

n="arora"
rev=""
temp=n
for i in n:
    rev=i+rev
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")