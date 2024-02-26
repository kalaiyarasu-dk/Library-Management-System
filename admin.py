from library import *
from database_create import *

admin_login = {'admin' : 'admin', 'passwd' : 'password'}

class Admin:

    def __init__(self, admin, password):
        self.__admin = admin
        self.__password = password

    def AdminLogin(self):
        if self.__admin == admin_login.get('admin') and self.__password == admin_login.get('passwd'):
            print('Login successful\n')
        else:
            print('Invalid username or password\n')
            return

        print('1. Add book')
        print('2. Remove book')
        print('3. Search Book')

        user_input = int(input('Enter an option: '))
        if user_input == 1:
            self.add_book()
        elif user_input == 2:
            self.remove_book()
        elif user_input == 3:
            self.book_search()
        else:
            print('Invalid option\n')

    def add_book(self):
        print('\n--- Add Book ---\n')
        title = input('Title: ')
        author = input('Author: ')
        ISBN = input('ISBN: ')
        availability = input('Availability: ')
        library = Library(title=title, author=author, ISBN=ISBN, availability=availability)
        library.add_book()
        print('Successfully added\n')

    def remove_book(self):
        print('\n--- Remove Book ---\n')
        title = input('Title: ')
        author = input('Author: ')
        remove_book_database(title, author)
        print('Successfully removed\n')

    def book_search(self):
        print('\n--- Search Book ---\n')
        title = input('Title : ')
        library1 = Library(title=title)
        library1.search_books()
