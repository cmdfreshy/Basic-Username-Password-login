import time

def authenticate(max_attempts=3, username="admin", password="password123"):
    """
    Authenticate the user by prompting for a username and a password.
    
    Parameters:
        - max_attempts (int): the maximum number of attempts allowed to enter the correct credentials.
        - username (str): the correct username for authentication.
        - password (str): the correct password for authentication.
    
    Returns:
        - bool: True if authentication is successful, False otherwise.
    
    Raises:
        - ValueError: if max_attempts is not positive.
    """
    if max_attempts <= 0:
        raise ValueError("max_attempts must be positive.")

    for i in range(max_attempts):
        print(f"Attempt {i+1}/{max_attempts}")
        time.sleep(1)  # Pause for 1 second to simulate processing time
        username_input = input("Enter your username: ")
        time.sleep(1)  # Pause for 1 second to simulate processing time
        password_input = input("Enter your password: ")

        if username_input.lower() == username.lower() and password_input == password:
            print("Authenticating...")
            time.sleep(2)  # Pause for 2 seconds to simulate processing time
            print("Authentication successful!")
            return True

        print("Authenticating...")
        time.sleep(2)  # Pause for 2 seconds to simulate processing time
        print("Authentication failed. Please try again.")

    print("Maximum number of attempts reached.")
    return False

# Call the authenticate function to start the authentication process
is_authenticated = authenticate(max_attempts=3, username="admin", password="password123")

if is_authenticated:
    print("Access granted. Welcome!")
else:
    print("Access denied. Please contact an administrator.")
