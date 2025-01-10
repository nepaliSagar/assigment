# Project Overview
This project is a simple To-Do List application written in Python. It allows users to manage a list of tasks through a console-based menu interface. Users can add tasks, view them, delete specific tasks, clear the entire list, and exit the program. The application uses modular functions, making it easy to read, maintain, and enhance.

# Features
Add Task:
    Users can input a task to add to their to-do list.
    Confirmation is displayed after the task is added.
    
View Tasks:
    Displays all tasks in a numbered list format.
    Handles empty task lists gracefully with an appropriate message.

Delete Task:
    Lists all tasks with corresponding numbers for easy selection.
    Allows users to delete a task by entering its number.
    Provides error handling for invalid inputs and out-of-range selections.

Clear All Tasks:
    Clears the entire to-do list.
    Includes a confirmation prompt to prevent accidental deletion.
    
Exit Program:
    Cleanly exits the application.
    Displays a friendly thank-you message before quitting.


    
# Implementation Details
Modular Functions:
    Each feature is implemented as a separate function, improving readability and reusability.
    
Input Validation:
    Ensures only valid menu choices are accepted.
    Handles invalid or non-integer inputs with error messages.

Error Handling:
    Handles cases where the list is empty during task viewing or deletion.
    Includes safeguards for clearing tasks and deleting non-existent tasks.
    
User-Friendly Design:
    Task lists are displayed in an intuitive numbered format.
    Feedback is provided for every user action, making the program interactive and engaging.

# Technology Stack
   Language: Python
   Modules Used:
        sys: For clean program termination with sys.exit().
