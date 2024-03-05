from task import Task
from task_manager import TaskManager

task_manager = TaskManager()

task_manager.add("Create game")
task_manager.add("draw art")
task_manager.complete("DRAw art")
task_manager.add("Compose music")
task_manager.remove("compose music")
task_manager.displayTasks()