# Simple To-Do List Program with Motivational Messages

FILE_NAME = "tasks.txt"

# Function to load tasks from the file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

# Function to save tasks to the file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to add a task
def add_task(task):
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added!")
    global task_added
    task_added = True  # Set flag when a task is added

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to remove a task
def remove_task(index):
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed}' removed!")
    except IndexError:
        print("Invalid task number!")

# Load existing tasks
tasks = load_tasks()
task_added = False  # Flag to check if user added any task

# Main menu
while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        task_num = int(input("Enter task number to remove: "))
        remove_task(task_num)
    elif choice == "4":
        if task_added:
            print("Have a productive day! ✅")
        else:
            print("Kuch toh productive krle! 😆")
        break
    else:
        print("Invalid choice! Try again.")
