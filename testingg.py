##when task is only working for one block take it out of the while loop!!!
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

             elif d == '2':
                  s = input("which task do u want to delete?")
                  print(task)
                  if s in task:
                       print(task.pop(s))
                       print(f"deleted{s} in list",task)

def fin():
      a = open("todo_log.txt","w")
      print(a)
      
      import os 
      username = os.getlogin()
      filepath = f"C:\\VISHAKA\\python folder vishaka\\todo_log.txt"
      os.startfile(filepath)

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

             elif d == '2':
                  s = input("which task do u want to delete?")
                  print(task)
                  if s in task:
                       print(task.pop(s))
                       print(f"deleted{s} in list",task)

             
fin()