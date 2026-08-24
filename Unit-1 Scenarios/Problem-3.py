class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def category(self):
        if self.price >= 1000:
            return "Premium"
        else:
            return "Standard"

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Category:", self.category())
        print("------------------------")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def display_all(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\n--- All Books ---")
            for book in self.books:
                book.display()


# Main Program
library = Library()

while True:
    print("\n===== Library Book Management System =====")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        price = float(input("Enter Price: "))

        book = Book(book_id, title, author, price)
        library.add_book(book)

    elif choice == 2:
        library.display_all()

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")


# OUTPUT:
# ===== Library Book Management System =====
# 1. Add Book
# 2. Display All Books
# 3. Exit
# Enter your choice: 1
# Enter Book ID: B101
# Enter Title: Python Programming
# Enter Author: John Smith
# Enter Price: 800
# Book added successfully!
#
# ===== Library Book Management System =====
# 1. Add Book
# 2. Display All Books
# 3. Exit
# Enter your choice: 1
# Enter Book ID: B102
# Enter Title: Data Structures
# Enter Author: Robert Brown
# Enter Price: 1200
# Book added successfully!
#
# ===== Library Book Management System =====
# 1. Add Book
# 2. Display All Books
# 3. Exit
# Enter your choice: 2
#
# --- All Books ---
# Book ID: B101
# Title: Python Programming
# Author: John Smith
# Price: 800.0
# Category: Standard
# ------------------------
# Book ID: B102
# Title: Data Structures
# Author: Robert Brown
# Price: 1200.0
# Category: Premium
# ------------------------
#
# ===== Library Book Management System =====
# 1. Add Book
# 2. Display All Books
# 3. Exit
# Enter your choice: 3
# Thank you!
