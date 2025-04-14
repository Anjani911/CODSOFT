import random
import string

def generate_password(length, letters=True, numbers=True, special=True):
    characters = ""
    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if special:
        characters += string.punctuation

    if not characters:
        return "Error!: No character set selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter password length: "))
        letters = input("Include letters? (y/n): ").lower() == 'y'
        numbers = input("Include numbers? (y/n): ").lower() == 'y'
        special = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, letters, numbers, special)
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()

