from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title: str):
        task = Task(title)
        self.tasks.append(task)
        print("201 - Created: Task added successfully")

    def remove(self, title: str):
        for task in self.tasks:
            if task.title.lower().strip() == title.lower().strip():
                # Iterate and create a new list from each task in self.tasks that doesn't match the title
                self.tasks = [task for task in self.tasks if task.title.lower().strip() != title.lower().strip()]
                print("200 - OK: Task removed successfully")
                return
        print("404 - Not Found: Task not found")

    def complete(self, title: str):
        for task in self.tasks:
            if task.title.lower().strip() == title.lower().strip():
                task.completed = True
                print("200 - OK: Task marked as complete")
                return
        print("404 - Not Found: Task not found")

    def displayTasks(self):
        if self.tasks:
            for task in self.tasks:
                status = "Completed" if task.completed else "Not completed"
                return print(f"{task.title} - {status}")
        print("204 - No Content: No tasks to display")
