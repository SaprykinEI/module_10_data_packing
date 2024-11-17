class CakeForm:

    def __init__(self, dough, form, *args):
        self.dough = dough
        self.form = form
        if not args:
            self.ingridient = []
        else:
            self.ingridient = list(args)

        # print(f"Я кекс в форме - {self.form}, из текста - {self.dough}!")

    def make_dough(self):
        return f"Мы замешиваем тесто {self.dough}"

    def make_form(self):
        return f"Мы выкладываем тесто в форму {self.form}"

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