# To-Do List
import sys

def tasksAppend():
        task = input("Enter a task: ")
        task_list.append(task)
        print(f"You just added the task: {task}\n")
        
def taskView():
     if not task_list:
          print("The task list is empty.\n")
     else:
        print("Your tasks:")
        for i, task in enumerate(task_list, start=1):
            print(f"{i}: {task}")
        print()

def clearList():
    confirm = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
    if confirm == "yes":
        task_list.clear()
        print("All tasks have been removed.\n")
    else:
        print("Clear operation cancelled.\n")
    
def deleteTasks():
    if not task_list:
        print("The task list is empty, nothing to delete.\n")
    else:
        print("Your tasks:")
        for i, task in enumerate(task_list, start=1):
            print(f"{i}: {task}")
        
        try:
            selectToDelete = int(input("Enter the number of the task to delete: "))
            if 1 <= selectToDelete <= len(task_list):
                deleted_task = task_list.pop(selectToDelete - 1)
                print(f"Successfully deleted: {deleted_task}")
            else:
                print("Invalid selection. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

def exitProgram():
    print("Thank you for using the To-Do List program. Goodbye!")
    sys.exit()

task_list = []

while True:
    try:
        select = int(input("--Hello User--\n1: Add Task\n2: View Tasks\n3: Delete Task\n4: Clear All Tasks\n5: Quit\n=> "))
        if select < 1 or select > 5:
            print("Invalid selection. Please choose a number between 1 and 5.\n")
        elif select == 1:
            tasksAppend()
        elif select == 2:
            taskView()
        elif select == 3:
            deleteTasks()
        elif select == 4:
            clearList()
        elif select == 5:
            exitProgram()
    except ValueError:
        print("\nInvalid input. Please enter an integer between 1 and 5.\n")
