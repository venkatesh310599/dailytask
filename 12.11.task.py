### Single Inheritance
##Problem Statement: Create a base class Animal with an attribute name and a method speak(). Then, create a #derived class Dog that inherits from Animal and overrides the speak() method to print "Bark".
 
#Tasks:
#Define a base class Animal with an __init__ method that takes name as a parameter.
#Define a method speak() in Animal that prints "Animal sound".
#Create a derived class Dog that inherits from Animal and overrides the speak() method to print "Bark".
#Create an instance of Dog and call the speak() method.
 
 
class animal:
    def __init__(self,name):
        self.name=name
    def m1(self):
        print("animal sound")
 
class dog(animal):
    def speak(self):
        print("barks")  
 
d=dog("luci")
d.speak()
 
 
#2. Multiple Inheritance
 
#1.Problem Statement: Create a class Teacher with an attribute subject.
# Then, create a class Researcher with an attribute field. Finally,
# create a class TeachingResearcher that inherits from both Teacher and Researcher,
# and has an additional method to display both attributes.
 
#Tasks:
#Define a Teacher class with an __init__ method to initialize subject.
#Define a Researcher class with an __init__ method to initialize field.
#Define a TeachingResearcher class that inherits from both Teacher and Researcher,
# and has an __init__ method to initialize both subject and field. Add a method to display both.
#Create an object of TeachingResearcher and display its attributes.
 
 
class teacher:
    def __init__(self,subject):
        self.subject=subject
 
 
 
class researcher:
    def __init__(self,field):
        self.field=field
 
class teachingresearcher(teacher, researcher):
    def __init__(self, subject, field):
        teacher.__init__(self, subject)  
        researcher.__init__(self, field)
 
    def dispaly(self):
        print(self.subject)
        print(self.field)
 
tr=teachingresearcher("physics","english")  
 
tr.dispaly()
 
 
#2.Problem Statement: Create two base classes: Bird and Flyable.
#Bird should have an attribute species, and Flyable should have a method fly().
# Then, create a derived class Eagle that inherits from both Bird and Flyable.
 
#Tasks:
#Define a class Bird with an attribute species.
#Define a class Flyable with a method fly() that prints "Flying".
#Create a class Eagle that inherits from both Bird and Flyable,
# and has a method to display species and flying capability.
#Create an instance of Eagle and call its methods.
 
 
class bird:
    def __init__(self,species):
        self.species=species
 
 
class flyable:
    def fly(self):
        print("flyable")
 
class eagle(bird,flyable):
    def __init__(self, species):
        bird.__init__(self, species)
 
    def dispaly(self):
        print(self.species)
        self.fly()  
 
e=eagle("Eagle")
 
e.dispaly()
 
 
 
#3. Multilevel Inheritance
#Problem Statement: Create a class hierarchy where Person is the base class,
# Employee is derived from Person, and Manager is derived from Employee.
# Each class should add an additional attribute, and a method to display
# all attributes from the hierarchy.
 
#Tasks:
#Define a base class Person with attributes name and age.
#Define a derived class Employee with an additional attribute salary.
#Define another derived class Manager that inherits from Employee and adds an attribute department.
#Implement methods to display the information in each class.
#Create an instance of Manager and display its information.
 
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
   
    def display(self):
        print(self.name)
        print(self.age)
 
 
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
 
    def display(self):
        super().display()
        print(self.salary)
 
 
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)  
        self.department = department
 
    def display(self):
        super().display()
        print(self.department)
 
 
m = Manager("venky", 24, 26000, "developer")
 
m.display()
 
 
 
#4. Hierarchical Inheritance
 
#1.Problem Statement: Design a class hierarchy for an employee management
# system with the following structure:
 
#Employee: Base class with name and salary.
#Developer: Inherits from Employee with an additional attribute programming_language.
#Manager: Inherits from Employee with an additional attribute team_size.
#Intern: Inherits from Developer and has an additional attribute internship_duration.
#Implement a method to display the details of each employee.
 
 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
 
    def display(self):
        print(self.name)
        print(self.salary)
 
 
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)  
        self.programming_language = programming_language
 
    def display(self):
        super().display()  
        print(self.programming_language)
 
 
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  
        self.team_size = team_size
 
    def display(self):
        super().display()  
        print(self.team_size)
 
 
