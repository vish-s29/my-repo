def calculator():
    print("welcome to calculator")

    try:
        x=float(input("enter number1:"))
        y=float(input("enter number2:"))
        print("check which operation:")
        print("1.add")
        print("2.division")
        choose = input("enter the desired operation")
        if choose == '1':
            print(x+y)
        elif choose == '2':
            print(x/y)
        else:
            print("invalid operation")
    except ValueError:
        print("enter an integer")
    except ZeroDivisionError:
        print("enter a non zero number in the denominator")
    finally:
        print("thankyou")

calculator()

#first convert into a flow chart wrt word use code
#2. except (both the errors)
#try cAatch is written in logic block usually or mostly----->functional block

#to try
#add contact: enter name  enter mobile no  the new contact added is SHAURAV  mobile no is:
#def contact():
try:
    x=input("enter name:")
    y=input("enter mobile no.")
    print("the new contact added is",x,y)

except ValueError:
    print("pls enter a 10digit number")
    
#contact()
    


# write a program that catches multiple errors using try and except to tell if zero is there
#to check why we get"none"
def zero(b):
    try:
        if '0' in b :
            print("the number consists of zero")
        else:
            print("the number doesnt have a zero")
    except ValueError:
       print('pls enter a positive number')
   

def main():
     n = input("enter a number")
     print(zero(n))
     
main()

#factorial and reversal
def fact(n):
    store=[]
    #print(store[::-1])
    f=1
    for i in range(1,n+1):
       store.append(i)
    for i in store:
        f=f*i
    return f 

def main():
    x=input("enter a list")
    x=x.split(",")
    x=[int(i)for i in x]
    print(x[::-1])
    for num in x:
        y=fact(num)
        print(y[::-1])

main()


#cube sum of n numbers(timetaken =1hour)
def cubesum(n):
     return sum(i ** 3 for i in range(1, n + 1))

def main():
     x=int(input("enter a number"))
     y=cubesum(x)
     print("sum of first n num",x,y)
main()

#using dictionaries 
x="hi hi there"
words=x.split()
#for i in x:
     #print("the words are",x)
dict = {}
for word in words:
     if word in dict:
         dict[word]=dict[word]+1
     else:
         dict[word] = 1

print(dict)

#using dictionaries for vowels
x="hi there"
vowels = "aeiou"

dict = {}

for char in x.lower():
     if char in vowels:
         if char in dict:
          dict[char]=dict[char]+1
     
         else:
          dict[char] = 1

print(dict)


#user input
x=input("enter a sentence:")
words=x.split()
#for i in x:
     #print("the words are",x)
dict = {}
for word in words:
     if word in dict:
         dict[word]=dict[word]+1
     else:
         dict[word] = 1

print(dict)


#Area of circle
#r=int(input("enter the radius"))
#area = 3.14 * (r**2) 
#print("area of the circle",area)

#Area of circle using functions
#def circle(r):
   
   # area = 3.14 * (r**2) 
    #return area

#def main():
    # r=int(input("enter the radius"))
    # y = circle(r)
    # print("area of the circle",y)
#main()

# cube roots for selected numbers using for loop
#num = int(input("enter a number"))
#n = int(input("enter a number"))
#b = n ** (1/3)
#for i in range(1,num+1):
   # num =  (i ** (1/3))
#print(num) 

# cube roots for selected numbers using for loop using functions
#def cube(n):
     #for i in range(1,n+1):
         # n =  n ** (1/3)
         # return n 
#def main():
    # x=int(input("enter a number"))
    # c=cube(x)
     #print(c)
#main()

#Area of triangle
#length = int(input("enter the length"))
#base = int(input("enter the base"))
#area = (1/2) * base * length
#print(area)

#Area of triangle using functions 
#def tri(a,b):
    #area = (1/2) * (a) * (b)
    #return area 

#def main():
    # length = int(input("enter the length"))
    # base = int(input("enter the base"))
    # c = tri(length,base)
    # print(c)
#main()


#squares of first 10 natural numbers
#i=0
#for i in range(1,11):
    #n=i**2
    #print(n)
    

