import argparse
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added successfully.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks):
        status = "✔" if task["done"] else "✖"
        print(f"{index} - [{status}] {task['title']}")

def complete_task(index):
    tasks = load_tasks()
    try:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    except IndexError:
        print("Invalid task index.")

def remove_task(index):
    tasks = load_tasks()
    try:
        tasks.pop(index)
        save_tasks(tasks)
        print("Task removed.")
    except IndexError:
        print("Invalid task index.")

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    parser.add_argument("--add", help="Add a new task")
    parser.add_argument("--list", action="store_true", help="List tasks")
    parser.add_argument("--done", type=int, help="Mark task as completed")
    parser.add_argument("--remove", type=int, help="Remove a task")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.done is not None:
        complete_task(args.done)
    elif args.remove is not None:
        remove_task(args.remove)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()