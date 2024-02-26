from admin import Admin
from library import *
from book import *


while True:
    print("\nWelcome to the Library Management System\n")
    user_number = int(input('Press 1 for Admin\nPress 2 for User: '))

    if user_number == 1:
        print('\n--- Admin Login ---')
        admin_username = input('Enter admin username: ')
        admin_passwd = input('Enter admin password: ')
        admin = Admin(admin_username, admin_passwd)
        admin.AdminLogin()
        exit()

    elif user_number == 2:
        print('\n--- User Menu ---')
        print('1. Login')
        print('2. Create User Account')
        print('3. Remove User Account')

        user_input = int(input('Enter a valid option: '))

        if user_input == 1:
            print('\n--- User Login ---')
            user_name = input('Enter username: ')
            user_password = input('Enter password: ')
            library1 = Library(username=user_name, password=user_password)
            library1.user_login()

            print('\n--- Book Menu ---')
            print('1. Check Availability')
            print('2. Borrow Book')
            print('3. Return Book')
            print('4. Search Book')

            user_input = int(input('Enter an option: '))
            if user_input == 1:
                title = input('Enter the title: ')
                author = input('Enter the author: ')
                book1 = Books(title=title, author=author)
                book1.check_availability()

            elif user_input == 2:
                title = input('Enter the title: ')
                author = input('Enter the author: ')
                book1 = Books(user_name, title=title, author=author)
                book1.borrow_book()

            elif user_input == 3:
                title = input('Enter the title: ')
                author = input('Enter the author: ')
                book1 = Books(user_name, title=title, author=author)
                book1.return_book()

            elif user_input == 4:
                title = input('Enter the title: ')
                library1 = Library(title=title)
                library1.search_books()

        elif user_input == 2:
            print('\n--- Create User Account ---')
            user_name = input('Enter username: ')
            user_password = input('Enter password: ')
            library1 = Library(username=user_name, password=user_password)
            library1.create_user_account()
            exit()

        elif user_input == 3:
            print('\n--- Remove User Account ---')
            user_name = input('Enter username: ')
            user_password = input('Enter password: ')
            library1 = Library(username=user_name, password=user_password)
            library1.delete_account()
            exit()

    else:
        print('Invalid input! Please try again.\n')
