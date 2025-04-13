def main():
    print("Password Generator")

if __name__ == "__main__":
    main()
    length = int(input("Enter password length: "))
    print(f"Length selected: {length}")
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
