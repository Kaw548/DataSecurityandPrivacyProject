from auth import register_user, authenticate_user

# Test the user registration and authentication
if __name__ == "__main__":
    # Register a new user
    username = input("Enter username to register: ")
    password = input("Enter password: ")
    register_user(username, password)

    # Authenticate the user
    username = input("Enter username to login: ")
    password = input("Enter password: ")
    authenticate_user(username, password)
