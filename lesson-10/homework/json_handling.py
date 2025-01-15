import json
import csv

def load_tasks(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_tasks(file_path, tasks):
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print("ID | Task Name         | Completed | Priority")
    print("---|------------------|-----------|---------")
    for task in tasks:
        print(f"{task['id']}  | {task['task']:<16} | {task['completed']}      | {task['priority']}")

def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks

    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

def convert_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

def main():
    json_file = "./python-homeworks/lesson-10/homework/tasks.json"
    csv_file = "./python-homeworks/lesson-10/homework/tasks.csv"

    tasks = load_tasks(json_file)

    print("Loaded Tasks:")
    display_tasks(tasks)

    calculate_stats(tasks)

    tasks[0]['completed'] = True  
    save_tasks(json_file, tasks)
    print("\nUpdated tasks have been saved to JSON.")

    convert_to_csv(json_file, csv_file)
    print(f"\nTasks have been converted to CSV and saved to {csv_file}.")

if __name__ == "__main__":
    main()
