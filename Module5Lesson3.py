"""
APPLYING SQL IN PYTHON

When dealing with several databases, Python is your tool to efficiently connect with & manage a structured collection of data.
Python facilitates interaction with the database, retrieving & organizing data effectively. It unlocks sections to access databases such as MySQL, SQLite, and PostgreSQL.

Think of SQL queries in Python as the librarian's magic wand. A simple command summons books (data) from any shelf (table) in our library.
These queries empower us to read, add, update, & remove books with ease.

In Python, a cursor plays the role of librarian's assistant. It acts as an intermediary facilitating communication with the database. We give instructions (execute queries)
, & the cursor fetches or rearranges the books accordingly.
"""

# TO INSTALL MYSQL CONNECTOR PUT THE FOLLOWING IN THE TERMINAL & RUN (pip install mysql-connector-python)

# ESTABLISHING A CONNECTION TO MYSQL DATABASE
import mysql.connector
from mysql.connector import Error

# DATABASE CONNECT PARAMETERS
db_name = "e_commerce_db"
user = "root"
password = "your_root_password"
host = "localhost"

try:
    conn = mysql.connector.connect(
        database = db_name,
        user = user,
        password = password,
        host = host
    )

    if conn.is_connected():
        print("Connected to MySQL database successfully")

except Error as e:
    print(f"Error: {e}")

finally:
    if conn and conn.is_connected():
        conn.close()
        print("MySQL connection is closed.")

"""
In the e_commerce_db library from the previous lesson, 2 key shelves stand out: Customers and Orders.
The Customers shelf holds books labeled with id, name, email, & the recently added phone details.
On the other hand, the Orders shelf records id, date, and links (customer_id) to specific books in the Customers shelf. 

EXAMPLE: RETRIEVING DATA
try:
    conn = mysql.connector.connect(database="e_commerce_db", ...)
    cursor = conn.cursor()

    query = "SELECT * FROM Customers"

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if conn and conn.is_connected():
        cursor.close()
        conn.close()

Creating a Cursor (cursor=conn.cursor()): The cursor is a tool that helps you communicate with the database.

Defining the SQL Query (query = "SELECT * FROM Customers"): It's a request to view everything that's stored in the Customers table of our database.

Executing the Query (cursor.execute(query)): By executing the query, you're asking the cursor to go to the Customers shelf & gather the information (data) you requested.

Fetching the Results (for row in cursor.fetchall():print(row)): The fetchall() method is like having your assistant bring all the books to your desk. THe for loop then goes through each 
book (row of data) & print(row) displays the contents of each book.

EXAMPLE: ADDING DATA
try: 
    conn = mysql.connector.connect(database="e_commerce_db", ...)
    cursor = conn.cursor()

    new_customer = ("John Doe", "john.doe@example.com", "1234567890)

    query = "INSERT INTO Customers (name, email, phone) VALUES (%s, %s, %s)"

    cursor.execute(query, new_customer)
    conn.commit()
    print("New customer added successfully.)

except Error as e:
    print(f"Error: {e}")

finally:
    if conn and conn.is_connected():
        cursor.close()
        conn.close()

Preparing new_customer = ("John Doe", "john.doe@example.com", "1234567890): includes customer information, like compiling & binding a book before shelving.

Writing the SQL instruction query = "INSERT INTO Customers (name, email, phone) VALUES (%s, %s, %s)": SQL instruction for shelving a new book. INSERT INTO Customers directs the assistant to place
it on the Customers shelf and (name, email, phone) designates where to put each piece of information. VALUES (%s, %s, %s) acts as a placeholder for the actual content, provided separately.

Placing the Book on the Shelf (cursor.execute(query, new_customer)): You give your assistant the book & instruction note. Executing the query with the new_customer tuple instructs the
assistant on placing specific content in each section of the book, & the assistant prepares it accordingly.

Finalizing the Addition(conn.commit()): It finalizes the addition of the new book, ensuring it is recorded & accessible in the library database.

EXAMPLE: UPDATING DATA
Imagine you need to update details for a book on the Customers shelf, such as changing a customer's phone number.

Prepare the Update Information: First, gather the new information. Let's say we need to update John Doe's phone number, assuming he has an ID of 5.
updated_customer = ("9876543210", 5)

Write the Update Instruction: Next, create an instruction note specifying the update.
query = "UPDATE Customers SET phone = %s WHERE id = %s"

Executing the Update: Hand over the instruction note to your assistant (the cursor) to update the books details.
cursor.execute(query, updated_customer)
conn.commit()

EXAMPLE: REMOVING DATA
Occasionally, a book (data entry) may need to be eliminated from the shelf.

Identify the Book for Removal: Determine which book to remove, for example, John Doe's record with an id of 5.
customer_to_remove = (5, )

Write the Deletion Instruction: Create a note directing the removal of the book.
query = "DELETE FROM Customers WHERE id = %s"

Execute the Deletion: Instruct your assistant (the cursor) to remove the specified book.
cursor.execute(query, customer_to_remove)
conn.commit()

In this scenario, the DELETE FROM Customers command guides the removal of a book from the Customers shelf. The WHERE id = %s clause specifies the book to remove, & the conn.commit() finalizes the removal.

Remember! When trying to delete a customer who has associated order details, the MySQL database won't allow the deletion of a customer if there are linked orders in the Orders table, so
we need to handle exceptions that may arise due to the foreign key constraints in our database.

As digital librarians managing the e_commerce_db MySQL library, we've organized the 'Customers' shelf. Now, lets establish links between Customers and Orders, ensuring each order is connected
to its respective customer, similar to a book series & its author.

In our database, Customers and Orders are like separate book series. Each Customers book has a unique ID, & the Orders series references these IDs, forming a foreign key relationship that
links each order to a specific customer book.

EXAMPLE: INSERTING AN ORDER LINKED TO A CUSTOMER
To initiate a new order for a customer, we begin by determining the customer's unique ID & then proceed to generate a fresh entry on the Orders shelf.

Locating the Customer ID: For instance, if we aim to place an order for John Doe, we must first retrieve his exclusive ID from the Customers shelf. 

Generating the New Order: With John Doe's ID in hand, we establish a new entry on the Orders shelf, establishing a connection to his ID.

from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        john_doe_id = 6
        order_date = "2024-01-15"

        query = "INSERT INTO Orders (date, customer_id) VALUES (%s, %s)

        cursor.execute(query, (order_date, john_doe_id))
        conn.commit()
        print("Order added successfully for John Doe.)

    finally:
    cursor.close()
    conn.close()

EXAMPLE: UPDATING & DELETING ORDERS

Updating an Order: In cases where adjustments are necessary, such as changing the order date, we pinpoint the particular order by its ID & modify the pertinent details.

Deleting an Order: If an order is canceled or no longer needed, it requires removal from the Orders shelf.

EXAMPLE: SELECTING ORDERS FOR A CUSTOMER NAMED CAROL
"""

