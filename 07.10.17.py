"Python program to print the highest frequency character in a String"

s=input("enter a string:")
char_count={}
for char in s:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
max_char=""
max_count=0
for char,count in char_count.items():
    if count>max_count:
        max_count=count
print(max_char)
print(max_count)