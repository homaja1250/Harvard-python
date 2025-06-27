def add_task(tasks, task):
    tasks.append(task)
    return tasks

def remove_task(tasks, task_number):
    try:
        del tasks[task_number - 1]
        return tasks
    except IndexError:
        print("Invalid task number.")
        return tasks

def view_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def main():
    tasks = []
    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter a task: ")
            tasks = add_task(tasks, task)
        elif choice == "2":
            task_number = int(input("Enter the task number to remove: "))
            tasks = remove_task(tasks, task_number)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
