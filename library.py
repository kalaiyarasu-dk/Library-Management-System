import sqlite3
from database_create import *

class Library:

    def __init__(self, username=None, password=None, title=None, author=None, ISBN=None, availability=None):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability = availability
        self.__username = username
        self.__password = password

    def add_book(self):
        insert_book(self.title, self.author, self.ISBN, self.availability)
        print("\nBook added successfully!\n")

    def remove_book(self, title, author):
        remove_book_database(title, author)
        print("\nBook removed successfully!\n")

    def search_books(self):
        print("\n--- Searching for Books ---")
        search_book(self.title)

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def user_login(self):
        if check_user(self.__username, self.__password):
            print(f'\nWelcome, {self.__username}! You have logged in successfully.\n')
        else:
            print('\nInvalid username or password. Please try again.\n')
            exit()

    def create_user_account(self):
        if check_user(self.__username):
            print('\nSorry, this username already exists. Please choose a different one.\n')
        else:
            if data_insert(self.__username, self.__password):
                print(f'\nAccount created successfully! Welcome, {self.__username}.\n')
            else:
                print('\nInvalid username or password. Please try again.\n')

    def delete_account(self):
        confirmation = input('\nAre you sure you want to delete your account? (Yes/No): ')
        if confirmation.capitalize() == 'Yes':
            remove_user_account(self.__username, self.__password)
            print(f'\nYour account ({self.__username}) has been successfully deleted.\n')
        elif confirmation.capitalize() == 'No':
            print('\nAccount deletion cancelled.\n')
        else:
            print('\nInvalid input! Please enter either "Yes" or "No".\n')


