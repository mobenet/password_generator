import string
import secrets

def generate_secure_password(length, use_uppercase=True, use_numbers=True, use_symbols=True):
    if length<4:
        raise ValueError("Password length should be at least 4 characters to accommodate each character type")
    
    characters = string.ascii_lowercase
    password_chars = []

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Asegura que la contraseña tenga al menos un carácter de cada tipo requerido
    if use_uppercase:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_numbers:
        password_chars.append(secrets.choice(string.digits))
    if use_symbols:
        password_chars.append(secrets.choice(string.punctuation))

    while len(password_chars) < length:
        password_chars.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)

try:
    password_length = int(input("Enter the desired length for your password: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    password = generate_secure_password(password_length, use_uppercase, use_numbers, use_symbols)
    print(f"Your new password is: {password}")
except ValueError:
    print("Please enter a valid number for password length.")
except Exception as e:
    print(f"An error occurred: {e}")