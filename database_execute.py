import sqlite3

# Connect to the SQLite database
def database_books_execute():
    conn = sqlite3.connect('books.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve all data from the 'books' table
    cursor.execute('SELECT * FROM books')

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print the header for the books section
    print('\n-------------------------------- Books ---------------------------------------\n')

    # Print the data
    for row in rows:
        if row:
            print(row)
        else:
            print('nill')

    # Close the cursor and connection
    cursor.close()
    conn.close()

def database_user_execute():
    conn = sqlite3.connect('user_database.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Execute a SELECT query to retrieve all data from the 'books' table
    cursor.execute('SELECT * FROM user')

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print the header for the user section
    print('\n--------------------------------- User ---------------------------------------\n')

    # Print the data
    for row in rows:
        if row:
            print(row)
        else:
            print('nill')

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Print the user data
print('\n-------------------------------- User -------------------------------------------\n')
database_user_execute()

# Print the books data
print('\n-------------------------------- Books ------------------------------------------\n')
database_books_execute()
