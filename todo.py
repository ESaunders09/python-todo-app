tasks = []
FILENAME = "tasks.txt"

# Load tasks from file
try:
    with open(FILENAME, "r") as the_file:
        for item in the_file:
            tasks.append(item.strip("\n"))
except FileNotFoundError:
    print("No saved tasks yet.")
    print()

# Repeat until user chooses to exit
while True:
    task_count = 1

    # Display menu with options
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")
    print()

    # Get user option
    user_option = input("Enter your choice: ")
    print()

    if user_option == "4":
        # Save tasks to file before exiting
        with open(FILENAME, "w") as the_file:
            for task in tasks:
                the_file.write(task + "\n")
        print()
        break

    elif user_option == "1":
        if len(tasks) > 0:
            print("Your tasks:")
            for task in tasks:
                print(f"{task_count}. {task}")
                task_count += 1
            print()
        else:
            print("No tasks yet!")
            print()

    elif user_option == "2":
        new_task = input("Please give a description of the task you want to add: ")
        print()
        tasks.append(new_task)
        if len(tasks) > 1:
            print(f"Task added! There are now {len(tasks)} tasks!")
        else:
            print(f"Task added! There is now {len(tasks)} task!")
        print()

    elif user_option == "3":
        try:
            remove_task = int(input("Please enter the number for the task you want to remove: "))
            print()
            if remove_task < 1 or remove_task > len(tasks):
                print("Invalid task number! Please choose another option.")
                print()
            else:
                del tasks[remove_task - 1]
                print("Task removed!")
                print()
                # Show updated task list
                task_count = 1
                if len(tasks) > 0:
                    print("Updated tasks:")
                    for task in tasks:
                        print(f"{task_count}. {task}")
                        task_count += 1
                    print()
                else:
                    print("No tasks left!")
                    print()
        except ValueError:
            print("Invalid input! Please enter a number.")
            print()

print("Goodbye! Your tasks have been saved!")