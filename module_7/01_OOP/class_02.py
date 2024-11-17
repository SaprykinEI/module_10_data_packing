class CakeForm:

    def __init__(self, dough, form):
        self.dough = dough
        self.form = form
        print(f"Я кекс в форме - {self.form}, из текста - {self.dough}!")

    def make_dough(self):
        return f"Мы замешиваем тесто"

    def make_form(self):
        return f"Мы выкладываем тесто в форму"

    def cook_cake(self, time=40):
        if time > 80:
            return f"За {time} минут кекс сгорит!"
        return f"Мы выпекаем кекс {time} минут"


cake_1 = CakeForm('Мучное', 'Круглая')
cake_2 = CakeForm('Овсяное', 'Квадратная')

# print(cake_1.make_dough())
# print(cake_1.make_form())
# print(cake_1.cook_cake())
# print()
# print(cake_2.make_dough())
# print(cake_2.make_form())
# print(cake_2.cook_cake(100))