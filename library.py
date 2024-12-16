# Dictionary containing user credentials with usernames as keys and passwords as values.
users = {
    "admin": "1234",
    "user1": "password1",
    "user2": "password2",
    "user": "password"
}

# Dictionary containing library books with details such as author, publisher, and year of publication.
library = {
    "Cybersecurity Bible": {"Author": "Shawn Walker", "Publisher": "Unknown", "Year": 2024},
    "Hacked: The Secrets Behind Cyber Attacks": {"Author": "Jessica Barker", "Publisher": "Unknown", "Year": 2024},
    "The Cuckoo's Egg": {"Author": "Clifford Stoll", "Publisher": "Doubleday", "Year": 1989},
    "Countdown to Zero Day": {"Author": "Kim Zetter", "Publisher": "Crown", "Year": 2014},
    "Sandworm": {"Author": "Andy Greenberg", "Publisher": "Doubleday", "Year": 2019},
    "Social Engineering": {"Author": "Christopher Hadnagy", "Publisher": "Wiley", "Year": 2018},
    "Threat Modeling": {"Author": "Adam Shostack", "Publisher": "Wiley", "Year": 2014},
    "The Code Book": {"Author": "Simon Singh", "Publisher": "Doubleday", "Year": 1999},
    "Cult of the Dead Cow": {"Author": "Joseph Menn", "Publisher": "PublicAffairs", "Year": 2019},
    "Click Here to Kill Everybody": {"Author": "Bruce Schneier", "Publisher": "W. W. Norton & Company", "Year": 2018}
}

# Header strings used to format the output.
H1 = "====================================================================="
H2 = "---------------------------------------------------------------------"

# Welcome message and user menu options.
usr_welcome = H1 + "\nWelcome To library System\n" + H1 + "\nSelect Function\n\n=>1 Add Book\n\n=>2 Search Book\n\n=>3 Remove Book\n\n=>4 see all available books\n\n=>5 exit\n" + H1
current_library = "Current books in the library: "
selection = "Enter selection: "
selection2 = "\n=>1 Show entire library \n=>2 Search other books:\n" + "any other keys to go back home\n" + selection
bookN = "Enter book name: "
review_lib = "would you like to see entire library? \npress y to view the library \npress any other key to exit\n" + selection

# List of symbols and numbers not allowed in author or publisher names.
symbols = ['+', '-', '*', '/', '=', '%', '.', ',', '!', '?', ';', ':', "'", '"', '(', ')', '[', ']', '{', '}', '<', '>', '|', '\\', '_', '~', '^', '$', '#', '&', '@', '£', '€', '¥', '¢', '§', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Function to register a new user.
def user_reg():
    print("User registration area")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    # Check if username already exists, otherwise register the user.
    if username in users:
        print(f"{username} already exists.")
    else:
        users[username] = password
        print("User is registered successfully.")

# Function to authenticate existing users.
def user_auth():
    while True:
        print("Welcome! Please log in.")
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        # Check if username and password match.
        if username in users and users[username] == password:
            print("Authentication successful! Access granted.")
            return True
        else:
            print("Invalid username or password. Please try again.")

# Function to display all books in the library in a formatted manner.
def line_format():
    for book, details in library.items():
        print(f"Title: {book}")
        for key, value in details.items():
            print(f"  {key}: {value}")
        print()  # Add a blank line between books.

# Main function to start the library system.
def start():
    # Prompt user to register or login.
    while True:
        usr_reg_log = input(
            "Please either login or register before continuing!!!\n"
            "Select one of the following options:\n1 - Register \n2 - Login \n->"
        ).strip().lower()

        if usr_reg_log in {"register", "1"}:
            user_reg()
        elif usr_reg_log in {"log", "2"}:
            user_auth()
            break
        else:
            print("Invalid Selection:Select one of the following options:\n1 - Register \n2 - Login\n->")

    # Main menu loop.
    while True:
        print(usr_welcome)
        usr_selection = input(selection).strip()

        if usr_selection == "1":  # Add Book
            usr_book = input(bookN).strip().lower()

            # Prompt for book author and validate input.
            while True:
                usr_book_author = input("Enter book author: ").strip().lower()
                if any(char in symbols for char in usr_book_author):
                    print("Author name cannot contain symbols or numbers. Please enter again.")
                else:
                    break

            # Prompt for book publisher and validate input.
            while True:
                usr_book_publisher = input("Enter book Publisher: ").strip().lower()
                if any(char in symbols for char in usr_book_publisher):
                    print("Publisher name cannot contain symbols or numbers. Please enter again.")
                else:
                    break

            # Check if the book already exists in the library.
            if usr_book in library:
                if library[usr_book]["Author"].lower() == usr_book_author:
                    print("Book already exists in the library with the same author.")
                else:
                    print("Book with a different author has been added.")
            else:
                library[usr_book] = {"Author": usr_book_author, "Publisher": usr_book_publisher}
                print("Book has been added.")

        elif usr_selection == "2":  # Search Book
            search_book_name = input(bookN).strip().lower()

            # Check if the book exists in the library.
            if search_book_name in library:
                print(search_book_name, "==> Status:Book is available")
            else:
                print(search_book_name, "==> Status:Book is not available")

            # Additional options to display library or search more books.
            usr_show_library = input(selection2).strip().lower()
            if usr_show_library == "1":
                line_format()
            elif usr_show_library == "2":
                while True:
                    usr_selection3 = input(bookN).strip().lower()
                    if usr_selection3 in library:
                        print(usr_selection3, "Book is available.")
                    else:
                        print("Book is not available.")

                    loop_var = input(selection2 + "any other keys to go back home").strip().lower()
                    if loop_var == "1":
                        line_format()
                    elif loop_var == "2":
                        print("Restarting the search...")
                        continue
                    else:
                        print("Going back to home.")
                        break

        elif usr_selection == "3":  # Remove Book
            usr_remove_book = input(bookN).strip().lower()
            # Remove the book if it exists in the library.
            if usr_remove_book in library:
                library.pop(usr_remove_book)
                print(">>>The book has been removed<<<")
            else:
                print(usr_remove_book, "does not exist.")

        elif usr_selection == "4":  # Display all books.
            line_format()

        elif usr_selection == "5":  # Exit Program
            print("Exiting program.")
            break

        else:
            print("Invalid command, please select an option from the list.")

# Start the library system.
start()
