#1
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def get_info(self):
#         return print(f"Name: {self.title}, author: {self.author}, published in {self.year}")
    
# book1 = Book("Seven Habits of Highly Effective People", "Stephen R. Covey", 1989)

# book1.get_info()

#2
# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def add(self):
#         return print(self.a + self.b)
#     def subtract(self):
#         return print(self.a - self.b)
#     def multiply(self):
#         return print(self.a * self.b)

# calc=Calculator(2, 15)
# calc.add()
# calc.subtract()
# calc.multiply()

#3
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         return print(f"Deposit successful. New balance: {self.balance}")
#     def withdraw(self, amount):
#         if self.balance <= amount:
#             return print("Insufficient funds.")
#         self.balance -= amount
#         return print(f"Withdrawal successful. New balance: {self.balance}")
#     def get_balance(self):
#         return print(f"{self.owner}'s balance: {self.balance}")

# John_account = BankAccount("John", 10000)
# John_account.withdraw(5000)
# John_account.deposit(2000)
# John_account.get_balance()

#4
# class Student:
#     def __init__(self, name, grades_semester):
#         self.name = name
#         self.grades_semester = grades_semester
#     def add_grade(self, grade):
#         self.grades_semester.append(grade)
#     def get_grades(self):
#         return print(f"{self.name}'s grades: {self.grades_semester}")
#     def get_average_grade(self):
#         average = sum(self.grades_semester) / len(self.grades_semester)
#         return print(f"{self.name}'s average grade: {average}")
    
# Student_1 = Student("Alex", [85, 90, 78])
# Student_1.add_grade(92)
# Student_1.get_grades()
# Student_1.get_average_grade()

#5
# class Vehicle:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#     def get_info(self):
#         return print(f"Model: {self.model}, Year: {self.year}")
#     def move(self):
#         return print(f"{self.model} is moving.")
    
# class Car(Vehicle):
#     def __init__(self, model, year):
#         super().__init__(model, year)
#     def move(self):
#         return print(f"{self.model} is driving on the road.")
# class Bike(Vehicle):
#     def __init__(self, model, year):
#         super().__init__(model, year)
#     def move(self):
#         return print(f"{self.model} is riding on the one-way street.")
# class Plane(Vehicle):
#     def __init__(self, model, year):
#         super().__init__(model, year)
#     def move(self):
#         return print(f"{self.model} is flying in the sky.")
    
# car1 = Car("Toyota Camry", 2020)
# plane= Plane("MiG-29", 2015)
# car1.move()
# plane.move()

#6
# class Employee:
    # def __init__(self, name, position, salary):
    #     self.name = name
    #     self.position = position
    #     self.salary = salary

# class Manager():
#     def work(self):
#         return print(f"Manager - is managing the team.")
# class Developer():
#     def work(self):
#         return print(f"Developer - is writing code.")
    
# class WhoIsDoing:
#     @staticmethod
#     def do_work(type_):
#         if type_ == "Manager":
#             return Manager()
#         elif type_ == "Developer":
#             return Developer.work()
#         else:
#             return print("Unknown employee type.")

# who_is_that = WhoIsDoing.do_work("Manager")
# who_is_that.work()

#7
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
# class Cart(Product):
#     def __init__(self, name, price):
#         super().__init__(name, price)
#         self.products = []
#     def add_product(self, product):
#         self.products.append(product)
#     def get_total_price(self):
#         total_price = sum(product.price for product in self.products)
#         return print(f"Total price: {total_price}")

# class DiscountProduct(Product):
#     def __init__(self, name, price, discount):
#         super().__init__(name, price)
#         self.discount = discount
#     def get_discounted_price(self):
#         discounted_price = self.price * (1 - self.discount / 100)
#         return print(f"Discounted price: {discounted_price}")

# prod = Product("Laptop", 1000)
# prod2 = Product("Mouse", 150)
# cart = Cart("My Cart", 0)
# cart.add_product(prod)
# cart.add_product(prod2)
# cart.get_total_price()

# discount = DiscountProduct("Headphones", 200, 20)
# discount.get_discounted_price()