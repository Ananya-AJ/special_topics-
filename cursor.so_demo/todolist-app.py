class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task added: {task}')

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task deleted: {task}')
        else:
            print('Task not found.')

    def list_tasks(self):
        print('Your tasks:')
        for task in self.tasks:
            print(task)

if __name__ == "__main__":
    app = TodoApp()
    while True:
        print("\n1. Add task")
        print("2. Delete task")
        print("3. List tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter task: ")
            app.add_task(task)
        elif choice == '2':
            task = input("Enter task: ")
            app.delete_task(task)
        elif choice == '3':
            app.list_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")