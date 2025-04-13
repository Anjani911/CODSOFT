import random
import string


def main():
    print("Password Generator")

if __name__ == "__main__":
    main()
    length = int(input("Enter password length: "))
    print(f"Length selected: {length}")
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

def generate_password(length, use_letters, use_numbers, use_special):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected."

    return ''.join(random.choice(characters) for _ in range(length))

    password = generate_password(length, use_letters, use_numbers, use_special)
    print(f"\nGenerated Password: {password}")
