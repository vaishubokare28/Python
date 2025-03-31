# Create a To-Do List project in Python using loops and conditionals:
# list=[]
# Add Task Users can add tasks.
# View Tasks Displays all tasks.
#  Remove Task Deletes a task by its number.
#  Exit Option Ends the program.
# Loops (while True) Keeps the program running until the user exits.
# Lists (tasks[]) Stores tasks dynamically.
# Conditionals (if-elif-else) Handles user choices

tasks = []  # List to store tasks

while True:
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!\n")
    
    elif choice == "2":
        if not tasks:
            print("No tasks available.\n")
        else:
            print("Your To-Do List:")
            i = 1
            for task in tasks:
                print(f"{i}. {task}")
                i += 1
            print()
    
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.\n")
        else:
            i = 1
            for task in tasks:
                print(f"{i}. {task}")
                i += 1
            try:
                task_no = int(input("Enter the task number to remove: "))
                if 1 <= task_no <= len(tasks):
                    removed_task = tasks.pop(task_no - 1)
                    print(f"Removed task: {removed_task}\n")
                else:
                    print("Invalid task number.\n")
            except ValueError:
                print("Please enter a valid number.\n")
    
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.\n")