"""
INTEGRATING SQL WITH PYTHON APPLICATIONS
Let's explore how to fetch, update, & organize our data accessible to others - through graphical user interface (GUIs), console applications & web APIs. Its like opening different windows into
our library, each offering a unique view & interaction method for our patrons (users).

THE CONSOLE APPROACH
For those who prefer a more direct approach, a console-based application offers a no-frills, efficient way to interact with our library database.

Building the Interface: Pythons simplicity makes it ideal for creating console applications. Users interact with the database through text-based commands, & the application responds with data or confirmation messages.

Effective for Administrators: This method is particularly effective for administrative tasks, like bulk updates or data migration, where a GUI might be overkill.

THROUGH THE WINDOW OF GUI - PYTHON & SQL IN HARMONY
Imagine creating a digital catalog where patrons can view, search, & modify the library's collection through a visually engaging interface.

Tools for the Trade: Libraries like Tkinter, PyQt, or Kivy in Python can be used to craft these GUI applications. These tools allow us to create windows, buttons, text fields, & more offering
a user friendly way to interact with our database.

WEB APIs
In the final step, we unlock our library's potential for the digital work through a web API. This remove access point allows seamless integration with external systems & facilitates interactions w/ our database.

Flask or Django Power: Utilizing Python frameworks like Flask or Django, we can create web APIs capable of handling HTTP requests, enabling users or systems to retrieve & modify data.

Global Accessibility: The web API extends our library's accessibility worldwide, supporting integration w/ various platforms such as web applications, mobile apps & third party services.
"""

"""
ERROR HANDLING & CLEAN CODE IN DATABASE OPERATIONS

The importance of Error Handling in Database Operations: Just as a librarian must be prepared for unexpected events - a misplaced book or an inaccurate catalog entry - so must our scripts
be ready to handle unexpected scenarios. Error handling in database operations is crucial for several reasons:
    Preventing Data Corruption: Just like a librarian avoids misplacing books, our scripts should prevent erroneous data manipulation.
    Maintaining System Stability: A librarian aims to keep the library orderly; similarly, our scripts should ensure the database system remains stable & accessible even when errors occur.
    Informative Feedback: A good librarian informs patrons of issues; our scripts should provide clear error messages to help.

Try-Except Blocks: The Safety Nets
In our Python scripts, the try-except blocks act as safety nets, catching exceptions that might be thrown during database operations. For example, when connecting to a database, executing
a query, or closing a connection, there's always a possibility of encountering issues like connection failures or syntax errors in SQL statements. The try-except structure allows our script to 
gracefully handle these exceptions.

Clean Code: The Organized Library
Writing clean, readable code is like maintaining a well-organized library, enhancing understanding, maintainability, and error prevention.
    Modular Functions: Just as a library has sections, our code should be modular, with each function handling a specific task like adding a new book or fetching details, ensuring manageability.
    Descriptive Variable Names: Clear & descriptive variable & function names, akin to accurate shelf labels, enhance code comprehension for others or future reference.
    Consistent Formatting: Consistent code formatting, like neatly organized books, improves readability & error detection.


Specific Exceptions: Catch specific exceptions instead of a general one, similar to identifying the specific reason a book can't be found - whether its check out, misplaced or lost.

Resource Management: Always close resources like database connections, even in case of errors. This can be done in a finally block or using a context manager (with statement).
"""