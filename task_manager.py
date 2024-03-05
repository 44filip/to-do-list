from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add(self, title : str):
        task = Task(title)
        self.tasks.append(task)
        
    def remove(self, title : str):
        # Iterate and create a new list from each task in self.tasks that doesn't match the title
        self.tasks = [task for task in self.tasks if task.title != title]
        
    def complete(self, title : str):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                
    def displayTasks(self):
        for task in self.tasks:
            status = "Completed" if task.completed else "Not completed"
            print(f"{task.title} - {status}")