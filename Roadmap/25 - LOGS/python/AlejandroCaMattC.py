import logging

import time

"""Logging in Python"""

# Logging is a way to track events that happen when some software runs.

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

print("\n")

"""Exercise"""


class TaskManager:

    def __init__(self) -> None:
        self.tasks = {}

    def add_task(self, name: str, description: str):
        start_time = time.time()
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(
                f"Task '{name}' added with description: {description}")
        else:
            logging.warning(f"Task '{name}' already exists.")
        logging.debug(f"The total number of tasks is: {len(self.tasks)}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def delete_task(self, name: str):
        start_time = time.time()
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"Task '{name}' deleted.")
        else:
            logging.error(
                f"The Task '{name}' that you are trying to delete is not found.")
        logging.debug(f"The total number of tasks is: {len(self.tasks)}")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def list_tasks(self):
        start_time = time.time()
        if self.tasks:
            logging.info("Listing all tasks:")
            for name, description in self.tasks.items():
                print(f"Task: {name}, Description: {description}")
        else:
            logging.info("No tasks available.")
        end_time = time.time()
        self._print_time(start_time, end_time)

    def _print_time(self, start_time, end_time):
        logging.debug(f"Elapsed time: {end_time - start_time:.6f} seconds")


# Example usage
task_manager = TaskManager()
task_manager.add_task("Bread", "Buy 5 loaves of bread")
task_manager.add_task("Study", "Study Python")
task_manager.list_tasks()
task_manager.delete_task("Bread")
task_manager.list_tasks()
