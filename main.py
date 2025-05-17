import json
import os

# ---------------- Helper Functions ----------------

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# ---------------- Add Book ----------------

def add_book():
    books = load_data("books.json")

    book_id = input("Enter book ID: ")
    for book in books:
        if book["id"] == book_id:
            print("❌ Book with this ID already exists.")
            return

    title = input("Enter book title: ")
    author = input("Enter author name: ")
    quantity = int(input("Enter quantity: "))

    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "quantity": quantity
    })

    save_data("books.json", books)
    print("✅ Book added successfully.")

# ---------------- View Books ----------------

def view_books():
    books = load_data("books.json")

    if not books:
        print("📂 No books available.")
        return

    print("\n📚 Available Books:")
    print("-" * 40)
    for book in books:
        print(f"ID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Quantity: {book['quantity']}")
        print("-" * 40)

# ---------------- Issue Book ----------------

def issue_book():
    books = load_data("books.json")
    issued = load_data("issued.json")

    student = input("Enter student name: ")
    book_id = input("Enter book ID to issue: ")

    for book in books:
        if book["id"] == book_id:
            if book["quantity"] > 0:
                book["quantity"] -= 1
                issued.append({
                    "student": student,
                    "book_id": book_id,
                    "title": book["title"]
                })
                save_data("books.json", books)
                save_data("issued.json", issued)
                print(f"✅ Book '{book['title']}' issued to {student}.")
                return
            else:
                print("❌ Book out of stock.")
                return

    print("❌ Book ID not found.")

# ---------------- Return Book ----------------

def return_book():
    books = load_data("books.json")
    issued = load_data("issued.json")

    student = input("Enter student name: ")
    book_id = input("Enter book ID to return: ")

    for record in issued:
        if record["student"] == student and record["book_id"] == book_id:
            for book in books:
                if book["id"] == book_id:
                    book["quantity"] += 1
                    break
            issued.remove(record)
            save_data("books.json", books)
            save_data("issued.json", issued)
            print(f"✅ Book '{record['title']}' returned by {student}.")
            return

    print("❌ No matching issued record found.")

# ---------------- Main Menu ----------------

def main():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Exit")
        print("4. Issue Book")
        print("5. Return Book")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            print("👋 Exiting program. Goodbye!")
            break
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        else:
            print("❌ Invalid choice. Try again.")

# ---------------- Run Program ----------------

if __name__ == "__main__":
    main()
