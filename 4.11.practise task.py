#instance method:
# >we can declaring and accessing a instance variable inside a method
# >while declaring instance method have to pass self as an first paramater
# >we can acces thses instance method using orv or classname
 
 
###instance method:
 
class vegetables:
    def __init__(self,carrot,potato,tomato):
        self.carrot=carrot
        self.potato=potato
        self.tomato=tomato
 
    def m(self,totalprice):
        self.totalprice=totalprice
        print(self.carrot)
        print(self.potato)
        print(self.tomato)  
        print(self.totalprice)
 
f=vegetables(2,3,4)
f.m(100)  
 
 
class parrot:
    def __init__(self,name,age):
 
        self.name=name
        self.age=age
 
    def m(self,bread):
        self.bread=bread
        print(self.name)
        print(self.age)
        print(self.bread)  
 
d=[]
m1=int(input("enter a number_of:"))  
for i in range(m1):
    name=input("enter a name:")
    age=int(input("enter a age:"))
 
    parrot=parrot(name,age)
    d.append(parrot)
 
for parrot in d:
    parrot.m("grayparrot")      
 
 
 
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def wish(self):
        print(self.name)
        print(self.age)
 
    def introduce(self):
        self.wish()
        print("iam going to trip")
 
person= person("murari", 22)
person.introduce()
 
 
 
 
 
 
#class method:
#  >inside the class method have  to use only static variable
# >while declaring class method have to pass @class method
# >while declaring class method have to pass cls as first parameter
# > using cls keyword we can declare and can access the data in side class method
 
class nuts:
    totalprice=2000
    @classmethod
    def m(cls,almond,cashew,walnuts):
        cls.shopname="dmart"
        print(almond)
        print(cashew)
        print(walnuts)
        print(nuts.totalprice)
        print(cls.shopname)
 
p=nuts()
p.m(1,2,3)              
 

 
class collage:
    branch="cse"
    @classmethod
    def m(cls,name,rollno):
        cls.collagename="venky"
        print(name)
        print(rollno)
        print(cls.branch)
        print(cls.collagename)
 
c=collage
c.m ("venky",295)      
 
 
class meeshoo:
    price=50000
    @classmethod
    def m(cls,name,rating):
        cls.companyname="dmart"
        print(name)
        print(rating)
        print(cls.companyname)
        print(cls.price)
 
f=meeshoo()
f.m("iphone","5star")
 
 
 
##static method:
#  >>we are not using instance and static variable
#  >we are not passing any paramter like self or cls
# >we have to pass @staticmethod decorate
# >we can access static method using class anem and cls variable
       
 
class add:
    @staticmethod  
    def m():
        a=3
        b=6
        print(a+b)
   
a1=add()
a1.m()
 
 
 
class bank:
    @staticmethod
    def m():
        name="venky"
        age=24
        phone_no=9912932124
        acc_no=295
        return name ,age,phone_no,acc_no
 
b=bank()
print(b.m())    
 
 
 
class vegetables:
    @staticmethod
    def m():
        tomato=3
        potato=1
        ladiesfinger=10
        onion=2
        totaliteams=tomato+potato+ladiesfinger+onion
 
        return totaliteams
v=vegetables()
print(v.m())
 
 
 
 