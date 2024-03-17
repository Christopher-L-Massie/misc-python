import string
import secrets


def generate_secure_password(length, exclude_chars=""):
    # Create a combined character set
    characters = string.ascii_letters + string.digits + string.punctuation
    # Remove any excluded characters from the character set
    for char in exclude_chars:
        characters = characters.replace(char, "")
    # Securely select random characters from the modified set
    password = "".join(secrets.choice(characters) for i in range(length))
    return password


# Specify characters to exclude and generate a secure password
exclude_chars = "0oO\"'"  # Add any characters you wish to exclude
password = generate_secure_password(12, exclude_chars)
print(password)
