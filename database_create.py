import sqlite3


# used to create a book database
def database_book_create():
    mydb = sqlite3.connect('books.db')
    mycursor = mydb.cursor()
    mycursor.execute('''create table if not exists books(
                    id integer primary key,
                    title text,
                    author text,
                    ISBN TEXT,
                    availability TEXT
    )
    ''')

    mydb.commit()
    mydb.close()


def database_user_creation(): 
    mydb = sqlite3.connect('user_database.db')
    mycursor = mydb.cursor()
    mycursor.execute('''CREATE TABLE IF NOT EXISTS user(
                        id INTEGER PRIMARY KEY,
                        user_name TEXT,
                        password TEXT,
                        books_borrowed TEXT
                    )''')
    mydb.commit()
    mydb.close()



# used to remove user
def remove_user_account(username, password): 
    mydb = sqlite3.connect('user_database.db')
    mycursor = mydb.cursor()
    mycursor.execute('''
                delete from user where user_name = ? and password = ?
            ''',(username, password))
    mydb.commit()
    mydb.close()

# used to insert user data while creating account
def data_insert(username, password, book_borrowed = None):
        mydb = sqlite3.connect('user_database.db')
        mycursor = mydb.cursor()
        mycursor.execute('''INSERT INTO user (user_name, password, books_borrowed) VALUES (?, ?, ?)''', (username, password, book_borrowed))
        mydb.commit()
        mydb.close()
        return True


import sqlite3

# Function to update user's borrowed books in the database
def book_barrow_user_update(barrowed_book, username):
    try:
        with sqlite3.connect('user_database.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''select * from user where user_name = ?''', (username,))
            user = cursor.fetchone()

            if user:
                # Update user's borrowed books
                cursor.execute('''update user set books_borrowed = ?
                                    where user_name = ?''', (barrowed_book, username))
                connection.commit()
                print(f"User '{username}' successfully borrowed the book '{barrowed_book}'.")
                return True
            else:
                print(f"User '{username}' not found.")
                return False

    except sqlite3.Error as error:
        print("SQLite error:", error)
        return False


def update_barrowed_book(barrowed_book, author):
    mydb = sqlite3.connect('books.db')
    mycursor = mydb.cursor()
    mycursor.execute('''
                    update books
                    set availability = 'unavailable'
                    where title = ? and author = ?
                    ''',(barrowed_book,author))
    mydb.commit()
    mydb.close()
    return False

def already_borrowed_book(username):
    mydb = sqlite3.connect('user_database.db')
    mycursor = mydb.cursor()
    mycursor.execute('''
                    select user_name from user
                    where books_borrowed = 'None'
                    ''')
    mydb.commit()
    mydb.close()
    return True

def book_retured(username):
    mydb = sqlite3.connect('user_database.db')
    mycursor = mydb.cursor()
    mycursor.execute('''
                    select user_name from user
                    where books_borrowed = 'None'
                    ''')
    mydb.commit()
    mydb.close()
    return True

# used to check whether user is exists or not while login
def check_user(username, password=None):
    mydb = sqlite3.connect('user_database.db')
    mycursor = mydb.cursor()

    if password:
        # Check username/password combination
        mycursor.execute('SELECT * FROM user WHERE user_name = ? AND password = ?', (username, password))
    else:
        # Check username existence
        mycursor.execute('SELECT * FROM user WHERE user_name = ?', (username,))

    fetched_username = mycursor.fetchone()

    mydb.close()

    return fetched_username is not None

# used to insert the book
def insert_book(title, author, ISBN, availability):
    mydb = sqlite3.connect('books.db')
    mycursor = mydb.cursor()
    mycursor.execute('''insert into books(title, author, ISBN, availability)
                    values(?, ?, ?, ?)
                    ''', (title,author, ISBN, availability) )
    mydb.commit()
    mydb.close()

# used to remove the book from book database
def remove_book_database(title, author):
    mydb = sqlite3.connect('books.db')
    mycursor = mydb.cursor()
    mycursor.execute('''delete from books 
                     where title = ? and author = ? ''',(title, author))
    
    mydb.commit()
    mydb.close()

# Check if the book is available for borrowing
def check_book_availability(title, author):
    mydb = sqlite3.connect('books.db')
    mycursor = mydb.cursor()
    mycursor.execute('''
                SELECT * FROM books
                WHERE title = ? AND author = ? AND availability = 'available'
                ''', (title, author))
    books = mycursor.fetchall()
    mydb.close()
    
    return len(books) > 0


def remove_borrowed_book(title, username):
    try:
        mydb = sqlite3.connect('user_database.db')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT books_borrowed FROM user WHERE user_name = ?", (username,))
        fetched_books = mycursor.fetchone()
        if fetched_books:
            borrowed_books = fetched_books[0].split(',')
            if title in borrowed_books:
                borrowed_books.remove(title)
                updated_books = ','.join(borrowed_books)
                mycursor.execute("UPDATE user SET books_borrowed = ? WHERE user_name = ?", (updated_books, username))
                mydb.commit()
                mydb.close()
                return True
        return False
    except sqlite3.Error as e:
        print("Error removing book from user's borrowed books:", e)
        return False

# Helper function to update book availability in the database
def update_book_availability(title, author):
    try:
        mydb = sqlite3.connect('books.db')
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE books SET availability = 'available' WHERE title = ? AND author = ?", (title, author))
        mydb.commit()
        mydb.close()
        return True
    except sqlite3.Error as e:
        print("Error updating book availability in the database:", e)
        return False

def search_book(search_term):
    try:
        mydb = sqlite3.connect('books.db')
        mycursor = mydb.cursor()

        # Search for the book by title, author, or ISBN
        mycursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR ISBN LIKE ?", 
                         ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
        books = mycursor.fetchall()
        mydb.close()

        if books:
            print("\nSearch results:\n")
            print("{:<20} {:<20} {:<15} {:<15}".format("Title", "Author", "ISBN", "Availability"))
            print("-" * 70)
            for book in books:
                print("{:<20} {:<20} {:<15} {:<15}".format(book[1], book[2], book[3], book[4]))
        else:
            print("\nNo matching books found.")

    except sqlite3.Error as e:
        print("Error searching for book:", e)

# database_book_create()
# database_user_creation()
# table_alter()
# database_user_creation()
# data_insert("john_doe", "password123")
# data_insert("john", "password123", 'Harry potter')

