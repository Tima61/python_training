# my_list = []
# print(type(my_list))

# my_list_2 = list()
# print(type(my_list_2))

# my_list = [1, 2, 3, 4, 5 , 'hello world', ("1","2","3"), {'user':'john'}, [], '']
# print(my_list)

my_list_2 = ["red", "green", "blue", "Python", "PHP", "SQL"]

# print(my_list_2[-6])

print(len(my_list_2))

# Срезы это извлечение одного или нескольких объектов из коллекции
print(my_list_2[0:3])
print(my_list_2[:3])

print('-' * 30)

my_list_2 = ["red", "green", "blue", "Python", "PHP", "SQL"]
# my_list_2.append("Python IS COOOOOOOOOOOL")
# print(my_list_2)

# my_list_2.insert(1,"Python IS COOOOOOOOOOOL")
# print(my_list_2)

my_list_2.pop(-2)
print(my_list_2)

print('-' * 30)

list2 = ["Кушать", "пить кофе", "купаться"]
my_list_2.extend(list2)
print(my_list_2)

print('-' * 30)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
# print(c)

x = ['Hello'] + ["friend"] + [3300]
# print(x)

# print(my_list_2)
my_list_2.remove("Кушать")
print(my_list_2)

print('-' * 30)

my_list_2_copy = my_list_2.copy()
# print(my_list_2_copy)

print(my_list_2.count("купаться"))
print(my_list_2.index("купаться")) #Если в списке несколько одинаковых элементов, то вернет индекс первого в попавшего в списке

print('-' * 30)

# print(my_list_2)
# my_list_2.sort()
# print(my_list_2)

n_list = [-22,1, 2, 3, 234,44,233,66, 8,4]
n_list.sort()
print(n_list)
print('-' * 30)
# n_list.reverse()

print(n_list)

print(min(n_list))
print(max(n_list))

print('-' * 30)

my_str = ["М","а","м","а"]
my_str = "".join(my_str)
print(my_str)




