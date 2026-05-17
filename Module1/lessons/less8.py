# #1
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
# class Card():
#     def __init__(self):
#         self.items = []
#     def add_to_cart(self, product):
#         self.items.append(product)
#     def total_price(self):
#         return sum(item.price for item in self.items)
# class Payment:
#     def pay(self, amount):
#         print(f"Payment of {amount} has been made.")

# class Order:
#     def __init__(self, cart, payment):
#         self.cart = cart
#         self.payment = payment
#     def checkout(self):
#         if self.cart.total_price() == 0:
#             return print("Your cart is empty.")
#         total = self.cart.total_price()
#         return self.payment.pay(total)

# prod1=Product("tomato", 100)
# prod2=Product("potato", 200)

# cart=Card()
# cart.add_to_cart(prod1)
# cart.add_to_cart(prod2)

# payment=Payment()
# order=Order(cart, payment)
# order.checkout()

# #2
# class Role:
#     def can_edit(self):
#         return False
#     def can_view(self):
#         return True
#     def can_delete(self):
#         return False

# class Admin(Role):
#     def __init__(self):
#         super().__init__()
#     def can_edit(self):
#         return True
#     def can_delete(self):
#         return True
    
# class User(Role):
#     def __init__(self):
#         super().__init__()
#     def can_edit(self):
#         return True
    
# class Guest:
#     def __init__(self):
#         super().__init__()

# class Check:
#     def check_permissions(role: Role):
#         if role.can_edit() == True:
#             return print("You can edit.")
#         else:
#             return print("You do not have permission to edit.")
        
# admin=Admin.can_edit()
# user=User()
# guest=Guest.can_edit()

# checker=Check()
# checker.check_permissions(admin)

# #3
# class NotificationService:
#     def __init__(self):
#         self.add_channels = []
#         self.send_queue = 0
#         self.history = []
#     def add_channel(self, channel):
#         self.add_channels.append(channel)
#     def send_notification(self, message):
#         for channel in self.add_channels:
#             channel.send(message)
#             self.send_queue += 1
#             self.history.append(message)
        

# class EmailChannel:
#     def send(self, message):
#         print(f"Sending email notification: {message}")
# class SMSChannel:
#     def send(self, message):
#         print(f"Sending SMS notification: {message}")

# sms_channel = SMSChannel()
# email_channel = EmailChannel()
# notification_service = NotificationService()
# notification_service.add_channel(sms_channel)
# notification_service.add_channel(email_channel)

# notification_service.send_notification("Hello, this is a message.")
# quantity = notification_service.send_queue
# print(f"Total notifications sent: {quantity}")

#4
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# class Inventory:
#     def __init__(self):
#         self.products = {}
#         self.reserved = {}
        
#     def add(self, product, qty):
#         if product.name not in self.products:
#             self.products[product.name] = 0
#         self.products[product.name] += qty

#     def remove(self, product, qty):
#         if self.products.get(product.name, 0) < qty:
#             raise Exception("Not enough stock")
#         self.products[product.name] -= qty

#     def reserve(self, product, qty):
#         if self.products.get(product.name, 0) < qty:
#             raise Exception("Not enough stock to reserve")
#         self.reserved[product.name] = self.reserved.get(product.name, 0) + qty
#         self.remove(product, qty)

#     def rollback(self, product, qty):
#         if self.products.get(product.name, 0) < 0:
#             raise Exception("Cannot rollback more than available stock")
#         self.reserved[product.name] -= qty
#         self.add(product, qty)

# inventory = Inventory()
# item1 = Product("Laptop", 1000) 
# item2 = Product("Phone", 500)
# inventory.add(item1, 10)
# inventory.add(item2, 20)
# product = inventory.products
# inventory.reserve(item1, 5)
# print(product)
# inventory.rollback(item1, 2)
# print(product)
# print(inventory.reserved)