import json
import bcrypt

# File to store user data
USER_DB_FILE = "users.json"


# Load users from JSON file
def load_users():
    try:
        with open(USER_DB_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# Save users to JSON file
def save_users(users):
    with open(USER_DB_FILE, "w") as file:
        json.dump(users, file, indent=4)


# Register a new user
def register_user(username, password):
    users = load_users()
    if username in users:
        print("User already exists. Try a different username.")
        return False

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = hashed_password.decode()
    save_users(users)
    print("Registration successful!")
    return True


# Authenticate a user
def authenticate_user(username, password):
    users = load_users()
    if username not in users:
        print("User not found.")
        return False

    hashed_password = users[username].encode()
    if bcrypt.checkpw(password.encode(), hashed_password):
        print("Authentication successful!")
        return True
    else:
        print("Invalid password.")
        return False


# Main function for user interaction
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            authenticate_user(username, password)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
