import csv
import json
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(
            task_id=data["task_id"],
            title=data["title"],
            description=data["description"],
            due_date=data.get("due_date"),
            status=data["status"]
        )

class FileHandler:
    @staticmethod
    def save_to_file(filename, tasks, format="json"):
        if format == "json":
            with open(filename, "w") as file:
                json.dump([task.to_dict() for task in tasks], file)
        elif format == "csv":
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["task_id", "title", "description", "due_date", "status"])
                for task in tasks:
                    writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])
        else:
            raise ValueError("Unsupported file format.")

    @staticmethod
    def load_from_file(filename, format="json"):
        tasks = []
        if format == "json":
            with open(filename, "r") as file:
                data = json.load(file)
                tasks = [Task.from_dict(item) for item in data]
        elif format == "csv":
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    tasks.append(Task.from_dict(row))
        else:
            raise ValueError("Unsupported file format.")
        return tasks

class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_id, title, description, due_date=None, status="Pending"):
        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if due_date:
                    task.due_date = due_date
                if status:
                    task.status = status
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered_tasks:
            print("No tasks found with the specified status.")
            return
        print("Filtered Tasks:")
        for task in filtered_tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def save_tasks(self, filename, format="json"):
        FileHandler.save_to_file(filename, self.tasks, format)
        print("Tasks saved successfully!")

    def load_tasks(self, filename, format="json"):
        self.tasks = FileHandler.load_from_file(filename, format)
        print("Tasks loaded successfully!")

def main():
    app = ToDoApp()

    while True:
        print("\n--- To-Do Application ---")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                task_id = input("Enter Task ID: ")
                title = input("Enter Title: ")
                description = input("Enter Description: ")
                due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
                status = input("Enter Status (Pending/In Progress/Completed): ") or "Pending"
                app.add_task(task_id, title, description, due_date, status)

            elif choice == "2":
                app.view_tasks()

            elif choice == "3":
                task_id = input("Enter Task ID: ")
                title = input("Enter new Title (leave blank to keep unchanged): ") or None
                description = input("Enter new Description (leave blank to keep unchanged): ") or None
                due_date = input("Enter new Due Date (YYYY-MM-DD, leave blank to keep unchanged): ") or None
                status = input("Enter new Status (leave blank to keep unchanged): ") or None
                app.update_task(task_id, title, description, due_date, status)

            elif choice == "4":
                task_id = input("Enter Task ID to delete: ")
                app.delete_task(task_id)

            elif choice == "5":
                status = input("Enter Status to filter by (Pending/In Progress/Completed): ")
                app.filter_tasks(status)

            elif choice == "6":
                filename = input("Enter filename to save tasks: ")
                format = input("Enter format (json/csv): ")
                app.save_tasks(filename, format)

            elif choice == "7":
                filename = input("Enter filename to load tasks: ")
                format = input("Enter format (json/csv): ")
                app.load_tasks(filename, format)

            elif choice == "8":
                print("Exiting the application. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
