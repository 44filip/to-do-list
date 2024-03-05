from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add(self, title : str):
        task = Task(title)
        self.tasks.append(task)
        print("200 - ADD OK")
        
    def remove(self, title : str):
        for task in self.tasks:
            if task.title.lower().strip() == title.lower().strip():
                # Iterate and create a new list from each task in self.tasks that doesn't match the title
                self.tasks = [task for task in self.tasks if task.title.lower().strip() != title.lower().strip()]
                return print("200 - REMOVE OK")
            print("400 - BAD REQUEST")
        
    def complete(self, title : str):
        for task in self.tasks:
            if task.title.lower().strip() == title.lower().strip():
                task.completed = True
                return print("200 - COMPLETE OK")
            print("400 - BAD REQUEST")
                
    def displayTasks(self):
        for task in self.tasks:
            status = "Completed" if task.completed else "Not completed"
            print(f"{task.title} - {status}")