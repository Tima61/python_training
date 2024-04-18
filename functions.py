# название функции в нижнем регистре
# писать  комментарий в теле функции для обзначения функции она
def say_hello():
    """ Says hello world """

    print("Hello World!")

say_hello()

##############################
print('#'*20)
##############################

def say_hello_name(username):
    """ Says hello name """

    print(f"Hello {username}!")

say_hello_name('Oleg')
say_hello_name('Max')

##############################
print('#'*20)
##############################

def say_name_age(username, age):
    """ Says hello name and age """

    print(f"Hello {username}!")
    print(f"You are {age} years old.")
    print('-' * 20)


say_name_age('Oleg', 20)
say_name_age('Valera', 22)

#Функцмя с именованными аргументами
say_name_age(username='Tom', age=33)
say_name_age(age=39, username='Bob')

##############################
print('#'*20)
##############################

def numbers_sum(n1 = 2, n2 = 2):
    """ Sum two numbers """
    print(n1 + n2)

numbers_sum()
numbers_sum(n1=150, n2=160)

##############################
print('#'*20)
##############################

#Важно если параметр без значения он должен быть первым!
def numbers_sum_name(username, n1 = 6, n2 = 6):
    """ sum two numbers and name """

    print(f"Hello {username}!")
    print(n1 + n2)
    print('-' * 20)

numbers_sum_name(username='Tom', n1=8)
numbers_sum_name(username='Max', n1=8, n2=50)

##############################
print('#'*20)
##############################

#Функции с не обезательными параметрами

def check_user(username, age = 0):
    """ Check if a user is 18 years old. """

    print(f"Hello {username}!")

    if age >= 18:
        print(f"You are {age} years old.")

    print('-'*20)

check_user(username='Oleg')
check_user(username='Max', age=33)
check_user(username='Tom', age=16)

##############################
print('#'*20)
##############################

def sum(n1 = 2, n2 = 2):
    """ Sum two numbers """

    return n1 + n2

print(sum(n1=5, n2=5))
print(sum())

result = sum(n1=11, n2=11)
print(result)