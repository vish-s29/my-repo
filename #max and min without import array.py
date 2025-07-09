#max and min without import array 
def max_min(list):
   # list=[]
    a=max(list)
    print("the maximum number from the given array is",a)
    b=min(list)
    print("the minimum number from the given array is",b)
    print(type(list))
max_min([1,2,3,4])

import array
x=array.array('i',[1,2,3,4])
a=max(x)
print(a)
b=min(x)
print(b)
print(type(x))

#array without import array
n=[1,2,3,4]
m=n[0]
for i in n:
     if i > m:
          m=i
print(m)

import array
n=array.array('i',[1,2,3,4])
m=n[0]
for i in n:
    if i>m:
         m=i
print(m)


def main():
    x=input("enter how many students marks do u want to calculate?")
    y=input


#student name enter ,student name ,marks,then output using array
def marks(x):
    #import array
    s=[]
    for i in x :
        i=i+1
        
        #s.append(a)
        #name=s
        
        s.append(b)
        d=s[0]
        m=max()
        return("the maximum marks scored is:",m,d)
    

n = int(input("Enter number of students: "))

names = []
marks = []


for i in range(n):
    name = input(f"Enter name of student #{i+1}: ")
    mark = int(input(f"Enter marks for {name}: "))
    names.append(name)
    marks.append(mark)

max_marks = max(marks)
top_index = marks.index(max_marks)
topper = names[top_index]


avg = sum(marks) / n

print("\n Results:")
print("Total students:", n)
print(f"Topper: {topper} with {max_marks} marks")
print("Average marks:", avg)

#to see
def marks(n):
    largest=n[0]
    smallest=n[0]
    
    for num in n:
        if num > largest:
            num = largest
        if num < smallest:
            num = smallest
    return largest,smallest

x=input("enter array")
    #y=input("enter students names and marks")
x=x.split(',')
x=[int(i)for i in x]
x=marks(x)
print(x)
##updated output
def my(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return ("the scores of the highest and lowest marks are:",maximum,minimum)


names = []
marks = []
z=int(input("Enter number of students: "))
for i in range(z):
        name = input(f"Enter name of student #{i+1}: ")
        mark = input(f"Enter marks for {name}: ")
        names.append(name)
        marks.append(mark)
x=my(marks)
print(x)

#how many numbers are there in the list
import array
n=array.array('i',[1,2,3,4])
numbers = print("the numbers that is present are",len(n))

contacts={}
s= input("enter the contact that u would like to delete")
if s in contacts:
     print(contacts.pop(s))
     print(f"deleted{s} in contacts")
else:
    print("cant delete")
    z=("the remaining contacts after deleting is:",contacts)
    print(z)
    print("do you want to delete all the contacts from the contact list?")
    print("1.yes or 2.no")
    d=input("choose the desired option")
              
if d=='1':
    contacts.clear()
    print("the remaining contacts after deleting is:",contacts)

elif d=='2':
     print ("not required")


 #to complete 
#view contacts
#restore contacts that is deleted 
#search contacts and identify them with suggestions
#create a gui for this
#can we create a program to rectify intendation error on its own rather than us doing it line by line??
def contact_list():
     print(" Hi! welcome! how can i help you?")
     print("1.show the current status of the list")
     print("2.create contacts")
     print("3.search for contacts")
     print("4.updating contacts")
     print("5.delete a particular contact")
     print("6.delete the entire contact list")
     print("7.view contacts")
     print("8.exit")
     c=input("pls select from the given options")

     try:
       if c=='1':
              print(status())
       elif c=='2':
               print(create())
       elif c=='3':
              print(search())
       elif c=='4':
              print(update())
       elif c=='5':
              print(delete())
       elif c=='6':
              print(clear())
       elif c=='7':
              print(view())
       elif c=='8':
              print(exit())
       #elif c=='9':
            #print(restore())
     
     except ValueError:##why is this not working??
          print("enter a valid number:")
     except TypeError:
         print("pls enter a number:")
contacts = {}
              
def status():
    #contacts = {}
    return("currently no contacts exist",contacts)

def create():
    #contacts = {}
    print("to create contacts:")
    n = int(input("How many contacts do you want to create? "))
    for i in range(n):
        name = input(f"Enter name for contact {i+1}: ")
        phone = input(f"Enter phone number for {name}: ")
        contacts[name] = phone
        
        if len(phone)==10:                
                print("the name and contact number is:",contacts)
                            
        else:
            print("invalid! pls enter a 10 digit number")

            break
        
        print("Saved Contacts:")         
        for name, number in contacts.items():
             print(f"{name}: {number}")

def search():
    while True:
        y=input("\n Enter name to search : ").strip()
        if y in contacts:
            return(f"found {y} -> {contacts[y]}")
            #break
        else:
               return("contacts not found")
        
def update():##to change this also accordingly
    while True:
               print("do u want to add this contact?")
               print("1.yes, 2.no")
               choose = input("enter option")
               if choose=='1':
                  n = int(input("How many contacts do you want to save? "))
                  for i in range(n):
                     name = input(f"Enter name for contact {i+1}: ")
                     phone = input(f"Enter phone number for {name}: ")
                     contacts[name] = phone
                     if len(phone)==10:
                       print("the name and contact number is:",contacts)
                     else:
                       print("invalid! pls enter a 10 digit number")
                       #break
                     
                       print("updated Contacts are:")
                  for name, number in contacts.items():
                      return(f"{name}: {number}")
                      #break
               elif choose =='2':
                      break
def delete():
               print("Saved Contacts:")
               #for name, number in contacts.items():
                 #  print(f"{name}: {number}")
               print("contacts that exist are:",contacts)  ## how to enter a value from the saved contacts to here??
               s= input("enter the contact that u would like to delete")
               if s in contacts:
                print(contacts.pop(s))
                print(f"deleted{s} in contacts")
               else:
                print("cant delete")
                z=("the remaining contacts after deleting is:",contacts)
                print(z)

def clear():
                print("do you want to delete all the contacts from the contact list?")
                print("1.yes or 2.no")
                d=input("choose the desired option")
       
                if d=='1':
                  contacts.clear()
                  print("the remaining contacts after deleting is:",contacts)
                  
                elif d=='2':
                 print ("not required")
def view():
       print("saved contacts are:",contacts)
    
def exit():
       return("Thankyou! The stored contacts are in the contact list!")
contact_list()

