import os

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append({"task": task, "done": False})  # Store task with a "done" flag

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

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        deleted_task = tasks.pop(task_num)
        print(f"Task '{deleted_task['task']}' has been deleted!")
    else:
        print("Invalid task number!")

def save_tasks_to_file(tasks, filename="tasks.txt"):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['done']}\n")

def load_tasks_from_file(filename="tasks.txt"):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                task, done = line.strip().split('|')
                tasks.append({"task": task, "done": done == 'True'})
    return tasks

def main():
    tasks = load_tasks_from_file()  # Load tasks when the app starts
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_as_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting...")
            save_tasks_to_file(tasks)  # Save tasks before exiting
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
