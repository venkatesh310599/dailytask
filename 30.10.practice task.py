## variables in oop:
 
# types of variables:

## 1.instance variables:
    ##    >>declarations:
    ##     >>accesing :
 
class emp:
    def __init__(self):
        self.name="venky"
        self.salary=89000
 
    def dispaly(self,age,id):
        self.age=age
        self.id=id
        print(self.name)
        print(self.salary)
       
 
e=emp()
e.dispaly(18,295)
print(e.name) 
print(e.age)
 
 
 
 
class collage:
    def __init__(self,name,branch,rollno,classno,blockno):
        self.name=name
        self.branch="eee"
        self.rollno=rollno
        self.classno=classno
        self.blockno=blockno
 
    def display(self):
        print(self.branch)
        print(self.name)
        print(self.rollno)
        print(self.classno)
        print(self.blockno)
 
c=collage("vinay","eee",282,203,1608)
c.display()
 
c1=collage("venky","eee",295,292,1999)
c1.display()
 
 
 
 
class cow:
    def __init__(self,name,age):
        self.name=name
        self.age=age
 
    def c(self):
        print(self.name)
        print(self.age)
 
c1=cow("radha",2.5)
c1.c()
c2=cow("cow",1.4)
c2.c()        
 
 
 
 
#static variable:

#   >>declaration :
#    >>accessing :

 
class collage:
    collagename="mit's collage"  
    def __init__(self,name,branch,rollno):
       
        self.name=name
        self.rollno=rollno
       
        collage.branch="eee branch"  
       
        print(collage.branch)
   
    def d(self):
        collage.section="section B"
        print(self.name)
        print(self.rollno)
       
 
s=collage("venkatesh","eee",295)
print(collage.collagename)
 
collage.age=22 
s.d()  
print(collage.age)  
 
 
 
 
 
class dog:

    dog_breed="doberman"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        dog.legs="4 legs"
 
    def d(self):
        dog.eyes="2 eyes"
        print(self.name)
        print(self.age)
s=dog("rockey",1.5)
s.d()
print(dog.dog_breed)
print(dog.legs)
print(dog.eyes)
 