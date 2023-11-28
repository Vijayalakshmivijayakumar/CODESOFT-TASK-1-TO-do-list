class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the to-do list.')

    def display_tasks(self):
        if not self.tasks:
            print('Your to-do list is empty.')
        else:
            print('Your to-do list:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

    def update_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print(f'Task {index} updated to "{new_task}".')
        else:
            print('Invalid index.')

    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f'Task "{removed_task}" removed from the to-do list.')
        else:
            print('Invalid index.')

def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task\n2. Display Tasks\n3. Update Task\n4. Remove Task\n5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == '2':
            to_do_list.display_tasks()
        elif choice == '3':
            index = int(input("Enter the index of the task to update: "))
            new_task = input("Enter the new task: ")
            to_do_list.update_task(index, new_task)
        elif choice == '4':
            index = int(input("Enter the index of the task to remove: "))
            to_do_list.remove_task(index)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
