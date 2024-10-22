# declaration:
 
def wish(name):
    print("happy birthday",name)
wish ("murari")
 
 
def add(s,s1):
    print(s+s1)
    print(s1-s1)
    print(s*s1)
    print(s/s1)
add(30,20)
 
 
def s(x,y):
    print(x+y)
s("venky","vinay")    
 
 
## by adding marks for students:
 
def marks (math,physics,chemistry,english):
   
    total=math+physics+chemistry+english
    print(total)
    print((total/totalscore)*100)
 
 
math=99
physics=55
chemistry=45
english=80
totalscore=400
marks(math,physics,chemistry,english)
 
math=92
physics=77
chemistry=49
english=73
totalscore=400
marks(math,physics,chemistry,english)
 
 
### return >> it is used to send a value back from a function to where it was called.
 
def add(a,b):
    #print(a+b)
    return a+b
add(10,20)
print(add(10,20))
sum=add(5,15)
print(sum)
 
if sum %2==1:
    print("is even")
else:
    print("not a even")    
 
 
 
##hight frequency element
#
def highest_frequency(l):
    max_count = 0
    most_frequent = None
    for i in l:
        count = l.count(i)
        if count > max_count:
            max_count = count
            most_frequent = i
    return most_frequent
 
s=highest_frequency([1, 4, 3, 7, 2, 8, 2, 5])
print(s)
 