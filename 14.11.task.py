#1.Create a class Vehicle with attributes brand and year. The class should have a method get_info() that returns the brand and year of the vehicle. Then, create two subclasses:

#Car, which adds an attribute number_of_doors.
#Motorcycle, which adds an attribute has_sidecar.
#Both subclasses should override the get_info() method to include their respective additional attributes in the returned string.

# Define the Vehicle class
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_info(self):
        return f"{self.brand}, {self.year}"


# Define the Car subclass
class Car(Vehicle):
    def __init__(self, brand, year, number_of_doors):
        super().__init__(brand, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"{super().get_info()}, {self.number_of_doors} doors"


# Define the Motorcycle subclass
class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        sidecar_status = "with" if self.has_sidecar else "without"
        return f"{super().get_info()}, {sidecar_status} sidecar"



car = Car("Toyota", 2020, 4)
print(car.get_info())  

motorcycle = Motorcycle("Harley Davidson", 2015, True)
print(motorcycle.get_info())  


#2.Define an abstract class Animal with an abstract method make_sound(). Then, create three classes that inherit from Animal:

#Dog with the sound "Woof".
#Cat with the sound "Meow".
#Cow with the sound "Moo".
#Create a function play_sound(animal) that takes an object of type Animal and calls its make_sound() method.

# Import the ABC module for abstract classes
from abc import ABC, abstractmethod

# Define the abstract Animal class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Define the Dog class
class Dog(Animal):
    def make_sound(self):
        return "Woof"


# Define the Cat class
class Cat(Animal):
    def make_sound(self):
        return "Meow"


# Define the Cow class
class Cow(Animal):
    def make_sound(self):
        return "Moo"


# Define the play_sound function
def play_sound(animal: Animal) -> None:
    if not isinstance(animal, Animal):
        raise TypeError("Expected an instance of Animal")
    print(animal.make_sound())



dog = Dog()
cat = Cat()
cow = Cow()

play_sound(dog)   # Output: Woof
play_sound(cat)   # Output: Meow
play_sound(cow)   # Output: Moo

try:
    play_sound("Invalid animal")
except TypeError as e:
    print(e)  


#3.Create an abstract class BankAccount with methods deposit(), withdraw(), and get_balance(). Then, create two subclasses:

#SavingsAccount, where the withdraw() method ensures that the balance cannot go below $500.
#CurrentAccount, where the withdraw() method allows the balance to go negative (up to $1000 overdraft).
#Ensure that only deposit() and withdraw() are exposed to the user, and the balance is encapsulated (hidden).


from abc import ABC, abstractmethod

# Abstract base class BankAccount
class BankAccount(ABC):
    def __init__(self, initial_balance):
        self._balance = initial_balance  # Balance is encapsulated (hidden)

    # Abstract methods to be implemented by subclasses
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance  # Return the current balance (encapsulated)

# Subclass SavingsAccount
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self._balance - amount < 500:
            print("Withdrawal denied: Cannot withdraw below $500.")
        else:
            self._balance -= amount

# Subclass CurrentAccount
class CurrentAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self._balance - amount < -1000:
            print("Withdrawal denied: Cannot go below $1000 overdraft.")
        else:
            self._balance -= amount


savings = SavingsAccount(1000)
current = CurrentAccount(500)

# Depositing and withdrawing in Savings Account
savings.deposit(200)
print(f"Savings Account Balance: {savings.get_balance()}")  
savings.withdraw(800)
print(f"Savings Account Balance: {savings.get_balance()}")  
savings.withdraw(100) 

# Depositing and withdrawing in Current Account
current.deposit(300)
print(f"Current Account Balance: {current.get_balance()}") 
current.withdraw(1500)
print(f"Current Account Balance: {current.get_balance()}")  
current.withdraw(2000)  

#4.Create a base class Employee with attributes name and salary, and methods get_details() and get_salary(). Then create two subclasses:

#Manager, which adds an attribute department.
#Developer, which adds an attribute programming_language.
#Both subclasses should override the get_details() method to include their respective additional attributes in the returned string.

#Add a method increase_salary(percent) in the Employee class that increases the salary by a given percentage.


# Define the Employee base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_details(self):
        return f"{self.name}, Salary: ${self.__salary:.2f}"

    def get_salary(self):
        return self.__salary

    def increase_salary(self, percent):
        self.__salary *= (1 + percent / 100)


# Define the Manager subclass
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"{super().get_details()}, Department: {self.department}"


# Define the Developer subclass
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_details(self):
        return f"{super().get_details()}, Programming Language: {self.programming_language}"


# Example usage
manager = Manager("John Doe", 80000, "Marketing")
developer = Developer("Jane Smith", 60000, "Python")

print("Initial details:")
print(manager.get_details())
print(developer.get_details())

print("\nIncreasing salaries by 10%:")
manager.increase_salary(10)
developer.increase_salary(10)

print("\nUpdated details:")
print(manager.get_details())
print(developer.get_details())


#5.Create an abstract class Media with an abstract method play(). Then create the following subclasses:

#Audio, which plays a .mp3 file.
#Video, which plays a .mp4 file.
#LiveStream, which plays a live stream.
#Implement a function start_media(media) that takes an object of type Media and calls its play() method. Demonstrate polymorphism by passing different types of media to this function.


from abc import ABC, abstractmethod

# Abstract base class Media
class Media(ABC):
    @abstractmethod
    def play(self):
        pass

# Subclass Audio
class Audio(Media):
    def __init__(self, filename):
        self.filename = filename
    
    def play(self):
        print(f"Playing audio file: {self.filename}")

# Subclass Video
class Video(Media):
    def __init__(self, filename):
        self.filename = filename
    
    def play(self):
        print(f"Playing video file: {self.filename}")

# Subclass LiveStream
class LiveStream(Media):
    def __init__(self, stream_url):
        self.stream_url = stream_url
    
    def play(self):
        print(f"Streaming live content from: {self.stream_url}")

# Function to start media
def start_media(media):
    media.play()

# Demonstrating polymorphism
audio = Audio("song.mp3")
video = Video("movie.mp4")
live_stream = LiveStream("https://livestream.example.com")

print("Playing media:")                         
start_media(audio)   
start_media(video)       
start_media(live_stream) 


#6.Create an abstract class LibraryItem with abstract methods borrow() and return_item(). Then create two subclasses:

#Book, with attributes title, author, and num_copies.
#DVD, with attributes title, director, and duration.
#Implement a function borrow_item(item) that borrows the library item and decreases the number of available copies (for books) or marks the DVD as borrowed.

# Import the ABC module for abstract classes
from abc import ABC, abstractmethod


# Define the abstract LibraryItem class
class LibraryItem(ABC):
    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_item(self):
        pass


# Define the Book subclass
class Book(LibraryItem):
    def __init__(self, title, author, num_copies):
        self.title = title
        self.author = author
        self.num_copies = num_copies
        self.is_borrowed = False

    def borrow(self):
        if self.num_copies <= 0:
            raise ValueError("No copies available")
        if self.is_borrowed:
            raise ValueError("Book is already borrowed")
        self.num_copies -= 1
        self.is_borrowed = True
        print(f"Borrowed '{self.title}' by {self.author}")

    def return_item(self):
        if not self.is_borrowed:
            raise ValueError("Book is not borrowed")
        self.num_copies += 1
        self.is_borrowed = False
        print(f"Returned '{self.title}' by {self.author}")


# Define the DVD subclass
class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            raise ValueError("DVD is already borrowed")
        self.is_borrowed = True
        print(f"Borrowed '{self.title}' directed by {self.director}")

    def return_item(self):
        if not self.is_borrowed:
            raise ValueError("DVD is not borrowed")
        self.is_borrowed = False
        print(f"Returned '{self.title}' directed by {self.director}")


# Define the borrow_item function
def borrow_item(item: LibraryItem) -> None:
    if not isinstance(item, LibraryItem):
        raise TypeError("Expected an instance of LibraryItem")
    
    item.borrow()


# Define the return_item function
def return_item(item: LibraryItem) -> None:
    if not isinstance(item, LibraryItem):
        raise TypeError("Expected an instance of LibraryItem")
    
    item.return_item()


# Example usage
book = Book("To Kill a Mockingbird", "Harper Lee", 5)
dvd = DVD("The Shawshank Redemption", "Frank Darabont", "2h 22m")

print("Borrowing items:")
borrow_item(book)
borrow_item(dvd)

print("\nReturning items:")
return_item(book)
return_item(dvd)

try:
    borrow_item("Invalid item")
except TypeError as e:
    print(e)  # Output: Expected an instance of LibraryItem