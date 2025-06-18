'''
Assignment
You've been tasked with writing the code for the wizard library.
Complete the Library and Book classes listed below.
Create the Book Class:
Create the __init__(self, title, author) method
Set .title and .author to the values of the parameters.
Create the Library Class:
Create the __init__(self, name) method
Initialize a .name member variable to the value of the name parameter.
Create a .books member initialized to an empty list.
Add the add_book(self, book) method:
Add book, the given Book instance, to the library's books instance variable by appending it to the end of the list.
Add the remove_book(self, book) method:
Create a new, empty list to hold the books you want to keep.
Loop through every book in the library’s books list.
If the book’s title and author do not match the one you want to remove, add it to the new list.
After checking all the books, replace the library’s books list with the new list.
Add the search_books(self, search_string) method:
For every book in the library check if the search_string is contained in the title or author field (case-insensitive).
Return a list of all books that match the search string, ordered in the same order as they were added to the library.
After a book is removed, it should no longer be returned in the search results.

Tips
You can use the .lower() method to convert a string to lowercase.
Avoid modifying a list while looping over it because it can skip items or cause errors; instead, create a new list with the items you want to keep or loop over a copy.
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        new_books = []
        for lib_book in self.books:
            if lib_book.title != book.title or lib_book.author != book.author:
                new_books.append(lib_book)
        self.books = new_books

    def search_books(self, search_string):
        search_string = search_string.lower()
        matching_books = []
        for book in self.books:
            if (
                search_string in book.title.lower()
                or search_string in book.author.lower()
                ):
                matching_books.append(book)
        return matching_books