## encapsulation :

class BankAccount:
    def __init__(self, account_number, account_holder_name, account_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = account_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if self.__account_balance >= amount:
            self.__account_balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__account_balance

# Create a BankAccount object
account = BankAccount(987654321, "Hemanth", 50000)

# Deposit money
account.deposit(5300)

# Withdraw money
account.withdraw(2000)

# Check balance
print(account.get_balance())




## encapsulation for student :
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade 

    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100.")

    # student info
    def student_info(self):
        return f"Student: {self.name}, Grade: {self.__grade}"


student = Student("venky", 95)
print(student.get_grade())  

student.set_grade(87)
print(student.get_grade()) 

# Trying to set an invalid grade
student.set_grade(105) 

