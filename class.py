# __init__ - это специальный метод в Python, который вызывается при создании экземпляра класса. Он используется для инициализации атрибутов объекта.
# self - это обязательный первый параметр в определении каждого метода класса в Python.
class Car:

    # Атрибут класса
    fuel_type = "Gasoline"

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

    @classmethod
    def get_fuel_type(cls):
        print(f"This car uses {cls.fuel_type}.")

# super() - это встроенная функция Python, которая используется для вызова методов родительского класса
class ElectricCar(Car):

    # Переопределение атрибута класса
    fuel_type = "Electricity"

    def __init__(self, brand, model, year):
        super().__init__(brand,model,year)
        self.battery_size = 70

    def describe_battery(self):
        print(f"This car has {self.battery_size}-kWh battery.")

    # Переопределение метода родительского класса
    def read_odometer(self):
        print(f"This electric car has {self.odometer_reading} miles on it.")

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

# Получаем тип топлива
Car.get_fuel_type()

# Создаем экземпляр класса ElectricCar
my_electric_car = ElectricCar('tesla', 'model s', 2020)

# Выводим описание электромобиля
print(my_electric_car.get_descriptive_name())

# Описываем батарею электромобиля
my_electric_car.describe_battery()

# Обновляем пробег электромобиля
my_electric_car.update_odometer(100)
my_electric_car.read_odometer()

# Получаем тип топлива электромобиля
ElectricCar.get_fuel_type()