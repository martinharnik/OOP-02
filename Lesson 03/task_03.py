class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"Title: {self.title}")
        print(f"Author {self.author}")
        print(f"Year: {self.year}")

class FictionBook(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def info(self):
        super().info()
        print(f"Genre: {self.genre}")


class NonFiction(Book):
    def __init__(self, title, author, year, topic):
        super().__init__(title, author, year)
        self.topic = topic

    def info(self):
        super().info()
        print(f"Topic: {self.topic}")    

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_book(self):
        for book in self.books:
            book.info()
            print()

    def search_author(self, author):
        found_books = []
        for book in self.books:
            if book.author == author:
                found_books.append(book)
        if found_books:
            print(f"Books by {author}: ")
            for book in found_books:
                book.info()
                print()
        else:
            print("No books found by this author!")

    def search_year(self, start_year, end_year):
        found_book = []
        for book in self.books:
            if start_year <= book.year <= end_year:
                found_book.append(book)
        
        if found_book:
            print(f"Books between {start_year} and {end_year}:")
            for book in found_book:
                book.info()
                print()
        else:
            print("Errors")

library = Library()

book1 = FictionBook("1984", "George Orwell", 1949, "Dystopian")
book2 = FictionBook("Brave New World", "Aldous Huxley", 1932, "Science Fiction")
book3 = NonFiction("Sapiens", "Yuval Noah Harari", 2011, "History")
book4 = NonFiction("Educated", "Tara Westover", 2018, "Memoir")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.display_book()

library.search_year(2010, 2020)