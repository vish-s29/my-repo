#adding contacts
contacts = {}
n = int(input("How many contacts do you want to save? "))

for i in range(n):
    name = input(f"Enter name for contact {i+1}: ")
    phone = input(f"Enter phone number for {name}: ")
    contacts[name] = phone

print("Saved Contacts:")
for name, number in contacts.items():
    print(f"{name}: {number}")

while True:
    y=input("\n Enter name to search : ").strip()
    if y in contacts:
     print(f"found {y} -> {contacts[y]}")
     break
    else:
     print("contacts not found")
     print("do u want to add this contact?")
     print("1.yes, 2.no")
     #print("2.no")
     choose = input("enter option")
    if choose=='1':
        n = int(input("How many contacts do you want to save? "))
        for i in range(n):
            name = input(f"Enter name for contact {i+1}: ")
            phone = input(f"Enter phone number for {name}: ")
            contacts[name] = phone
            print("Saved Contacts:")
            for name, number in contacts.items():
               print(f"{name}: {number}")
    elif choose =='2':
       break

    s= input("which contact would u like to delete?")
    
    


# say which contact would u like to delete then enter that contact and delete it 
# contacts not found do u want to add this contact if not exit 







 