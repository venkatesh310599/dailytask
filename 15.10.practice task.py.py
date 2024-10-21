
s = "python"
s1 = "learning"
print(s + s1)
print(s + "10")
print((s +" ") *10)
print(s+s1)

s = "learning python is very easy"
ss = s.split()
print(ss)
print(len(ss))


s1 = "ram"
s2 = "raju"
print(s1 == s2)
print(s1 < s2)
print(s1 > s2)


s=["hello","nani","nagu"]
c=""
for i in s:
    c+=i
c=c.strip()
print(c)  

s=input("hello,world!")
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


s = "python learning"  
c = " is easy to "  
s1 = ""  
for i in s:
    if i == " ":
        s1 += c
    else:
        s1 += i
print(" string:", s1)

n="arora"
rev=""
temp=n
for i in n:
    rev=i+rev
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")



    s="nani"
s1="nagu"
if set(s)==set(s1) and len(s)==len(s1):
    print("anagram")
else:
    print("not")

s="12345667"
s1="nani123"
print(s.isdigit())
print(s1.isdigit())


s="learning"
print(s.count("l"))
print(s.count("e"))
print(s.count("a"))
print(s.count("r"))
print(s.count("n"))
print(s.count("i"))
print(s.count("g"))


s="learning python is very easy"
print(s[::-1])
word=s.split()
reversed_sentence=word[4]+' '+word[3]+' '+word[2]+' '+word[1]+' '+word[0]+' '
print(reversed_sentence)

