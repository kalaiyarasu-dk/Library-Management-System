from library import *
from database_create import *

class Books(Library):
    def __init__(self, username=None, password=None, title=None, author=None, ISBN=None, availability=None):
        super().__init__(username, password, title, author, ISBN, availability)

    def check_availability(self):
        if check_book_availability(self.title, self.author):
            print('Book is available')
        else:
            print('Book is Not available')


    def borrow_book(self):
        username = self.get_username()
        if already_borrowed_book(username):
            print('\nPls submit the borrowed book to get a new book.\n')
            exit()

        # Check book availability
        if check_book_availability(self.title, self.author):
            print(f"\nThe book '{self.title}' by {self.author} is available for borrowing.")
            # Update user's borrowed books in the database
            if book_barrow_user_update(self.title, username):
                print(f'{username} borrowed {self.title}.')
                if update_barrowed_book(barrowed_book=self.title, author=self.author):
                    print('Updated in Book database successfully, now the book is unavailable.\n')
                else:
                    print('------Error updating book availability in the database------\n')
            else:
                print("\nFailed to update user's borrowed books in the database.\n")
        else:
            print(f"\nThe book '{self.title}' by {self.author} is not available.\n")

    def return_book(self):
        username = self.get_username()
        if check_user(username):
            if self.title and self.author:
                print(f"\nUser '{username}' is returning the book '{self.title}' by {self.author}.")
                # Remove the book from the user's borrowed books
                if remove_borrowed_book(self.title, username):
                    print(f"Book '{self.title}' returned successfully.")
                    # Update the book's availability in the database
                    if update_book_availability(self.title, self.author):
                        print("Book availability updated in the database.\n")
                    else:
                        print("Failed to update book availability in the database.\n")
                else:
                    print("Failed to remove book from user's borrowed books.\n")
            else:
                print("\nTitle and author of the book to be returned must be provided.\n")
        else:
            print("\nUser not found.\n")