# writing programs using functions
#factorial
#def fact(n):        
   # result = 1     
   # while n >0:         
        #result *= n      
       # n-=1              
       # n = n-1
   # return result         

#def main():
   # x=int(input("enter the number to find its factorial"))
   # y = fact(x)
   # print(y)
#main()

#simple interest
#def si(p,r,t):
    #y = (p*t*r)/100
    #return y

#def main():
   # q = int(input("enter a number 1:"))
    #s = int(input("enter a number 2:"))
    #z = int(input("enter a number 3:"))
    #interest = si(q,s,z)
    #print(f"SI is :{interest}")

#main()



#squares of first 10 natural numbers
#def sq():
    #i=0
    #for i in range(1,4):
        #n=i**2
    #return n
#c=sq()
#print(c)

#wap for finding simple interest using functions
#def si(p,t,r):
    #SI = (p*t*r)/100
   # return SI

#def main():
   # a=int(input("enter a number 1:"))
   # b=int(input("enter a number 2:"))
   # c=int(input("enter a number 3:"))
   # d=si(a,b,c)
   # print(d)
#main()

#def fact(n):
    #f=1
    #for i in range (1,n+1):
       # f=f*i
    #return f 

#def main():
    #x = int(input("enter the number to find its factorial"))
    #g = fact(x)
    #print(g)
#main()

#wap for finding sqrt for a particular range using functions
#def sqrt(n):
   # for i in range(n+1):
       # n = i**(1/2)
    #return n

#def main():
    #n=int(input("enter a number:"))
    #y=sqrt(n)
    #print(y)

#main()

# multiplication of tables using functions
#def mult(n):
    #d=""
    #for i in range (1,11):
        #d+=f"{n} * {i} = {n*i}\n"
    #return d

#def main():
   # x=int(input("enter a number"))
    #y=mult(x)
    #print(y)
#main()

#check pstive or ngtive
#def check(n):
    #if n>=0:
       # return ("n is positive")
    #else:
       # return("not positive")

#def main():
    #x=int(input("enter a number"))
    #y=check(x)
    #print(y)
#main()

#checking of even numbers with function
#def even(n):
   # if n%2==0:
       # return ("n is even")
    #else:
       # return ("n is odd")

#def main():
   # x = int(input("enter a number to check"))
   # y = even(x)
   # print(y)
#main()

#checking for largest number
#def large(a,b):
    #if a>b:
       # return ("it is greater")
   # else:
       # return("it is lesser")

#def main():
   # x = int(input("enter a number 1:"))
   # y = int(input("enter a number 2:"))
   # c = large(x,y)
   # print(c)
#main()

#finding area of rectangle using functions:


#cube sum of n numbers(timetaken =1hour)
def cubesum(n):
     return sum(i ** 3 for i in range(1, n + 1))

def main():
     x=int(input("enter a number"))
     y=cubesum(x)
     print("sum of first n num",x,y)
main()




#done by baba
#do the
numbers = {}
n = int(input("Please enter? "))

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = int(input(f"Enter value for key '{key}': "))
    numbers[key] = value

max_key = max(numbers, key=numbers.get)
max_value = numbers[max_key]

print(f"\nDictionary entered: {numbers}")
print(f"Max value is {max_value} for key '{max_key}'")



x=input("enter a sentence:")
words=x.split()
#for i in x:
     #print("the words are",x)
dict = {}
for word in words:
     if word in dict:
         dict[word]=dict[word]+1
     else:
         dict[word] = 1

print(dict)

#program for creating contact details via dictionary
try:
    dict={
       #"vishaka":"9901565503"
    }
    n=int(input("enter the number of contacts u want to add"))
    #key=dict[n]
    #value=dict[x]

    #for key,value in dict.items():
    for i in range(n):
        key=input("enter name:")
        value=input(f"enter the contact no.for '{key}':")
        dict[key]=value
    names = (dict)
  
    if len(value)==10:
             print("the name and contact number is:",names)
    else:
     #print("the name and contact number is:",key,value)
         
          print("invalid! pls enter a 10 digit number")
     

