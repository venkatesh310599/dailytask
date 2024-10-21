"Python program to count alphabets, digits and special characters"

s="python is easy and 12345 and @#$%"
digit_count=0
alpha_count=0
spe_count=0
for i in s:
    if i.isdigit():
        digit_count+=1
    elif i.isalpha():
        alpha_count+=1
    elif i.isspace():
        spe_count+=1
print(digit_count)
print(alpha_count)
print(spe_count)      