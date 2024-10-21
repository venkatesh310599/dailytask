"Python program to print all non repeating character in string"

str=input("enter a string:")
for i in str:
    if str.count(i)==1:
        print(i) 