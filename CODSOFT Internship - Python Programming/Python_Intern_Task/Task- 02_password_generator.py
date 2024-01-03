import random
import string

def generate_password(length, include_symbols=True):
    """Generates a random password of specified length and complexity."""

    all_characters = string.ascii_letters + string.digits
    if include_symbols:
        all_characters += string.punctuation

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

while True:
    try:
        desired_length = int(input("Enter desired password length (minimum 8): "))
        if desired_length < 8:
            raise ValueError("Password length must be at least 8 characters.")

        include_symbols = input("Include symbols? (y/n): ").lower() == "y"

        password = generate_password(desired_length, include_symbols)
        print("Generated password:", password)

        break  # Exit the loop after successful password generation

    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

    try_again = input("Do you want to generate another password? (y/n): ")
    if try_again.lower() != "y":
        break
