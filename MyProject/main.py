from manager import TaskManager
from storage import load_tasks,save_tasks


def main():
    manager = TaskManager()
    tasks = load_tasks()
    manager.load_tasks(tasks)
    while True:
        print("\n1. Add task")
        print("2. Show tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter your task's title: ")
            description = input("Enter your task's description: ")
            if not title.strip() or not description.strip():
                print("cant be empty")
                continue
            manager.add_task(title, description)
            save_tasks(manager.show_tasks())
            print("Task added")
        elif choice == "2":
            tasks = manager.show_tasks()
            if not tasks:
                print("No tasks yet")
                continue
            for task in tasks:
                status = "done" if task.is_done else "not done"
                print(f"{task.id}. {task.title} [{status}]")
                print(f"   {task.description}")

        elif choice == "3":
            try:
                task_id = int(input("Enter your task's id: "))
            except ValueError:
                print("Id must be a number")
                continue
            if manager.complete_task(task_id):
                save_tasks(manager.show_tasks())
                print("Task completed")
            else:
                print("Task not found")

        elif choice == "4":
            try:
                task_id = int(input("Enter your task's id: "))
            except ValueError:
                print("Id must be a number")
                continue
            if manager.delete_task(task_id):
                save_tasks(manager.show_tasks())
                print("Task deleted")
            else:
                print("Task not found")

        elif choice == "5":
            break

if __name__ == "__main__":
    main()

