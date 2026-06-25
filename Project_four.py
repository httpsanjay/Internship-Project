import bcrypt
import os

FILE_NAME = "password.txt"


def register():
    password = input("Create a password: ")

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    with open(FILE_NAME, "wb") as f:
        f.write(hashed_password)

    print("Registration successful!")


def login():
    password = input("Enter password: ")

    with open(FILE_NAME, "rb") as f:
        stored_hash = f.read()

    if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
        print("Login successful!")
    else:
        print("Login failed!")


print("1. Register")
print("2. Login")

choice = input("Choose an option: ")

if choice == "1":
    register()

elif choice == "2":
    if not os.path.exists(FILE_NAME):
        print("No user registered yet. Please register first.")
    else:
        login()

else:
    print("Invalid choice")