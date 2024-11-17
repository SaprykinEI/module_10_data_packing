# class Human:
#
#     def __init__(self, name, birthday, phone, city, address):
#         self.name = name
#         self.birthday = birthday
#         self.phone = phone
#         self.city = city
#         self.address = address
#
#     def get_full_name(self):
#         return f"ФИО: {self.name}"
#
#     def get_birthday(self):
#         return f"Дата Рождения: {self.birthday}"
#
#     def get_phone_number(self):
#         return f"Номер телефона: {self.phone}"
#
#     def get_city(self):
#         return f"Город: {self.city}"
#
#     def get_address(self):
#         return f"Мой адресс: {self.address}"
#
#
# full_name = input("Введите ваше ФИО: ")
# birthday = input("Введите дату рождения: ")
# phone = input("Введите номер телефона: ")
# city = input("Введите город: ")
# address = input("Введите адрес: ")
# print()
#
#
# human_1 = Human(full_name, birthday, phone, city, address)
# print(human_1.get_full_name())
# print(human_1.get_birthday())
# print(human_1.get_phone_number())
# print(human_1.get_city())
# print(human_1.get_address())
#

class City:
    def __init__(self, name, region, country, population, post_code, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.post_code = post_code
        self.phone_code = phone_code


    def get_data(self):
        return f"Название города {self.name} Регион: {self.region} Население: {self.population}, Код телефона: {self.phone_code}"


    def set_population(self, new_population):
        self.population = new_population


    def set_phone_code(self, new_phone_code):
        self.new_phone_code = new_phone_code


    def set_post_code(self, new_post_code):
        self.new_post_code = new_post_code


Voronezh = City("Воронеж", "Воронежская область", "Russia", 1_300_000, 'Не знаю', '473')
print(Voronezh.get_data())
Voronezh.set_population(2_000_000)
print(Voronezh.get_data())



class Country:

    def __init__(self, name_country, continent, population, phone_code, capital,):
        self.name_country = name_country
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital

    def get_name_country(self):
        return f"Страна: {self.name_country}"

    def get_continet(self):
        return f"Континент: {self.continent}"

    def get_population(self):
        return f"Население: {self.population}"

    def get_phone_code(self):
        return f"Код телефона: {self.phone_code}"

    def get_capital(self):
        return f"Столица: {self.capital}"

    def set_population(self, new_population):
        self.population = new_population

country = input("Введите страну: ")
continent = input("Введите континент: ")
population = input("Введите кол-во населения: ")
phone_code = input("Введите код телефона: ")
capital = input("Введите столицу: ")


country_1 = Country(country, continent, population, phone_code, capital)
print(country_1.get_name_country())
print(country_1.get_continet())
print(country_1.get_population())
print(country_1.get_phone_code())
print(country_1.get_capital())

new_population = input("Введите новое кол-во население:")
country_1.set_population(new_population)
print(country_1.get_population())








class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
            self.numerator = numerator
            self.denominator = denominator
    def add(self, numerator_1, denominator_1):
        new_denominator = self.denominator * denominator_1
        new_nomenator = self.numerator * denominator_1
        new_nomenator_1 = numerator_1 * self.denominator
        return f"{new_nomenator + new_nomenator_1}/{new_denominator}"

    def multiply(self, numerator_1, denominator_1):
        new_numerator = self.numerator * numerator_1
        new_denominator = self.denominator * denominator_1
        return f"{new_numerator}/{new_denominator}"

    def divide(self, numerator_1, denominator_1):
        if denominator_1 == 0:
            raise ZeroDivisionError("На ноль делить нельзя")
            new_numerator = self.numerator * denominator_1
            new_denominator = self.denominator * numerator_1
            return f"{new_numerator}/{new_denominator}"


fraction_1 = Fraction(2, 3)

print(fraction_1.add(3, 5))
print(fraction_1.multiply(2, 4))
print(fraction_1.divide(2, 3))