# To-Do List Application with Enhanced Features

# A list to store tasks
tasks = []

def display_tasks():
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for i, (task, completed) in enumerate(tasks, start=1):
            status = "✔️" if completed else "❌"
            print(f"{i}. {task} [{status}]")

def add_task():
    """Add a new task."""
    task = input("Enter the task: ")
    tasks.append((task, False))  # False indicates the task is not completed
    print(f"Task '{task}' added.")

def mark_task_complete():
    """Mark a task as complete."""
    display_tasks()
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        tasks[task_num - 1] = (tasks[task_num - 1][0], True)
        print(f"Task {task_num} marked as complete.")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

def delete_task():
    """Delete a task."""
    display_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        deleted_task = tasks.pop(task_num - 1)
        print(f"Task '{deleted_task[0]}' deleted.")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

def save_tasks():
    """Save tasks to a file."""
    with open("tasks.txt", "w") as file:
        for task, completed in tasks:
            file.write(f"{task}|{completed}\n")
    print("Tasks saved to 'tasks.txt'.")

def load_tasks():
    """Load tasks from a file."""
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task, completed = line.strip().split("|")
                tasks.append((task, completed == "True"))
        print("Tasks loaded from 'tasks.txt'.")
    except FileNotFoundError:
        print("No saved tasks found.")

def main():
    """Main function to run the application."""
    load_tasks()
    while True:
        print("\nOptions:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save and Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()






    
