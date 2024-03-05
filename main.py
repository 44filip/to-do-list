from task_manager import TaskManager
task_manager = TaskManager()

# task_manager.add("Create game")
# task_manager.add("draw art")
# task_manager.complete("DRAw art")
# task_manager.add("Compose music")
# task_manager.remove("compose music")
# task_manager.displayTasks()

def main():
    print("Welcome to PYTodo")
    while True:
        print("\n1. Add item to list\n2. Remove item from the list\n3. Mark item as completed\n4. Display all tasks\n5. Exit\n")
        res = input("Enter your choice: ")

        match res:
            case "1":
                add_input = input("Enter title of the task to be added: ")
                task_manager.add(add_input)
            case "2":
                if task_manager.checkContent():
                    remove_input = input("Enter title of the task to be removed: ")
                    task_manager.remove(remove_input)
            case "3":
                if task_manager.checkContent():
                    complete_input = input("Enter title of the task to be marked complete: ")
                    task_manager.complete(complete_input)
            case "4":
                if task_manager.checkContent():
                    task_manager.displayTasks()
            case "5":
                exit()
            case _:
                print("Invalid input.")
                
if __name__ == "__main__":
    main()