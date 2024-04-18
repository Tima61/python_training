my_string_1 = "Hello World"
my_string_2 = 'Hello World'
my_string_3 = """Hello World"""
my_string_4 = "Hello 'good' World" #или использовать экранирование

#Конкатенация строк

my_string = "Hello World " + "Good Morning " + "Old Morning"
print(my_string)
print(len(
    my_string
))

print('-'*30)

stroka = 'Hi Timur!'

for index, symbols in enumerate(stroka):
    print(f"Номер символа - {index}: {symbols}")

print('-'*30)

for stroka in reversed(stroka):
    print(stroka)

print('-'*30)

str = "Python"
for mth in dir(str):
    print(mth)

print('-'*30)

#Вызов метода у объекта

str = str.upper()
print(str)
#
str = str.lower()
print(str)
#
str = str.title()
print(str)

strokaa = 'I like PHP!'
print(strokaa)
#
strokaa = strokaa.replace("PHP", "Python")
print(strokaa)

my_string  = "I like Python"
my_string = my_string.split(" ")
print(my_string)

my_string = "I " + "like " + "Python"
print(my_string)

my_string = "-".join(my_string)
print(my_string)

my_string  = "I like Python                "
my_string = my_string.strip()
print(my_string)

my_string  = "I like Python!"
my_string = my_string.strip("!")
print(my_string)

name = "Oleg"
my_string  = f"Привет {name}"
print(my_string)

my_string = "Python is awesome!"
my_string = my_string[0:6]
print(my_string)

my_string = my_string[7:9]
print(my_string)

print('-'*30)

my_string = "123456789"
print(my_string)
print(my_string[::2])
print(my_string[::-1])

