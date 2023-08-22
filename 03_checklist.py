tasks = []

while True:
    print("----- My first checklist -----")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Remove Task")
    print("4. Show")
    print("5. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        task = input("Insert your new task:")
        tasks.append(task)
        print("New task added successfully!")
    elif choice == 2:
        if not tasks:
            print("The checklist is empty.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            indice = int(input("What is the number of the task you want to edit? "))
            if 1 <= indice <= len(tasks):
                new_task = input("Write your new task description now: ")
                tasks[indice - 1] = new_task
                print("Task edited!")
            else:
                print("Number invalid.")
    elif choice == 3:
        if not tasks:
            print("The checklist is empty.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            indice = int(input("What is the number of the task you want to remove? "))
            if 1 <= indice <= len(tasks):
                tasks.pop(indice - 1)
                print("Task removed!")
            else:
                print("Number invalid.")
    elif choice == 4:
        if not tasks:
            print("The checklist is empty.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif choice == 5:
        if not tasks:
            print("Leaving the program.")
            break
        else:
            print("Invalid option. Choose again.")
