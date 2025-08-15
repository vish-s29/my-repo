##corrected code
from array import array

def main():
    task_names = []                
    task_ids = array('i', [])      
    while True:
        print("\nHello!\nWhat would you like to do?")
        print("1. Add task")
        print("2. Mark as done")
        print("3. Delete task")
        print("4. View tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            count = int(input("How many tasks do you want to add? "))
            for i in range(count):
                task = input(f"Enter task {len(task_names) + 1}: ")  ### for element by element
                task_names.append(task)
                #task_ids.append(len(task_names))  ##to check the inference of this line
            print("Tasks added.")

        elif choice == '2':
            task_to_mark = input("Enter task to mark as done: ")
            if task_to_mark in task_names:
                print(f"Task '{task_to_mark}' marked as completed.")
            else:
                print("Task not found.")    

        elif choice == '3':
            delete = input("which task do u want to delete? ")
            if delete in task_names:
                print(task_names.remove(delete))
                      # print(task_names.pop(delete))  ## dont use push and pop as its directly importing the array
                print(f"deleted {delete} in list, the remaing tasks are:",task_names)
            else:
                print("invalid")

        elif choice == '4':
            print("\n Current Tasks:")
            if task_names:
                for i in range(len(task_names)):
                    print(f"{task_ids[i]}. {task_names[i]}")
            else:
                print("No tasks available.")

        elif choice == '5':
            print("Thank you! Exiting.")
            break

        else:
            print("Invalid choice. Try again.")

main()