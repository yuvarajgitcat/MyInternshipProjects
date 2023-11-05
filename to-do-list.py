import os
#Open the file if not exist 
if not os.path.exists("store"):
    open("store", 'w').close()

# Define a data structure to store tasks
tasks = []

# Define a data structure to store completed tasks
completed_tasks = []

# Function to load tasks from the "store" file
def load_tasks():
    if os.path.exists("store"):
        with open("store", 'r') as file:
            for line in file:
                task_data = line.strip().split(',')
                description = task_data[0]
                due_date = task_data[1] if task_data[1] else None
                priority = task_data[2] if task_data[2] else None
                completed = task_data[3] == 'True'

                if completed:
                    completed_tasks.append({"description": description, "due_date": due_date, "priority": priority})
                else:
                    tasks.append({"description": description, "due_date": due_date, "priority": priority})

# Function to save tasks to the "store" file
def save_tasks():
    with open("store", 'w') as file:
        for task in tasks:
            file.write(f"{task['description']},{task['due_date']},{task['priority']},False\n")
        for task in completed_tasks:
            file.write(f"{task['description']},{task['due_date']},{task['priority']},True\n")

load_tasks()

# Function to add a new task
def add_task():
    description = input("Enter task description: ")
    due_date = input("Enter task due date (optional): ")
    priority = input("Enter task priority (optional): ")

    task = {"description": description, "due_date": due_date, "priority": priority}
    tasks.append(task)
    print("Task added successfully!")

# Function to display the list of tasks
def display_tasks(task_list):
    if not task_list:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(task_list):
            print(f"{index + 1}. Description: {task['description']}")
            if task['due_date']:
                print(f"   Due Date: {task['due_date']}")
            if task['priority']:
                print(f"   Priority: {task['priority']}")
            print("")

# Function to mark a task as completed
def complete_task():
    display_tasks(tasks)
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        completed_task = tasks.pop(task_index)
        completed_tasks.append(completed_task)
        print("Task marked as completed and moved to the completed tasks list.")
    else:
        print("Invalid task number.")

# Function to update a task
def update_task():
    display_tasks(tasks)
    task_index = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_index < len(tasks):
        description = input("Enter new description (press Enter to keep the current one): ")
        due_date = input("Enter new due date (press Enter to keep the current one): ")
        priority = input("Enter new priority (press Enter to keep the current one): ")

        if description:
            tasks[task_index]["description"] = description
        if due_date:
            tasks[task_index]["due_date"] = due_date
        if priority:
            tasks[task_index]["priority"] = priority

        print("Task updated successfully.")
    else:
        print("Invalid task number.")

# Function to remove a task
def remove_task():
    display_tasks(tasks)
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print("Task removed from the to-do list.")
    else:
        print("Invalid task number.")

# Function for displaying completed tasks
def display_completed_tasks():
    if not completed_tasks :
        print("No tasks in the Completed Tasks list.")
    display_tasks(completed_tasks)

# Main loop for the application
while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Remove Task")
    print("6. Display Completed Tasks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        display_tasks(tasks)
    elif choice == "3":
        complete_task()
    elif choice == "4":
        update_task()
    elif choice == "5":
        remove_task()
    elif choice == "6":
        display_completed_tasks()
    elif choice == "7":
        save_tasks()
        break
    else:
        print("Invalid choice. Please select a valid option.")
