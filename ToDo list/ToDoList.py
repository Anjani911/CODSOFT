def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            print("Viewing tasks...")
        elif choice == '2':
            print("Adding a task...")
        elif choice == '3':
            print("Marking a task as done...")
        elif choice == '4':
            print("Deleting a task...")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()