except ValueError:
    print("enter integers")

contacts = {}



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

s= input("enter the contact that u would like to delete")
if s in contacts:
   print(contacts.pop(s))
   print(f"deleted{s} in contacts")
else:
   print("cant delete")

#to complete 
#adding contacts
def add():
    for i in contacts:
        name = input(f"enter name{i+1}")
        phone = int(input(f"enter phone number for{name}"))
        contacts[name]=phone

        if len()

# say which contact would u like to delete then enter that contact and delete it 
# contacts not found do u want to add this contact if not exit 

names = []
marks = []
z=int(input("Enter number of students: "))
for i in range(z):
        name = input(f"Enter name of student #{i+1}: ")
        mark = int(input(f"Enter marks for {name}: "))
        names.append(name)
        marks.append(mark)

##programs advanced 
def integer(a,b,flag):
    if ((a) or (b) >0)and (flag==False):
        return True
    if ((a) and (b) < 0) and (flag==True):
        return True
    else:
        return False
def main():
    a=int(input("enter a "))
    b=int(input("enter b "))
    flag = bool(input("enter true or false:"))
    print(integer(a,b,flag))
main()

## to get this
def angry(john,smith):
     if ((john) or (smith)) == False:
        return False
     #if ((john) and (smith)) == False:
       # return True
     else:
        return True
        
def main():
    #j = input("is john angry?")
    #s = input("is smith angry?")
    j_angry = input("john is angry")
    s_angry = input("smith is angry")
    print(angry(j_angry,s_angry))
main()

def angry(j_angry , s_angry):
    if j_angry == 1 and s_angry == 1:
        return "in trouble"
    elif j_angry == 0 and s_angry == 0:
        return "In trouble"
    else :
        return "safe"
a=angry(1 ,0)
print(a)

def numbers(x):
    array = [0,x]
    for i in x:
        #array.append(i)
        if x<0 :
         print((array)+1)
        elif x > 0:
         print(array)
def main():
    n=input("enter a number ")
    print(numbers(n))
main()

def pos(n):
    n -= 1
    while n >= 0:
        print(n, end=" ")
        n -= 1

#print number in increasing order
def fun(x):
    #x=[1,3,2]
    x.sort()
    return(x)

def main():
    number=input("enter numbers")
    number=number.split(',')
    number=[int(i)for i in number]
    print(fun(number))
main()

def largest_smallest(n):
    largest=n[0]
    smallest=n[0]
    for num in n:
         if num>largest:
          largest = num
         if num<smallest:
            smallest=num
    return largest,smallest

def main():
   x=input("enter a list")
   x=x.split(',')
   x=largest_smallest(x)
   print(x)
main()

##logic building 29th june 
##if u want the user to enter a password and he keeps entering till the password is correct 
password = "123"
userinput = ""

while userinput != password:
    userinput = input("enter password")

print("successful")

#count numbers from 5 to 1
for i in range(5,0,-2):
    print(i)

    i = 5
while i > 0:
    
    i = i-1
    print(i)

#keep taking number from user until the user types 0 as soon as it types 0 print sum 
i = 0
n = int(input("enter a number "))
while n != 0:
    i = i + n 
    n = int(input("enter a number "))
print("the sum ",i)

def main():
    print("Hi! welcome")
    print("what would u like to do today?")
    print("1.check balance")
    print("2.withdraw amount")
    print("3.exit")
    c=int(input("enter from the above options: "))
    
    if c=='1':
        print(balance())
    #elif c=='2':
      #  print(withdrawal())
    #elif c=='3':
      #  print(ext())

##to check on this the 2nd option of the program
def main():
    print("Hi! welcome")
    print("what would u like to do today?")
    print("1.check balance")
    print("2.withdraw amount")
    print("3.exit")
    c=input("enter from the above options: ")
    
    if c=='1':
        print(balance())
    elif c=='2':
        print(withdrawal())
    elif c=='3':
        print(ext())

def balance():
    i = 500
    return "the balance in ur account is: ",i 

