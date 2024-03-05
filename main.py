from task import Task
from task_manager import TaskManager

task_manager = TaskManager()

task_manager.add("Create game")
task_manager.add("Draw art")
task_manager.complete("Draw art")
task_manager.add("Compose music")
task_manager.remove("Compose music")
task_manager.displayTasks()