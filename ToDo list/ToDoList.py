def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append({"task": task, "done": False})

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{idx}. {task['task']} - {status}")
def mark_task_as_done(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["done"] = True
        print(f"Task '{tasks[task_num]['task']}' marked as done!")
    else:
        print("Invalid task number!")

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

