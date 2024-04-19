# my_dict_1 = {}
# my_dict_2 = dict()

# print(type(my_dict_1))
# print(type(my_dict_2))

my_dict = {
    "username": "Bob",
    "nickname": "Bob61",
    "team": ["Springfield", "Springfield1"],
    1: "One",
    2: "Two",
    (1, 2, 3): "numbers"
}

# print(my_dict)
# print(my_dict["username"])
# print(my_dict[1])
# print(my_dict[(1,2,3)])

months = {
    1: "January",
    2: "February",
    3: "March"
}

# print(months[2])

person = {
    "name": "Bob",
    "age": 30,
    "height": 40,
}

# print(f"{person["name"]} age is {person['age']} years old")

person["weight"] = 75
person["nationality"] = "Russian"
# print(person)

person["name"] = "Tom"
# print(person)

del person["weight"]
print(person)

person["car"] = ["BMW", "Ford"]

for k, v in person.items():
    print(f"{k}: {v}")

print("-" * 30)

for key in person:
    print(key)

print("-" * 30)

for key in person.keys():
    print(key)

print("-" * 30)

if "car" in person.keys():
    print("The key 'car' is present")
else:
    print("The key 'car' is not present")

print("-" * 30)

for key in person.values():
    print(key)

print("-" * 30)

for v in person["car"]:
    print(v)

print("-" * 30)

persons = {
    "Bob": {
        "username": "Bob",
        "nickname": "Bob61",
        "car": ["BMW", "Rols"],
        "age": 30,
        "height": 40,
        "city": "Rostov"
    },
    "Sara": {
        "username": "Sara",
        "nickname": "Sara93",
        "car": ["MB", "Mybach"],
        "age": 22,
        "height": 35,
        "city": "Krasnodar"
    },
}

# for username, userinfo in persons.items():
#     print(f"Имя пользвоателя:{username}")
#     age = userinfo["age"]
#     car = userinfo["car"]
#     print(f"Возвраст: {age}")
#     print(f"автомобиль: {car}")

print("-" * 30)

print(person)
print(person.get("name"))

person.update({"job": "driver"})
print(person)

