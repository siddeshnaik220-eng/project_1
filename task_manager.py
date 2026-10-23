"""A command-line manager for students' academic tasks."""

import json
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Optional
from uuid import uuid4

PRIORITIES = ("Low", "Medium", "High")


@dataclass
class Task:
    """An academic task and its current completion status."""

    task_id: str
    title: str
    description: str
    due_date: str
    priority: str
    completed: bool = False


class TaskManager:
    """Create, retrieve, update, and delete tasks stored in a JSON file."""

    def __init__(self, storage_path="tasks.json"):
        self.storage_path = Path(storage_path)
        self._tasks = self._load_tasks()

    def _load_tasks(self):
        if not self.storage_path.exists():
            return []

        try:
            data = json.loads(self.storage_path.read_text(encoding="utf-8"))
            if not isinstance(data, list):
                raise ValueError("Task data must be a JSON list.")
            return [Task(**item) for item in data]
        except (json.JSONDecodeError, TypeError) as error:
            raise ValueError(f"Could not read task data: {error}") from error

    def _save_tasks(self):
        self.storage_path.write_text(
            json.dumps([asdict(task) for task in self._tasks], indent=2),
            encoding="utf-8",
        )

    @staticmethod
    def _validate(title, due_date, priority):
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        try:
            parsed_due_date = date.fromisoformat(due_date)
        except (TypeError, ValueError) as error:
            raise ValueError("Due date must be a valid date in YYYY-MM-DD format.") from error
        if parsed_due_date.isoformat() != due_date:
            raise ValueError("Due date must be a valid date in YYYY-MM-DD format.")
        if priority not in PRIORITIES:
            raise ValueError("Priority must be Low, Medium, or High.")

    def _find_task(self, task_id):
        for task in self._tasks:
            if task.task_id == task_id:
                return task
        raise KeyError(f"No task found with ID {task_id}.")

    def create_task(self, title, description, due_date, priority):
        self._validate(title, due_date, priority)
        task = Task(str(uuid4()), title.strip(), description.strip(), due_date, priority)
        self._tasks.append(task)
        self._save_tasks()
        return task

    def list_tasks(self):
        return list(self._tasks)

    def update_task(
        self,
        task_id,
        title: Optional[str] = None,
        description: Optional[str] = None,
        due_date: Optional[str] = None,
        priority: Optional[str] = None,
        completed: Optional[bool] = None,
    ):
        task = self._find_task(task_id)
        new_title = task.title if title is None else title
        new_due_date = task.due_date if due_date is None else due_date
        new_priority = task.priority if priority is None else priority
        self._validate(new_title, new_due_date, new_priority)

        if title is not None:
            task.title = title.strip()
        if description is not None:
            task.description = description.strip()
        if due_date is not None:
            task.due_date = due_date
        if priority is not None:
            task.priority = priority
        if completed is not None:
            task.completed = completed
        self._save_tasks()
        return task

    def delete_task(self, task_id):
        task = self._find_task(task_id)
        self._tasks.remove(task)
        self._save_tasks()
        return task


def _display_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        status = "Complete" if task.completed else "Pending"
        print(
            f"\nID: {task.task_id}\n"
            f"Title: {task.title}\n"
            f"Description: {task.description}\n"
            f"Due date: {task.due_date}\n"
            f"Priority: {task.priority}\n"
            f"Status: {status}"
        )


def main():
    try:
        manager = TaskManager()
    except (OSError, ValueError) as error:
        print(f"Unable to load tasks: {error}")
        return

    while True:
        print("\nAcademic Task Manager")
        print("1. Create task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                title = input("Title: ")
                description = input("Description: ")
                due_date = input("Due date (YYYY-MM-DD): ").strip()
                priority = input("Priority (Low, Medium, High): ").strip().capitalize()
                task = manager.create_task(title, description, due_date, priority)
                print(f"Created task {task.task_id}.")
            elif choice == "2":
                _display_tasks(manager.list_tasks())
            elif choice == "3":
                task_id = input("Task ID to update: ").strip()
                current = next(
                    (task for task in manager.list_tasks() if task.task_id == task_id),
                    None,
                )
                if current is None:
                    raise KeyError(f"No task found with ID {task_id}.")
                title = input(f"Title [{current.title}]: ")
                description = input(f"Description [{current.description}]: ")
                due_date = input(f"Due date [{current.due_date}]: ")
                priority = input(f"Priority [{current.priority}]: ")
                status = input(
                    f"Completion status (y/n) [{'y' if current.completed else 'n'}]: "
                ).strip().lower()
                if status and status not in ("y", "n"):
                    raise ValueError("Completion status must be y or n.")
                manager.update_task(
                    task_id,
                    title=title or None,
                    description=description or None,
                    due_date=due_date or None,
                    priority=priority.capitalize() if priority else None,
                    completed=(status == "y") if status else None,
                )
                print("Task updated.")
            elif choice == "4":
                task_id = input("Task ID to delete: ").strip()
                manager.delete_task(task_id)
                print("Task deleted.")
            elif choice == "5":
                break
            else:
                print("Choose a number from 1 to 5.")
        except (KeyError, ValueError, OSError) as error:
            print(f"Unable to complete that action: {error}")


if __name__ == "__main__":
    main()
