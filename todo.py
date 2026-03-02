tasks = []


# Repeat until user chooses to exit
while True:
    # Display menu with options
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")
    print()

    # Get user option
    user_option = input("")
    print()
    task_count = 1

    if user_option == "4":
        break

    elif user_option == "1":
        if len(tasks) > 0:
            for task in tasks:
                print(str(task_count) + "." , task)
            print()

        else:
            print("No tasks yet!")
            print()
    
    elif user_option == "2":
        new_task = input("Please give a description of the task you want to add: ")
        print()
        tasks.append(new_task)
        if len(tasks) > 1:
            print("Task added! There are now", str(len(tasks)), "tasks!")
            print()
        else:
            print("Task added! There is now", str(len(tasks)), "task!")
            print()