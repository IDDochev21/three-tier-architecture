import json

def load_users():
    try:
        with open('users.json', 'r') as file:
            users_data = json.load(file)
    except FileNotFoundError:
        users_data = {"users": []}
    return users_data['users']

def save_users(users):
    with open('users.json', 'w') as file:
        json.dump({"users": users}, file, indent=2)

def register(username, password, role='user'):
    users = load_users()
    for user in users:
        if user['username'] == username:
            print("Username already exists. Please choose a different one.")
            return False

    new_user = {"username": username, "password": password, "role": role}
    users.append(new_user)
    save_users(users)
    print("Registration successful!")
    return True

def authenticate(username, password):
    users = load_users()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user['role']
    return None

def main():
    print("Welcome to the Three-Layer Login Application!")

    while True:
        print("\nChoose an option:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            role = authenticate(username, password)

            if role:
                print(f"Login successful! You are logged in as a {role}.")
            else:
                print("Invalid username or password. Login failed.")

        elif choice == '2':
            username = input("Enter a new username: ")
            password = input("Enter a new password: ")
            if register(username, password):
                print("You can now log in with your new credentials.")

        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
