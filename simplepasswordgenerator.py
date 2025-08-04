import random
import string

def generate_password(length):
    # Define characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Ask user for the desired password length
try:
    length = int(input("Enter the password length: "))
    if length <= 0:
        print("Length should be a positive number.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
