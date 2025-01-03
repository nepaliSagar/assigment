
def rectangle():
    class rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def rectangle_area(self):
            return f"Area of rectangle is {self.length * self.width}" 
        
        def rectangle_perimeter(self):
            return f"Perimeter of rectangle is {2 * (self.length * self.width)}"
 
    rectangle_1 = rectangle(20,10)
    print(rectangle_1.rectangle_area())
    print(rectangle_1.rectangle_perimeter())

def student():
    class Student:
        def __init__(self, name, roll_number, marks):
            self.name = name
            self.roll_number = roll_number
            self.marks = marks

        def display_details(self):
            return f"Student: Name is {self.name}. Roll number is {self.roll_number}. Marks obtain is {self.marks}"
        
        def is_passed(self):
            return ('Passed') if self.marks >= 40 else print("Failed")
        
    student_1 = Student("Sagar", 12, 39)
    print(student_1.display_details())
    print(student_1.is_passed())


from math import pi
def circle():
    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return pi*self.radius*self.radius
        
        def circumferenc(self):
            return 2*pi*self.radius
    
    circle_1 = Circle(12)
    print(circle_1.area())
    print(circle_1.circumferenc())

def bankAccount():
    class BankAccount:
        def __init__(self, account_number, account_holder, balance):
            self.account_number = account_number
            self.account_holder = account_holder
            self.balance = balance
        
        def deposite(self, amount):
            print(f"You deposited {amount}.")
            return f"New balance is {self.balance + amount}"

        def withdraw(self, amount):
            if self.balance > amount:
                print(f"You withdraw {amount}.")
                return f"New balance is {self.balance - amount}"
            else:
                print("Insuffucient balance")

        def display_balance(self):
            return self.balance
    
    person_1 = BankAccount(123, "Sagar", 90)

    print(person_1.display_balance())
    print(person_1.deposite(50))
    print(person_1.withdraw(40))

def book():
    class Book:
        def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price

        def apply_discount(self, discount):
            return self.price - discount

        def display_details(self, discount):
            discounted_price = self.apply_discount(discount)
            return f"Title of book ie {self.title} by {self.author}. Which cost {self.price} but after discount it cost {discounted_price}"
    
    book_1 = Book("Hello world", "Sagar", 123)

    print(book_1.apply_discount(10))
    print(book_1.display_details(10))


def calculator():
    class Calculator:
        def __init__(self,a,b):
            self.a = a
            self.b = b
        
        def add(self):
            return self.a + self.b
        
        def sub(self):
            return self.a - self.b

        def multiply(self):
            return self.a * self.b

        def divide(self):
            return self.a / self.b if self.b != 0 else print("Zero")
    
    first = Calculator(0,5)
    print(first.divide())

def person():
    class Person:
        def __init__(self, name, age, gender):
            self.name = name
            self.age = age
            self.gender = gender
        
        def introduction(self):
            return f"Hello, my name is {self.name}, I am {self.age} years old, and I am {self.gender}."
        
    class Employee(Person):
        def __init__(self, name, age, gender, job_title):
            super().__init__(name, age, gender)
            self.job_title = job_title

        def introduction(self):
            return f"Hello, my name is {self.name}, I am {self.age} years old, and I am {self.gender}. I work as {self.job_title}."
        
    person_1 = Employee("sagar", 20, "male", "programmer")

    
    
    print(person_1.introduction())

