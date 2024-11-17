# class Book:
#
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#
# book = Book("Dubrovsky", "A.S. Pushkin")
# print(book.title)
# print(book.author)
#
#
# book.title = 'Странный Человек'
# book.author = "M.Y. Lermontov"
# print(book.title)
# print(book.author)
# print()
#
#
# class Book:
#
#     def __init__(self, title, author):
#         self._title = title
#         self._author = author
#
#
# book = Book("Dubrovsky", "A.S. Pushkin")
# print(book._title)
# print(book._author)
#
#
# book._title = 'Странный Человек'
# book._author = "M.Y. Lermontov"
# print(book._title)
# print(book._author)


class Book:

    def __init__(self, title, author):
        self.__title = title
        self.__author = author


    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title, access='user'):
        if access == 'moderator':
            self.__title = title
            return f"Название книги изменено на {title}"
        else:
            return f"У Вас нет необходимых прав доступа!"

    def set_author(self, author, access='user'):
        if access == 'moderator':
            self.__author = author
            return f"Имя автора изменено на {author}"
        else:
            return f"У Вас нет необходимых прав доступа!"


book = Book("Dubrovsky", "A.S. Pushkin")
# print(book.get_title("Странный человек"))
# print(book.get_author("Лермонтов"))
#
# book.__title = "Странный человек"
# book.__author = "Лермонтов"


print(book.set_title("Странный человек", 'moderator'))
print(book.set_author("Лермонтов", 'moderator'))

print(book.get_title())
print(book.get_author())