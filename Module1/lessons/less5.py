def square(x): 
    return x ** 2
# print(square(5))

def even(n):
    if(n % 2 == 0):
        return "even-number"
    else:
        return "odd-number"
# print(even(4))

def square(h, w): return h * w
# print(square(5, 4))

def sToM (s):
    con = f"minutes:{s // 60}, second:{s % 60}"
    return con
# print(sToM(180))

number=[1, 10, 5, 2]
def maximus(n):
    return max(n)
# print(maximus(number))


def calculator(n1, n2, a):
    if a == "+":
        value = int(n1 + n2)
    elif a == "-":
        value = int(n1 - n2)
    elif a == "*":
        value = int (n1 * n2)
    elif a == "/":
        value = int( n1 / n2 )
    else: print('помилка введення')
    return value
# num1 = int(input("число №1 = "))
# act = input("введи дію: ")
# num2 = int(input("число №2 = "))
# print(f"Результат:{calculator(num1, num2, act)}")

print(eval(input('введіть вираз: ')))


