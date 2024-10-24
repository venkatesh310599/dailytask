# Types os argument :

## 1 : Position argument :

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet("venky", "vinay")


def add(x , y):
    print("x -",x)
    print("y -",y)
    print(x - y)

    add(10,20)

def add(x,y):
    print(x + y)

    add(5,10)

## 2 : keyword augument :

def wish(animal_type, pet_name):
    print(animal_type + pet_name)

wish(animal_type="dog", pet_name="Buddy")



def wish(title, author, year):
     print(f"'{title}' by {author}, published in {year}.")

wish(author="George Orwell", title="1984", year=1949)

## 3 : variable length keyword argument :

def student(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student (name="Alice", age=21, major="Computer Science")



def order_details(customer_name, **order_details):
    print(f"Order details for {customer_name}:")
    for item, quantity in order_details.items():
        print(f"{item}: {quantity}")

order_details("Bob", apples=3, bananas=5, oranges=2)


## 4 : Default argument :

def data(name="Guest"):
    print(f"Hello, {name}!")
data("Alice") 
data()      

def data (email , first_name , last_name = False):
    print(email)
    print(first_name)
    print(last_name)
data("venkatesh@gmail.com" , "venkatesh","venky")
