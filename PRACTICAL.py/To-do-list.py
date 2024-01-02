# Project of TO DO LIST using oop's and basic concepts of python
class ToDoList:
    tasks = []  # creating a class variable to append tasks

    def show_menu(self): # Creating function to show menu of the list
        
        print('''
                1.Add tasks to list 
                2.View tasks
                3.Mark task as completed
                4.Exit

            ''')
    def add_task(self): # This function is used to add the tasks to the list
        task = input("\nEnter the task :==> ")
        self.tasks.append( {"Task":task, "completed":False} ) # Using dictionary we assign two values
        print("\nTask added successfully")                  # to the single input


    def view_task(self):
        if not self.tasks: # List is empty to avoid error we are passing if statement 
            print("No Tasks found")
        else:  
            for index, task in enumerate(self.tasks, start=1): # using enumerate function we can iterate two values at once
                status = "Completed" if task["completed"] else "Not Completed" #  initializing status to check task is finish or not
                print(f"{index}.{task} = {status}") # printing using format string within the loop
    
    def mark_completed(self):
        self.view_task() # calling the view function to view the tasks before adding

        try:
            task_index = int(input("\nEnter task number to mark as complete :==> "))- 1
            self.tasks[task_index]["completed"] = True
            print("Task is completed")
        except (ValueError, IndexError):
            print("\nInvalid Input. Please enter a valid number.")

check = ToDoList()
heading = "To Do List Application"

title = heading.center(80, ">")
print(title)
print("\nWelcome to the success people's secret")
print("\nStart best habits from NOW.")

while True: # using while can use the execute the code infinite times
    check.show_menu()
    choice = input("Enter your choice (1-4):==> ")

    match choice:
        case "1":
            check.add_task()
        
        case "2":
            check.view_task()
        
        case "3":
            check.mark_completed()
        
        case "4": # using lower() we can  solve the conflict with case sensitive
            restart = input("Are you want exit or continue. 'Yes or No': ").lower()
            if restart != "yes": # here we are checking the user input to loop the program
                print("Bye, See you next time.")
        
        case _:
            print("Invalid Choice.")

