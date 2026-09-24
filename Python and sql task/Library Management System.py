# Library Management System

FILE_NAME = "books.txt"


# Add a new book
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    # Check whether Book ID already exists
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if data[0] == book_id:
                    print("Book ID already exists.")
                    return

    except FileNotFoundError:
        pass

    # Add book to file
    with open(FILE_NAME, "a") as file:
        file.write(f"{book_id}|{title}|{author}|Available\n")

    print("Book added successfully.")


# Display all books
def view_books():
    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

            if not books:
                print("No books available.")
                return

            print("\nLibrary Books")
            print("-" * 70)
            print("ID\tTitle\t\tAuthor\t\tStatus")
            print("-" * 70)

            for line in books:
                data = line.strip().split("|")

                print(
                    f"{data[0]}\t"
                    f"{data[1]}\t\t"
                    f"{data[2]}\t\t"
                    f"{data[3]}"
                )

    except FileNotFoundError:
        print("No book file found.")


# Search for a book
def search_book():
    search_id = input("Enter Book ID to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if data[0] == search_id:
                    print("\nBook Found")
                    print("Book ID:", data[0])
                    print("Title:", data[1])
                    print("Author:", data[2])
                    print("Status:", data[3])
                    return

            print("Book not found.")

    except FileNotFoundError:
        print("No book file found.")


# Borrow a book
def borrow_book():
    book_id = input("Enter Book ID to borrow: ")

    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

        found = False
        updated_books = []

        for line in books:
            data = line.strip().split("|")

            if data[0] == book_id:
                found = True

                if data[3] == "Borrowed":
                    print("Book is already borrowed.")
                    return

                data[3] = "Borrowed"

            updated_books.append("|".join(data) + "\n")

        if not found:
            print("Book not found.")
            return

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_books)

        print("Book borrowed successfully.")

    except FileNotFoundError:
        print("No book file found.")


# Return a book
def return_book():
    book_id = input("Enter Book ID to return: ")

    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

        found = False
        updated_books = []

        for line in books:
            data = line.strip().split("|")

            if data[0] == book_id:
                found = True

                if data[3] == "Available":
                    print("Book is already available.")
                    return

                data[3] = "Available"

            updated_books.append("|".join(data) + "\n")

        if not found:
            print("Book not found.")
            return

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_books)

        print("Book returned successfully.")

    except FileNotFoundError:
        print("No book file found.")


# Main menu
def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            borrow_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            print("Thank you for using Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


main()

