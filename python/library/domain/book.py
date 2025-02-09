class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    def __str__(self):
        return f"Book id: {self.__book_id}; Title: {self.__title}; Author: {self.__author}"