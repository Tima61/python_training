# Кортежи в Python - это неизменяемые упорядоченные объекты, похожие на списки, но без возможности добавления, удаления или изменения элементов.
# Создание кортежа с одним элементом без запятой приводит к созданию обычного целого числа.

# my_tuple = (1, 2, 3)
# print(type(my_tuple))
#
# my_tuple = tuple((1, 2, 3))
# print(type(my_tuple))

my_list = ["python", "is", "awesome"]
my_tuple = ("python", "is", "awesome")

# print(my_list.__sizeof__())
# print(my_tuple.__sizeof__())

my_tuple = ("python", "is", "awesome")

# print(my_tuple[0])
# print(my_tuple[1])
# print(my_tuple[2])
# print(my_tuple[0:3])
# print(my_tuple[:3])
# print(my_tuple[:])

# print(len(my_tuple))
# my_tuple[0] = "php" -- 'tuple' object does not support item assignment

my_tuple = ("python", "is", "awesome", [1, 2, 3], 85, ("a", "b", "c"), 85, {"user": "Mr.Anderson"})
my_tuple[3].append(99)
# print(my_tuple)

# print(my_tuple.count("python"))
# print(my_tuple.count(85))



