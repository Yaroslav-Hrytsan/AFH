# number = int(input("Enter a number: "))
# try:
#     result = 10 / number
#     print(f"Result: {result}")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# try:
#     int(" abc")
# except ValueError:
#     print(ValueError)
# except Exception:
#     print("error occurred.")

# try :
#     x= 10 / 0   
# except ZeroDivisionError:
#     print("division by zero is not allowed.")
# finally:
#     print("its not problem")


# try:
#     print(a)
# except NameError:
#     print("variable a is not defined.")


try:
    user_number = int(input("Enter a number: "))
    result = 100 / user_number
    print(f"Result: {result}")
except ZeroDivisionError:
    print("число не ділиться на 0")
except ValueError:
    print("це не число")