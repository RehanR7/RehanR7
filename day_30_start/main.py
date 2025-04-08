"""
# FileNotFound
with open("a_file") as file:
    file.read()

# KeyError
a_dictionary = {"key": "value"}
value = a_dictionary["non_existence_key"]

# IndexError
fruit_list = ["Apple", "Banana", "Orange"]
fruit = fruit_list[3]

# TypeError
text = "abc"
print(text + 5)
"""
from logging import exception

# try:
#     file = open("file_a.txt")
# except FileNotFoundError as error_message:
#     print(f"there was {error_message}")
#     file = open("file_a", "w")
#     file.write("something")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is the error i madeup")

# heigth = float(input("Height: "))
# weight = int(input("Weight: "))
# if heigth > 3:
#     raise ValueError("Human height should not be above 3 meters.")
#
# bmi = weight / heigth ** 2
# print(bmi)

# fruits = ["Apple", "Pear", "Orange"]
#
#
# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except:
#         print("Fruit pie")
#
#
# make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0
    try:
        for post in posts:
            total_likes = total_likes + post['Likes']
    except:
        print("There was an error")

    return total_likes


count_likes(facebook_posts)


