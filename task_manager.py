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
            return print(f"{task.title} - {status}")

    def checkContent(self):
        if self.tasks:
            return True
        return print("204 - No Content: No tasks in list")
        