#menu driven: add contacts delete contacts search contacts and update contacts. shld continue running until the user chooses to exit 
#done improvements------> as a simulator!
def main():
    while True:
       print("Hello! what would u like to do?")
       print("1.add contacts")
       print("2.delete contacts")
       print("3.search contacts")
       print("4.update contacts")
       print("5.exit")
       c=input("pls enter ur choice")

       if c=='1':
        print(add())
       elif c=='2':
        print(delete())
       elif c=='3':
        print(search())
       elif c=='4':
         print(update())
       elif c=='5':
        print(ext())
        break


contacts = {}

def add():
    n = int(input("How many contacts do you want to add? "))
    
    for i in range(n):
        name = input(f"Enter name for contact {i+1}: ")
        phone = input(f"Enter phone number for {name}: ")
        contacts[name] = phone
        print("Saved Contacts:")
        for name, number in contacts.items():
            return(f"{name}: {number}")
            
def search():
    while True:
     y=input("\n Enter name to search : ").strip()
     if y in contacts:
      return(f"found {y} -> {contacts[y]}")
     break
def update():
    print("do u want to update this contact?")
    print("1.yes, 2.no")
    choose = input("enter option")
    if choose=='1':
        n = int(input("How many contacts do you want to save? "))
        for i in range(n):
            name = input(f"Enter name for contact {i+1}: ")
            phone = input(f"Enter phone number for {name}: ")
            contacts[name] = phone
            print("Saved Contacts:")
            for name, number in contacts.items():
               return(f"{name}: {number}")
    else:
       return("thanku!")

def delete():
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
     return(contacts.clear())
    
    elif d=='2':
      z=("the remaining contacts after deleting is:",contacts)
      return (z)
    
def ext():
   return ("Thankyou!")

main()