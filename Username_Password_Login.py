def authenticate():
    # Predefined username and password
    correct_username = "admin"
    correct_password = "password123"

    for i in range(3):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == correct_username and password == correct_password:
            print("Authentication successful!")
            return

        print("Authentication failed. Please try again.")

    print("Maximum number of attempts reached.")

# Call the authenticate function to start the authentication process
authenticate()