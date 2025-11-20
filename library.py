# ---------------------------------------------------------------
# Library Inventory & Borrowing System
# Name: KRISHNA
# Roll No: 2501660036
# Date: 18/11/2025
# ---------------------------------------------------------------

# Dictionaries to store book data and borrow records
books = {}
borrowed = {}

# ---------------------------------------------------------------
# Task 1: MENU PRINTING
# ---------------------------------------------------------------

def print_menu():
    print("\n" + "-"*50)
    print("\t Welcome to Library Manager")
    print("-"*50)
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")
    print("-"*50)

# ---------------------------------------------------------------
# Task 2: ADD BOOK
# ---------------------------------------------------------------

def add_book():
    print("\n--- Add New Book ---")
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    copies = int(input("Enter Number of Copies: "))

    books[book_id] = {
        "title": title,
        "author": author,
        "copies": copies
    }

    print(f"\nBook '{title}' added successfully!")

# ---------------------------------------------------------------
# Task 3: VIEW BOOKS
# ---------------------------------------------------------------

def view_books():
    if not books:
        print("\nNo books available.")
        return

    print("\n--------------- Library Books ---------------")
    print("ID\tTitle\t\tAuthor\t\tCopies")
    print("---------------------------------------------")

    for bid, details in books.items():
        print(f"{bid}\t{details['title']}\t{details['author']}\t{details['copies']}")

# ---------------------------------------------------------------
# Task 3: SEARCH BOOK (BY ID OR TITLE)
# ---------------------------------------------------------------

def search_by_id(book_id):
    return books.get(book_id, None)

def search_by_title(title):
    for bid, details in books.items():
        if title.lower() in details["title"].lower():
            return bid, details
    return None

def search_book():
    print("\n--- Search Book ---")
    print("1. Search by ID")
    print("2. Search by Title")
    choice = input("Enter choice: ")

    if choice == "1":
        bid = input("Enter Book ID: ")
        result = search_by_id(bid)
        if result:
            print("\nBook Found:")
            print(f"{bid} -> {result['title']} by {result['author']} | Copies: {result['copies']}")
        else:
            print("Book Not Found.")

    elif choice == "2":
        name = input("Enter Title/Keyword: ")
        result = search_by_title(name)
        if result:
            bid, d = result
            print("\nBook Found:")
            print(f"{bid} -> {d['title']} by {d['author']} | Copies: {d['copies']}")
        else:
            print("Book Not Found.")

# ---------------------------------------------------------------
# Task 4: BORROW BOOK
# ---------------------------------------------------------------

def borrow_book():
    print("\n--- Borrow Book ---")
    student = input("Enter Student Name: ")
    book_id = input("Enter Book ID: ")

    if book_id not in books:
        print("Book does not exist.")
        return

    if books[book_id]["copies"] <= 0:
        print("No copies available right now.")
        return

    books[book_id]["copies"] -= 1
    borrowed[student] = book_id

    print(f"\n{student} borrowed {books[book_id]['title']} successfully!")

# ---------------------------------------------------------------
# Task 5: RETURN BOOK
# ---------------------------------------------------------------

def return_book():
    print("\n--- Return Book ---")
    student = input("Enter Student Name: ")

    if student not in borrowed:
        print("This student has not borrowed any book.")
        return

    book_id = borrowed[student]
    books[book_id]["copies"] += 1

    del borrowed[student]

    print("Book returned successfully!")

    # List comprehension for borrowed list
    borrowed_list = [f"{s} -> {b}" for s, b in borrowed.items()]
    print("\nCurrent Borrowed Books:")
    for entry in borrowed_list:
        print(entry)

# ---------------------------------------------------------------
# Task 6: LOOP & EXIT
# ---------------------------------------------------------------

# Pre-adding 5 books
books = {
    "B101": {"title": "Python Basics", "author": "Guido", "copies": 5},
    "B102": {"title": "DSA", "author": "Cormen", "copies": 3},
    "B103": {"title": "Algorithms", "author": "Sedgewick", "copies": 4},
    "B104": {"title": "AI Fundamentals", "author": "Russell", "copies": 2},
    "B105": {"title": "Cyber Security", "author": "Anderson", "copies": 6},
}

# Borrow examples for submission requirement
borrowed = {
    "Amit": "B101",
    "Neha": "B102"
}

while True:
    print_menu()
    option = input("Enter your choice: ")

    if option == "1":
        add_book()
    elif option == "2":
        view_books()
    elif option == "3":
        search_book()
    elif option == "4":
        borrow_book()
    elif option == "5":
        return_book()
    elif option == "6":
        print("Exiting Program... Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
