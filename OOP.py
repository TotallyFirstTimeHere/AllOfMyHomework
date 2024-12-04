#Створи клас Ragtangle через конструктор клас має приймати довжину та ширину і зберігає їх в атрибутах
#height weight відповідно. Створи два методи, які будуть рахувати та повертати площу і периметр фігури.
class Rectangle:
    def __init__(self, height, width):
        self.h = height
        self.w = width

    def calculate_area(self):
        return self.h * self.w

    def calculate_perimeter(self):
        return 2 * (self.h + self.w)

class BankAcc:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def add_money(self, amount):
        if amount > 1:
            self.balance += amount
            self.balance = round(self.balance, 2)
            print(f"Додано {amount} USD. Новий баланс {self.balance} USD")
        else:
            print("Сума для додавання має бути більше нуля.")

    def remove_money(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.balance = round(self.balance, 2)
            print(f"Знято {amount} USD. Новий баланс: {self.balance} USD.")
        elif amount > self.balance:
            print("Недостатньо коштів на рахунку.")
        else:
            print("Сума для зняття має бути більше нуля.")


r = Rectangle(6, 9)
print(f"Площа: {r.calculate_area()}")
print(f"Периметр: {r.calculate_perimeter()}")
print()

account = BankAcc(100) #акаунт з початковим балансом
account.add_money(50)
account.remove_money(69)
account.remove_money(170)
account.add_money(-35)
account.remove_money(-10000000)
account.add_money(50.50)
account.add_money(0.0000004)
print()

#Завдання 3
#Створіть клас «Країна». Збережіть у класі: назву країни,
#азву континенту, кількість жителів країни, телефонний
#код країни, назву столиці, назву міст країни. Реалізуйте
#методи класу для введення-виведення даних та інших
#операцій.
class Country:
    def __init__(self, name, continent, population, phone_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def display_info(self):
        print(f"Назва країни: {self.name}")
        print(f"Континент: {self.continent}")
        print(f"Кількість жителів: {self.population} осіб")
        print(f"Телефонний код: +{self.phone_code}")
        print(f"Столиця: {self.capital}")
        print(f"Міста: {', '.join(self.cities)}")

    def add_city(self, city):
        # Метод для додавання міста до списку
        if city not in self.cities:
            self.cities.append(city)
            print(f"Місто {city} додано.")
        else:
            print(f"Місто {city} вже є у списку.")

    def remove_city(self, city):
        # Метод для видалення міста зі списку
        if city in self.cities:
            self.cities.remove(city)
            print(f"Місто {city} видалено.")
        else:
            print(f"Місто {city} не знайдено у списку.")

    def update_population(self, new_population):
        self.population = new_population
        print(f"Кількість жителів оновлено до {self.population} осіб.")


ukraine = Country(
    name="Україна",
    continent="Європа",
    population=41000000,
    phone_code=380,
    capital="Київ",
    cities=["Львів", "Одеса", "Харків", "Дніпро"]
)

ukraine.display_info()
ukraine.add_city("Запоріжжя")
ukraine.remove_city("Одеса")
ukraine.update_population(42000000)
print()
ukraine.display_info()


#Завдання 2
#Створіть клас «Місто». Збережіть у класі: назву міста,
#азву регіону, назву країни, кількість жителів у місті,
#поштовий індекс міста, телефонний код міста. Реалізуйте
#методи класу для введення-виведення даних та інших
#операцій.
class City:
    def __init__(self, name, region, country, population, postal_code, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def display_info(self):
        # Метод для виведення інформації про місто
        return (
            f"Назва міста: {self.name}\n"
            f"Регіон: {self.region}\n"
            f"Країна: {self.country}\n"
            f"Кількість жителів: {self.population}\n"
            f"Поштовий індекс: {self.postal_code}\n"
            f"Телефонний код: {self.phone_code}"
        )

    def update_population(self, new_population):
        # Метод для оновлення кількості жителів
        self.population = new_population

    def is_larger_than(self, other_city):
        # Метод для порівняння кількості жителів з іншим містом
        return self.population > other_city.population


# Приклад використання
city1 = City("Київ", "Київська область", "Україна", 2800000, "01001", "+38044")
city2 = City("Львів", "Львівська область", "Україна", 720000, "79000", "+38032")

print(city1.display_info())
print("\n---\n")
print(city2.display_info())

city1.update_population(2900000)
print(f"\nОновлена кількість жителів у {city1.name}: {city1.population}")

if city1.is_larger_than(city2):
    print(f"\n{city1.name} більше за {city2.name} за кількістю жителів.")
else:
    print(f"\n{city2.name} більше за {city1.name} за кількістю жителів.")