class Intern(Developer):
    def __init__(self, name, salary, programming_language, internship_duration):
        super().__init__(name, salary, programming_language)  
        self.internship_duration = internship_duration
 
    def display(self):
        super().display()  
        print(self.internship_duration)
 
 
 
e = Employee("venky", 150000)
d = Developer("varun", 80000, "Python")
m = Manager("nani", 50000, 8)
i = Intern("vinay", 35000, "Java", 4)
 
 
e.display()
 
d.display()
m.display()
 
i.display()
 
 
 
#2.Problem Statement: Create a base class Vehicle with attributes brand and model.
# Then, create two derived classes Car and Bike, both inheriting from Vehicle,
# and adding their own attributes and methods.
 
#Tasks:
##Define a base class Vehicle with attributes brand and model.
##Create a derived class Car that inherits from Vehicle and adds an attribute num_doors.
#Create another derived class Bike that inherits from Vehicle and adds an attribute type.
#Implement methods to display the details of the vehicles.
#Create instances of both Car and Bike and display their information.
 
 
 
# Base class Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
 
    def display(self):
        print(self.brand)
        print(self.model)
             
 
 
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)  
        self.num_doors = num_doors
 
    def display(self):
        super().display()  
        print(self.num_doors)
 
class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)  
        self.bike_type = bike_type
 
    def display(self):
        super().display()  
        print(self.bike_type)
 
car = Car("Maruthi", "Thar 4x4", 4)
 
bike = Bike("kawasakhi", "ninza", "Sport")
 
car.display()
 
bike.display()
 
 
#5. Hybrid Inheritance
#Problem Statement: Create a class structure to represent hybrid inheritance:
 
##Device: Base class with name attribute.
#Phone: Derived from Device with an additional phone_number attribute.
#Tablet: Derived from Device with an additional screen_size attribute.
#Smartphone: Derived from both Phone and Tablet with an additional attribute os.
 
#Tasks:
#Define a base class Device with an attribute name.
#Define a class Phone that inherits from Device and adds an attribute phone_number.
#Define a class Tablet that inherits from Device and adds an attribute screen_size.
#Define a class Smartphone that inherits from both Phone and Tablet, adding an attribute os.
#Implement methods to display all attributes of the Smartphone.
#Create an instance of Smartphone and display its information.
 
 
 
 
"""class Device:
    def __init__(self, name):
        self.name = name
 
    def display(self):
        print(f"Device Name: {self.name}")
 
class Phone(Device):
    def __init__(self, name, phone_number):
        super().__init__(name)  
        self.phone_number = phone_number
 
    def display(self):
        super().display()
        print(self.phone_number)
 
 
class Tablet(Device):
    def __init__(self, name, screen_size):
        super().__init__(name)  
        self.screen_size = screen_size
 
    def display(self):
        super().display()
        print(f"Screen Size: {self.screen_size} inches")
 
class Smartphone(Phone, Tablet):
    def __init__(self, name, phone_number, screen_size, os):
        Phone.__init__(self, name, phone_number)
        Tablet.__init__(self, name, screen_size)  
        self.os = os  
 
    def display(self):
        print("Smartphone Details:")
        Phone.display(self)  
        Tablet.display(self)
        print(self.os)
 
phone = Phone("samsung", "123-456-7890")
tablet = Tablet("thinkpad", 10.1)
smartphone = Smartphone("iPhone", "902-123-3456", 11, "iOS")
 
 
phone.display()
tablet.display()
smartphone.display()
"""
 
 
#6.Basic Inheritance
#Problem Statement: Create a class Person with attributes: name and age.
# Create another class Student that inherits from Person and has
# an additional attribute grade. Define methods in both classes to display the attributes.
 
#Tasks:
##Define a Person class with an __init__ method to initialize name and age.
#Define a Student class that inherits from Person, with an additional attribute grade.
#Define a display_info method in both Person and Student classes to print all attributes.
#Create objects for both Person and Student and display their information.
 
 
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
 
 
class Student(Person):
    def __init__(self, name, age, grade):
       
        super().__init__(name, age)  
        self.grade = grade
 
    def display_info(self):
       
        super().display_info()  
        print(f"Grade: {self.grade}")
 
person = Person("ramu", 32)
 
student = Student("raju", 30, "A")
 
 
person.display_info()
student.display_info()
