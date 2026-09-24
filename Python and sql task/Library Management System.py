# Library Management System

FILE_NAME = "books.txt"


# Function to check empty input
def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value == "":
            print("Input cannot be empty. Please try again.")
        else:
            return value


# Add a new book
def add_book():
    book_id = get_non_empty_input("Enter Book ID: ")
    title = get_non_empty_input("Enter Book Title: ")
    author = get_non_empty_input("Enter Author Name: ")

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:
                data = line.strip().split("|")

                if data[0] == book_id:
                    print("Book ID already exists.")
                    return

    except FileNotFoundError:
        pass

    with open(FILE_NAME, "a") as file:
        file.write(
            f"{book_id}|{title}|{author}|Available\n"
        )

    print("Book added successfully.")


# View all books
def view_books():
    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

            if not books:
                print("No books available.")
                return

            print("-" * 75)
            print(
                f"{'ID':<10}"
                f"{'Title':<25}"
                f"{'Author':<20}"
                f"{'Status':<15}"
            )
            print("-" * 75)

            for line in books:
                data = line.strip().split("|")

                print(
                    f"{data[0]:<10}"
                    f"{data[1]:<25}"
                    f"{data[2]:<20}"
                    f"{data[3]:<15}"
                )

            print("-" * 75)

    except FileNotFoundError:
        print("No books available.")


# Search for a book
def search_book():
    book_id = get_non_empty_input("Enter Book ID: ")

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:
                data = line.strip().split("|")

                if data[0] == book_id:

                    print("\nBook Found")
                    print("Book ID :", data[0])
                    print("Title   :", data[1])
                    print("Author  :", data[2])
                    print("Status  :", data[3])

                    return

            print("Book not found.")

    except FileNotFoundError:
        print("No books available.")


# Update a book
def update_book():
    book_id = get_non_empty_input("Enter Book ID to update: ")

    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

        found = False
        updated_books = []

        for line in books:

            data = line.strip().split("|")

            if data[0] == book_id:

                found = True

                print("\nCurrent Details:")
                print("Title :", data[1])
                print("Author:", data[2])
                print("Status:", data[3])

                new_title = get_non_empty_input(
                    "Enter New Title: "
                )

                new_author = get_non_empty_input(
                    "Enter New Author: "
                )

                data[1] = new_title
                data[2] = new_author

            updated_books.append("|".join(data) + "\n")

        if not found:
            print("Book not found.")
            return

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_books)

        print("Book updated successfully.")

    except FileNotFoundError:
        print("No books available.")


# Delete a book
def delete_book():
    book_id = get_non_empty_input("Enter Book ID to delete: ")

    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

        found = False

        updated_books = []

        for line in books:

            data = line.strip().split("|")

            if data[0] == book_id:

                found = True

                print("Book found:", data[1])

                confirmation = input(
                    "Are you sure you want to delete this book? (yes/no): "
                ).strip().lower()

                if confirmation != "yes":
                    print("Delete cancelled.")
                    return

                continue

            updated_books.append(line)

        if not found:
            print("Book not found.")
            return

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_books)

        print("Book deleted successfully.")

    except FileNotFoundError:
        print("No books available.")


# Borrow a book
def borrow_book():
    book_id = get_non_empty_input("Enter Book ID to borrow: ")

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
        print("No books available.")


# Return a book
def return_book():
    book_id = get_non_empty_input("Enter Book ID to return: ")

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
        print("No books available.")


# Main menu
def main():

    while True:

        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            update_book()

        elif choice == "5":
            delete_book()

        elif choice == "6":
            borrow_book()

        elif choice == "7":
            return_book()

        elif choice == "8":
            print("Thank you for using Library Management System.")
            break

        else:
            print("Invalid choice. Please select 1 to 8.")


main()

