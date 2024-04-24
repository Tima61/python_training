# __init__ - это специальный метод в Python, который вызывается при создании экземпляра класса. Он используется для инициализации атрибутов объекта.
# self - это обязательный первый параметр в определении каждого метода класса в Python.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"Year: {self.year}, Brand: {self.brand}, Model: {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kilometers on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# Создаем экземпляр класса Car

my_car = Car('audi', 'a4', 2019)

# Выводим описание автомобиля
print(my_car.get_descriptive_name())

# Обновляем пробег автомобиля
my_car.update_odometer(50)
my_car.read_odometer()

# Увеличиваем пробег автомобиля
my_car.increment_odometer(100)
my_car.read_odometer()
