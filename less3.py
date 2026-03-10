# # l1
# myFilms = ["Ted", "Iron Man", "Forest Gamp", "Remember", "Matrix"]
# print(f"{myFilms[0]}, {myFilms[-1]}")

# color = ["red", "blue", "green"]
# color.append("violet")
# print(color)
# color[1]= "yellow"
# print(color)

# days = ("monday", "tuesday", "wednesday" "thursday")
# days[-1]= "friday"
# print(days)

# l2
# person = {
#     "name": "Slava",
#     "age": 31,
#     "city": "Stryi"
# }
# print(f"Hello, my name {person['name']}, i have {person['age']}, i live in {person["city"]}")
# person.update({"hobby": "tennis", "learn": "py"})
# # del person["city"]
# person.pop("city")
# print(person.values())

# l3 
# numbers = [1, 2, 5, 8, 12] 
# newList = [i * 2 for i in numbers]
# print(newList)

# products = ["bread", "milk", "egg", "better"]
# for (i, product) in enumerate(products):
#     print(f"{i+1}. {product}")

# ?
# priceList ={"apple": 12, "orange": 22, "banana": 20, "potato": 10}
# for element, price in priceList.items():
#     if price > 18:
#         print(element)

# l4
# point=[(1, 2), (3, 4), (5, 6)]
# for coord in point:
#     print(f"КоординатаX: {coord[0]}, КоординатаY: {coord[1]}")

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# total = 0
# for list in matrix:
#     print("\n")
#     for number in list:
#         if number == 50:
#             number = 500
#         total += number
#         print(number, end=" ")
# print(f" {"\n" * 2}matrix sum = {total}")

# l = len(matrix)
# for i in range(l):
#     matrix[i][i]="X"
#     matrix[i][l-i-1]="O"
# for mat in matrix:
#     print(mat, end="\n")
