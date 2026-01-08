#Goal: create a to-do-list. let the user add, view, and delete tasks.
#learning outcomes:
#lists (adding/removing items)
#file handling(open/read/write)
#menu-driven programs (while loop with options)

#Challenge: save tasks in a .txt file so data isn't lost after closing.

#notes
#since it is a command line version of to-do-list, i think i will have to ask the user for input
#and check what mode they want (open, read, write) and when they want to add items, delete them, or view them (read).

# input() → to get user choices
# print() → to show menu & messages
# while loop → to keep the program running
# Lists → to store tasks
# Files (open, read, write) → to save tasks

import os
file_path = "to_do_list.txt"
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        tasks_list = lines
else:
    tasks_list = []
while True:
    try:
        #ask user for input
        choose_task = input("Kindly choose your desired option (add, view, delete), press Q to quit: ").lower()
        
        if choose_task == "add":
            add_task = input("add a task... \n")
            tasks_list.append(add_task)
            with open(file_path, 'w') as file:
                for task in tasks_list:
                    file.write(task + "\n")
            print("task was added!")

        elif choose_task == "view":
            if not tasks_list:
                print('No tasks yet')
            else:
                # for task in tasks_list:
                #     print(tasks_list)
                for i, task in enumerate(tasks_list, start=1):
                    print(f"{i}. {task}")
                #print the tasks, since they are going to be in a list ill have to loop through them
                # try readlines() with a for loop later
                #to deal with list, we must keep using tasks_list to add, remove and view from the list and not file!!

        elif choose_task == "delete":
            if not tasks_list:
                print('No tasks yet')
            else:
                # for task in tasks_list:
                #     print(tasks_list)
                for i, task in enumerate(tasks_list, start=1):
                    print(f"{i}. {task}")
                try:
                    task_deletion = int(input('Write the number of the task you want to delete: '))
                    #use chained comparison
                    if 1 <= task_deletion <= len(tasks_list):
                        removed_task = tasks_list.pop(task_deletion - 1)

                        with open(file_path, 'w') as file:
                            for task in tasks_list:
                                file.write(task + "\n")
                        print("Task deleted!")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("please enter a number")

        elif choose_task == "q":
            break
        else:
            print("Please enter the correct option.")
    #add this exception if x was used
    # except FileExistsError:
    #     print("This file already exists!")
    except FileNotFoundError:
        print("This file was not found")
    except PermissionError:
        print("You do not have permission to read this file")
