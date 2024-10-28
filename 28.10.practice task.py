
## oops :
"Object-Oriented Programming (OOP) is a programming paradigm centered around the concept of objects ,"
"which can contain data and methods."
## Encapsulation 
## Encapsulation 
## Inheritance 
## Polymorphism

## uses case of oops :
"oops is widely used across various domains due to its flexibility and modularity."
##Software Development
# Game Development
# Web Development
# Graphical User Interfaces (GUIs)
#Simulation and Modeling
#Database Management
#Artificial Intelligence

## importance of oops :
"Modularity: OOP encourages breaking down complex system."
"Code Reusability: Through inheritance and polymorphism"
"Abstraction: It simplifies complex reality by modeling classes based on essential attributes and behaviors"
"Flexibility and Scalability: OOP allows for easier updates and modifications. As requirements change"
"Encapsulation: OOP promotes data hiding, protecting the internal state of objects and ensuring that only necessary interactions are exposed"
"Maintainability: The clear structure provided by OOP makes it easier to understand and maintain code over time"
"Collaboration: OOP facilitates teamwork, as different developers can work on different classes or modules independently"
"Real-world Modeling: OOP aligns closely with how we think about real-world entities"

## real time applications :
#Web Applications
#Game Development
#Mobile Applications
#Simulation Software
#Enterprise Resource Planning (ERP) Systems
#Customer Relationship Management (CRM) Systems
#Healthcare Management Systems

"the oops concept is based on the class and object"
# class , object :

class Car:
    def __init__(self, make, model, year):
        self.make = make        # Brand of the car
        self.model = model      # Model of the car
        self.year = year        # Year of manufacture

    def get_details(self):
        print(self.make)
        print(self.model)
        print(self.year)

e1 = Car("Toyota", "Corolla", 2024)
e1.get_details()


class student:
    def __init__(self,name,section,roll_no,marks):
        self.name = name
        self.section = section
        self.roll_no = roll_no
        self.marks = marks
    
    def get_details(self):
        print(self.name)
        print(self.section)
        print(self.roll_no)
        print(self.marks)

v1 = student("venkatesh","Sec-A",15,818)
v1.get_details()

# Define the Dog class :

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def info(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}."

dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "Bulldog", 5)
print(dog1.bark())  
print(dog1.info())  

print(dog2.bark())  
print(dog2.info()) 