def withdrawal():
    while True:
         amount = int(input("enter amount to withdraw "))
         #if amount < balance():
            #return("insufficient")
         #for amount in :
         print(f"withdrawing {amount}")    
         break     

def ext():
    return("Thankyou for choosing us!")

main()


def main():
    print("Hi! welcome")
    print("what would u like to do today?")
    print("1.check balance")
    print("2.withdraw amount")
    print("3.deposit amt")
    print("4.exit")
    c=input("enter from the above options: ")
    
    if c=='1':
        print(balance())
    elif c=='2':
        print(withdrawal())
    elif c=='3':
        print(deposit())
    elif c=='4':
        print(ext())


def balance():
    i = 500
    return "the balance in ur account is: ",i 

def withdrawal():
    balance=500
    while True:
        amt = int(input("Enter amount to withdraw: "))
        if amt <= balance:
            balance -= amt
            return("Withdrawn:", amt)
            
        else:
            print("Insufficient balance!")

def deposit():
    balance=500
    while True:
        amt=int(input("enter amt to deposit"))
        balance=balance+amt
        return ("deposited:",amt)

def ext():
    return("Thankyou for choosing us!")

main()

## atm  done by baba
balance = 1000

while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        print("Current Balance:", balance)
    elif choice == '2':
        amt = int(input("Enter amount to deposit: "))
        balance += amt
        print("Deposited:", amt)
    elif choice == '3':
        amt = int(input("Enter amount to withdraw: "))
        if amt <= balance:
            balance -= amt
            print("Withdrawn:", amt)
        else:
            print("Insufficient balance!")
    elif choice == '4':
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid option!")

## a pattern of right angle
for i in range(1,6):
    i=i*'*'
    print(i)

#invert triangle 
for i in range(6,0,-1):
    i=i*'*'
    print(i)
##user input
n = int(input("how many lines do u want to enter?"))
for i in range(1,n):
    i=i*'*'
    print(i)

for i in range(1,6):
    i=i+1
    i=i*'*'
    print(i)

for i in range(1,6):
   # i=i+1
    i=i*' *'
    print(i)
for i in range(1,5):
    i=i*' *'
    print(i)

for i in range(5,0,-1):
    i=i*' *'
    print(i)

#pyramid pattern---->  to check this
## menu driven calculator using while loop
print("hi! welcome! \n what would u like to calculate?")
print("choose from the given options")
print("1.add")
print("2.sub")
print("3.multiply")
c=input("enter the option u would like to: ")
if c=='1':
    print(add())
#elif c=='2':
   # print(sub())
#elif c=='3':
    #print(mult())
#else:
   # print(divide())

n=int(input("enter num1: "))
b=int(input("enter num2: "))

def add():
    return i


print("\n📖 Student List:")
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())


##factorial using recurssion
def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_rec(n - 1)

a=factorial_rec(2)
print(a)

def factorial_rec(n):
    if n<0:
        return n * factorial_rec(n - 1)
a=factorial_rec(2)
print(a)

a= open("text.txt", "w")
print(a)

file = open("text.txt", "r")
content = file.read()
print(content)
file.close()


##simple automations
import os

username = os.getlogin()
file_path = f"C:/Users/{username}/Desktop/myfile.txt"

application
os.startfile(file_path)


#renaming multiple files
import os

folder = r"C:\\Users\\Admin\\Desktop\\TestFolder"
files = os.listdir(folder)

for i, filename in enumerate(files, start=1):
    if filename.endswith(".txt"):
        new_name = f"file{i}.txt"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

import 

##advanced scripting starts!!
#save student data to file
with open("marks.txt", "w") as file:
    while True:
        name = input("Enter student name (or 'stop' to finish): ")
        if name.lower() == 'stop':
            break
        marks = input(f"Enter marks for {name}: ")
        file.write(f"{name},{marks}\n")
print(" Data saved to marks.txt")

## atm  done by baba
balance = 1000

while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        print("Current Balance:", balance)
    elif choice == '2':
        amt = int(input("Enter amount to deposit: "))
        balance += amt
        print("Deposited:", amt)
    elif choice == '3':
        amt = int(input("Enter amount to withdraw: "))
        if amt <= balance:
            balance -= amt
            print("Withdrawn:", amt)
        else:
            print("Insufficient balance!")
    elif choice == '4':
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid option!")

