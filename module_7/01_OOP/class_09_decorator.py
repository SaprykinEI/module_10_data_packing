class Publication:

    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year


    def display(self):
        print(f"Название: {self.__title}")
        print(f"Автор: {self.__author}")
        print(f"Год: {self.__year}")


    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year



class Book(Publication):

    def __init__(self, title, author, year, code):
        super().__init__(title, author, year)
        self.__code = code


    def display(self):
        super().display()
        print(f"Код книги {self.__code}")

    def get_code(self):
        return self.__code

    def get_book_data(self):
        return f"{self.get_title()}, {self.get_author()}, {self.get_code()}"


book = Book("Дубровский", "А.С. Пушкин", "2015", "23-015")
book.display()
print(book.get_book_data())