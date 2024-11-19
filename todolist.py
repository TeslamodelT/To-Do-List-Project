def menu(): # Displays the main menu
    print("Welcome to your To Do List!")
    print("[1] Add Task")
    print("[2] View Tasks")
    print("[3] Delete Task")
    print("[4] Exit List")

def get_valid_input(prompt, valid_choices): 
    """
    Prompt the user for input and ensure it is one of the valid choices.
    """
    while True:
        choice = input(prompt)
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please select a valid option.")

def main(): # Asks the user to input one of the number options
    tasks = []
    while True:
        menu()
        try:
            choice = get_valid_input("Please choose an option (1-4): ", ["1", "2", "3", "4"])
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                delete_task(tasks)
            elif choice == "4":
                print("Exiting List")
                break
            else:
                raise ValueError("Invalid option.")
        except ValueError as e:
            print(e)
            

def add_task(tasks): # Asks the user to input a task
    task = input("Enter your task: ")
    tasks.append(task)
    print(f"Task {task} has been added.")
    
def view_tasks(tasks): # Displays current tasks or lack of them
    try:
        if not tasks:
            raise ValueError("No tasks available.")
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    except ValueError as e:
        print(e)
        
def delete_task(tasks):
    """
    Asks the user to delete a task by its number and removes it from the list.
    """
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if not(1 <= task_num <= len(tasks)):
                raise ValueError("Invalid task number.")
            removed_task = tasks.pop(task_num - 1)
            print(f"Task {removed_task} has been deleted.")
        except ValueError as e:
            print(e)
        except Exception as e:
            print("An unexpected arror occured:", e)
        finally:
            print("Delete operation attempted.")
            
if __name__ == "__main__": 
    main()