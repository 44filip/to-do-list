from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title: str):
        task = Task(title)
        self.tasks.append(task)
        return print("201 - Created: Task added successfully")

    def remove(self, title: str):
        for task in self.tasks:
            if task.title.lower().strip() == title.lower().strip():
                # Iterate and create a new list from each task in self.tasks that doesn't match the title
                self.tasks = [task for task in self.tasks if task.title.lower().strip() != title.lower().strip()]
                return print("200 - OK: Task removed successfully")
        print("404 - Not Found: Task not found")

    def complete(self, title: str):
        for task in self.tasks:
            if task.title.lower().strip() == title.lower().strip():
                task.completed = True
                return print("200 - OK: Task marked as complete")
        print("404 - Not Found: Task not found")

    def displayTasks(self):
        for task in self.tasks:
            status = "Completed" if task.completed else "Not completed"
            print(f"{task.title} - {status}")
        return

    def checkContent(self):
        if self.tasks:
            return True
        return print("204 - No Content: No tasks in list")
        
    def saveToFile(self, filename='tasks.txt'):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.completed}\n")
        print(f"200 - OK: Tasks saved to {filename}")

    def loadFromFile(self, filename='tasks.txt'):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    title, completed_str = line.strip().split(',')
                    completed = (completed_str.lower() == 'true')
                    task = Task(title)
                    task.completed = completed
                    self.tasks.append(task)
            print(f"200 - OK: Tasks loaded from {filename}")
        except FileNotFoundError:
            print(f"404 - Not Found: File {filename} not found. No tasks loaded.")