#.Create a class Person that has instance variables name, age, and gender. Add methods to:
#Initialize these variables.
#Update the age.
#Display the person's information.
 #Exercise:
 #> Create multiple instances of the Person class.
 #> Change the age of one person and display the updated information.

 
class Person:
    def __init__(self, name, age, gender, Acc_no, branch_no, phone_no):
        self.name = name
        self.age = age
        self.gender = gender
        self.Acc_no = Acc_no
        self.branch_no = branch_no
        self.phone_no = phone_no
 
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Acc_no:", self.Acc_no)
        print("Branch_no:", self.branch_no)
        print("Phone_no:", self.phone_no)
 
    def update(self, new_age, new_phone_no):
        self.age = new_age
        self.phone_no = new_phone_no
        print("Updated Age:", self.age)
        print("Updated Phone No:", self.phone_no)
 
p = []
for i in range(1):  
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    Acc_no = int(input("Enter your Acc_no: "))
    branch_no = input("Enter your branch_no: ")
    phone_no = int(input("Enter your phone_no: "))
   
    person = Person(name, age, gender, Acc_no, branch_no, phone_no)
    p.append(person)  
 
 
for person in p:
    person.display()
 
 
update_index = int(input("Enter an index value (0 for the first person): "))
update_new_age = int(input("Enter your new age: "))
update_new_phone_no = int(input("Enter your new phone number: "))
 
p[update_index].update(update_new_age, update_new_phone_no)
 
for person in p:
    person.display()
 
 
 
#2.Create a class Company that keeps track of the total number of employees using a
# static variable total_employees.
#  Each employee has instance variables name and department. Every time an employee is
# added, the total_employees should increment.
#  Exercise:
#   >Create multiple employee instances.
#   >Print the total number of employees after adding each new employee.
#   >Check whether changing the total_employees in one instance affects the others.
 
class company:
    total_emp=0
    def __init__(self,emp_name,emp_id,emp_dep):
        self.emp_name=emp_name
        self.emp_id=emp_id
        self.emp_dep=emp_dep
       
        company.total_emp +=1
 
    def display(self):
        print("emp_name:",self.emp_name)
        print("emp_id:",self.emp_id)
        print("emp_dep:",self.emp_dep)
 
p=[]
num_emp=int(input("enter a no of emp to added:"))
for i in range(num_emp):
    emp_name=input("enter your emp_name:")
    emp_id=int(input("enter your emp_id:"))
    emp_dep=input("enter your emp_dep:")
    emp=company(emp_name,emp_id,emp_dep)
    p.append(emp)
 
    print("total emp :{company.total_emp}")
 
for company in p:
    company.display()
 
company.total_emp=+1
print("total no of emps after adding : {company.total_emp}")
 
 
 
 
 
#3.Create a class Rectangle that has instance variables length and width.
#  Add a method calculate_area that calculates and prints the area of the rectangle
# using local variables inside the method.
#  Exercise:
#    >Create instances of the Rectangle class with different lengths and widths.
#    >Calculate and print the area for each rectangle.
 
class rectangle:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
 
    def dispaly(self):
        print("lenght:",self.lenght)
        print("width:",self.width)
 
    def calculate_area(self):
        area=self.lenght*self.width
        return area
 
rect=[]
num_rectangle=int(input("enter a no of rectangle:"))
for i in range(num_rectangle):
    lenght=int(input("enter a lenght of rectangle:"))
    width=int(input("enter a width of rectangle:"))
    rect.append(rectangle(lenght,width))
 
 
for rectangle in rect:
    rectangle.dispaly()
    area =rectangle.calculate_area()
    print(area)
 
 
 
#4.Create a class Employee where:
#  Each employee has an instance variable salary.
#  There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
#  Write a method total_salary that calculates the total salary for an employee (including the bonus).
#  Exercise:
#   >Create several employee instances with different salaries.
#   >Change the bonus amount (static variable) and see how it affects all employees.
#   >Calculate and print the total salary for each employe
 
 
class employee:
    bonus=0
    def __init__(self,emp_salary):
        self.emp_salary=emp_salary
    def dispaly(self):
        print("emp_salary:",self.emp_salary)    
 
    def total_salary(self):
        sum=emp_salary + emp_bonus
        return sum
 
emp=[]
num_emp=int(input("enter no of emp_salary_no:"))
for i in range(num_emp):
    emp_salary=int(input("enter your salary:"))
    emp.append(employee(emp_salary))
 
emp_bonus=int(input("enter your bonus for your salary:"))    
 
for employee in emp:
    employee.dispaly()
    sum=employee.total_salary()
    print(sum)   
 
 