#accepts numbers into a list, calculates factorial,computes lcm,herons formula for right angled triangle
def main():
    print("hi!\n what would u like to do?")
    print("1.accepts numbers into a list")
    print("2.calculates factorial")
    print("3.computes lcm")
    print("4.herons formula")
    print("5.exit")
    while True:
         c=input("enter from the above options")
         if c=='1':
              print(accept())
         elif c=='2':
             print(fact())
         elif c=='3':
             print(lcm())
         elif c=='4':
             print(herons())
         elif c=='5':
             print(ext())    
             break
def accept():
        x=input("enter a list")
        x=x.split(',')
        x=[int(i)for i in x]
        return("the list is",x)
     
def fact():
    x=int(input("enter a number from the list:"))
    f=1
    i=0
    for i in range(1,x+1):
         f=f*i
    return("factorial is:",f)
    
def lcm():##to check
     a=int(input("enter num1: "))
     b=int(input("enter num2: "))
     if a>b:
          return ("lcm of the two numbers",a)
     else:
          return("lcm is",b)
     
def herons():
     a=int(input("enter base: "))
     b = int(input("enter perpendicular"))
     c= ((a**2)+(b**2))**(0.5)
     #b= ((c**2)-(a**2))**(0.5)
    # a=((c**2)-(b**2))**(0.5)
     s=(a+b+c)/2
     e = (s*(s-a)*(s-b)*(s-c))**(0.5)
     return "the area of triangle is:",e,"and the other side is:",c
    

def ext():
     return ("thankyou!")
main()




#def lcm():
   #  a=int(input("enter num1: "))
  #   b=int(input("enter num2: "))

 #if change_pin()==True:
       # y=input("enter pin to go ahead!")
       # while y!=change_pin():
         #   y=input("pls enter correct pin")
         #   break
#else:
       # y = user['pin']
         
import array
num = array.array('i',[1,2,3,4])
target = 4
if num['i'] == target:
    print (num['i'])


list1 = [1,2,3,4]
target = 3
if list1[0] + list1[1] == target:
    print(list1[0],list1[1])


#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#compare two lists using store
x = input("enter list1 ")
x=x.split(',')
x=[int(i)for i in x]
y = input("enter list2 ")
y=y.split(',')
y=[int(i)for i in y]

store = []
lis=[]
for i in x:
    store.append(i)
    #print(store)
  
for t in y:
    lis.append(t)
    #print(lis)

if store[-1] == lis[-1]:
    print("its same")
else:
    print("its different")

list1 = [2,3,1,4]
target = 4
store=[]
for i in list1:
    if list1[] ==target:
        print(list1)

list1=[1,2,3,4]
store=[]
for i in list1:
    store.append(i)
    print(store)
   # j=i+1
for j in store:
    if store[3]>store[2]:
       store[3],store[2] = store[2],store[3]
       print(i)
      # c=j+1
for c in store:
    if store[2]>store[1]:
     store[2],store[1] = store[1],store[2]
     print(j)

list1 = [1,2,3,4]
store = []
for i in list1:
   store.append(i)
   print(store)
   j=i+1
for i in store:
   if store[i]>store[j]:
     print(store[i])
          

j=i+1
for j in store:
   if store[i]>store[j]:
    store[i],store[j] = store[j],store[i]
    print(store)

    
n=len(store)
for i in range(n):
   max1= i
   for j in range(n,i+1):
      if store[max1]>store[i+1]:
         store[max1],store[i+1] = store[i+1],store[max1]
         print(j,max1)


#max in dictionary
numbers = {}
n=int(input("enter the numbers:"))

for i in range(n):
    key = input(f"enter key{i+1}")
    value = int(input(f"enter the value for key'{key}': "))
    numbers[key] = value

max1 = max(numbers,key = numbers.get)
max2 = numbers[max1]

print(f"\ndictionary entered:{numbers}")
print(f"max value is {max1} for key {max2}")