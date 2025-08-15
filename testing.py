#to get this right!!
#Use a main() function to:
# Show a menu (Add Task, Mark as Done, Delete Task, View Tasks, Exit).
# Use a fin() function to:
# Automatically save all tasks to a file (todo_log.txt) when the user exits the program.
# Save in the format: Task - Status
# Add basic error handling (e.g., invalid input, empty task name, index out of range).
# Handle user input and perform the corresponding action.
# Store tasks in memory as a list of dictionaries:

def main():
         task = {}
         while True:
             print("hello!\n what would u like to do?")
             print("1.add task")
             print("2.mark as done")
             print("3.delete task")
             print("4.view tasks")
             print("5.Exit")
             d=input("pls choose from the given options:")

             if d == '1':
                    c = int(input("enter the number of tasks u want to add: "))
                    for i in range(c):
                          b = str(input(f"enter task for {i+1}: "))
                          task[b] = i+1
                          print(task)
                         

             if d == '2':
                   c = input("which task do u want to mark as done?")
                   if c in task:
                        print( "this task is completed")
                        
             if d == '3':
                  s = input("which task do u want to delete?")
                  print(task)
                  if s in task:
                       print(task.pop(s))
                       print(f"deleted{s} in list, the remaing tasks are:",task)
             if d == '4':
                   print("viewing the tasks")
                   print (task)
             if d == '5':
                    print("thankyou!")
                    break
main()    
     

