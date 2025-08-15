##prime numbers
def prime(n):
    if n<=1:
        return("is not a prime number")
    if n==2:
        return("is prime")
    for i in range(2,n):
        if n%i == 0 :              #logic 
            return ("is not prime")
        else:
            return("is prime")
x=prime(4)
print(x)

#fibonacci series  using for loop
def fib(n):
  fibseries = [0,1]                                    ## assingning what fibseries is
  for i in range(1,n-1):         
    fibseries.append(fibseries[-1]+fibseries[-2])      ##formula
  return fibseries
c=fib(5)
print(c)

#factorial using for loop 
def fact(n):
  i=0
  f=1
  for i in range(1,n+1):
        f=f*i
        i=n-1 
  return f
c=fact(3)
print("factorial OF","is",c) 
   

#factorial using while loop
def fact(n):
    f=1
    while n>0:
        f=f*n
        n=n-1
    return f
c=fact(4)
print(c)


def occurrence(mylist,value):
    count = 0
    for item in mylist:   ##[logic is important]
       if item == value:
           count +=1
    return count 

x = input("enter a list")
x=x.split(',')
x=[int(i) for i in x]
y = input("enter the value to check:")
valuetocheck=int(y)
count=occurrence(x,valuetocheck)
print(valuetocheck , "occurs ",count,"times")

# 1st program convert a list into tuple and pribnt the items in list and tuple
#x=[1,2,3,4]
#y = tuple(x)
#print(type(y))

# write factorial and def in tuples # to get this #u cant write it in tuples bcooz it is immutable first  to write in list and then convert it to tuples
# list to tuple and then factorial 
def fun(num):
    store=[]
    f=1
    for i in num:
        f=f*i
        i=i+1
        store.append(f)
    return(store)


x=input("enter a list")
x=x.split(',')
x = (int(i)for i in x)     
#print(fun(x))
print(tuple(fun(x)))
print(type(fun(x)))## why is it still showing list even after converting tuple


# count the numbers of times the values get entered in list (it shld count only those which gets repeated more than once)
def occurrence(mylist,value):
    count = 0
    for item in mylist:   ##[logic is important]
       if item == value:
           count +=1
    return count 

x = input("enter a list")
x=x.split(',')
x=[int(i) for i in x]
y = input("enter the value to check:")
valuetocheck=int(y)
count=occurrence(x,valuetocheck)
print(valuetocheck , "occurs ",count,"times")

def occurrence(mylist,value):
    count = 0
    for item in mylist:
        if item == value:
            count +=1
    return count
    
x=input("enter a sentence")
x=x.split(',')
x=[int(i) for i in x]
y = input("enter the value to check:")
valuetocheck=int(y)
count=occurrence(x,valuetocheck)
print(valuetocheck , "occurs ",count,"times")


# written by baba
def fact(n):
    store=[]
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            store.append(i)
        result = 1
        for num in store:
            result*= num
        return result
def main():
    numbers = input("enter numbers:")
    numbers = numbers.split(',')
    numbers = tuple(int(i)for i in numbers)
    c = type(numbers)
    print(c)
    for num in numbers:
        print(f"the factorial of {num} is {fact(num)}")

main()

##reverse factorial 
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
    a=(x[::-1])
    print(a)
    for num in a:
        y=fact(num)
        print(y)

main()

#Write a Python code to count the number of uppercase letters in a string
#to think over this   
def capslock(mylist,caps):
    count = 0
    for item in mylist:
        if item == caps:
            count +=1
    return count

y=capslock("heLLo","o")
print(y)

# count the numbers of times the values get entered in list (it shld count only those which gets repeated more than once)
def occurrence(mylist,value):
    count = 0
    for item in mylist:   ##[logic is important]
       if item == value:
           count +=1
    return count 

x = input("enter a list")
x=x.split(',')
x=[int(i) for i in x]
y = input("enter the value to check:")
valuetocheck=int(y)
count=occurrence(x,valuetocheck)
print(valuetocheck , "occurs ",count,"times")


##try it with dictionary 
dict={
    "key":"w",
    "value": 1
}
count = 0
for key,value in dict.items():
    if dict["key"] == value:
        count = count+1
    print(count) 

x= int(input("enter a number"))
y=x//100
store = x%100
z = store//10
a=x%10
print(a+z+y)

def sum_of_digits_string(number):
    return sum(int(digit) for digit in str(number))
z=sum_of_digits_string(23)
print(z)
##adding number of digits using while loop

#find even numbers in a list
lis  = [1,2,3,4]
for x in lis:
    if x%2 == 0:
        print("the even numbers are:",x)


n=[1,2,3,4]
store=[]
for i in n:
        store.append(i)
        print(store)

for j in range(0,n-1):
     if store[3]>store[2]:
       store[3],store[2] = store[2],store[3]
       print(i,j)

#Write a Python code to count the number of uppercase letters in a string
#to think over this   
def capslock(mylist,caps):
    count = 0
    for item in mylist:
        if item == caps:
            count +=1
    return count

y=capslock("heLLo","o")
print(y)

# count the numbers of times the values get entered in list (it shld count only those which gets repeated more than once)
def occurrence(mylist,value):
    count = 0
    for item in mylist:   ##[logic is important]
       if item == value:
           count +=1
    return count 

x = input("enter a list")
x=x.split(',')
x=[int(i) for i in x]
y = input("enter the value to check:")
valuetocheck=int(y)
count=occurrence(x,valuetocheck)
print(valuetocheck , "occurs ",count,"times")

##class
class dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

dog1 = dog("tommy","labrador")
dog2 = dog("parry","gs")

dog1.bark()


#Write a Python program to find the longest word in a sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("i m vishaka")) 


#Write a Python program to find the longest word in a sentence using class
class long:
    def __init__(self,sentence,word):
        self.sentence = sentence
        self.word = word
    def longest_word(sentence):
        words = sentence.split()
        return max(words, key=len)
    print(longest_word("i m suresh")) 

#Python program to print even length words in a string
def longest_word(sentence):
        words = sentence.split()
        for word in words:
             print(word)
             print(len(word))
             if len(word) %2 == 0:
               return (word)
print(longest_word("i m vish")) 

def longestword(sentence):
     words = sentence.split()
     print(words)
     print(len(words))
     if len(words)%2 == 0:
          return (words)
print(longestword("im vish"))
##to ask the difference between these 2 programs 


# count the numbers of times the values get entered in list (it shld count only those which gets repeated more than once)
##to ask baba how do i convert this into a class??
class dude:
    def __init__(self,mylist,value):
        self.mylist = mylist
        self.value = value
        
        def occurrence(mylist,value):
         count = 0
         for item in mylist:   ##[logic is important]
           if item == value:
             count +=1
         return count 

x = input("enter a list")
x=x.split(',')
x=[int(i) for i in x]
y = input("enter the value to check:")
valuetocheck=int(y)
count=(x,valuetocheck)
print(valuetocheck , "occurs ",count,"times")

##
class car:
    def __init__(self,company_name,model ,color,year,price):
        self.company_name = company_name
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def atr(self):
        print(f"the details of the car are:{self.company_name},{self.model},{self.price}")

carx = input("enter the company name: ")
cary = input("enter the model: ")
carz = input("enter the color: ")
card = input("enter the year: ")
care = input("enter the price: ")
        
cars = car(carx,cary,carz,card,care)

cars.atr()



#import array
#s = array.array('i',[])
# d= input("enter the number of tasks u want to add: ")
#d = [str(i) for i in s]
#s.append(d)
#print(s)
#integer= []
#d= input("enter the number of tasks u want to add: ")
#string = list(map(str, integer))
#string_list = [str(x) for x in integer_list]
#string.append(d)
#print(string)

import array
task=array.array('b',[])

d=input("pls choose from the given options:") 
if d == '1':
     c = int(input("enter the number of tasks u want to add: "))
     for i in range(c):
        b = i+1
        f = input(f"enter task for {b}: ")
        g = [str(x) for x in task]
        g.append(f)
        print (g)

##ascending order and descending order in list without sort method
n=[2,4,1,3]
for i in range(0,len(n)):
    for j in range(i,len(n)):
         
         if n[i] < n[j]:
             Temp = n[i]
             n[i]=n[j]
             n[j] = Temp
    #print(n[i])
         
n = [2,3,5,4]
c = len(n)
while i in c:
    i=0
    while j in c:
         j=0
    if n[i] < n[j]:
             Temp = n[i]
             n[i]=n[j]
             n[j] = Temp
             print(n[i])



import pywhatkit
import time

try:
    print("Opening WhatsApp Web...")
    pywhatkit.sendwhatmsg_instantly("+919072773868", "reached college! ✅", wait_time=10, tab_close=True)
    print("Waiting for message to send...")
    time.sleep(10)  
    print("✅ Message sent successfully!")
except Exception as e:
    print("❌ Error:", e)

##to ask baba
###how to send it to a grp 
###how to set the time?


while True:
             print("hello!\n what would u like to do?\n 1.add task\n 2.mark as done\n 3.delete task\n 4.view tasks\n 5.Exit")
             import array
             task=array.array('b',[])   ### will not work here bcoz it is integer and python doesnt support!!
             
             d=input("pls choose from the given options:") 
             if d == '1':

                c = int(input("enter the number of tasks u want to add: "))
                for i in range(c):
                          b = i+1
                          f = input(f"enter task for {b}: ")
                          g = [str(x) for x in task]
                          task.append(f)
                          print (g)
                        
             if d == '2':
                   c = input("which task do u want to mark as done?")
                   if c in g:
                        print( "this task is completed")
                        
             if d == '3':
                  s = input("which task do u want to delete?")

                  if s in g:
                       print(g.remove(s))
                       print(f"deleted{s} in list, the remaing tasks are:",g)

             if d == '4':
                         print("viewing the tasks")
                         print (g)
                       
             if d == '5':
                    print("thankyou!")
                    break


##array for contacts project
from array import array
def main():
    contacts_names = []                
    contacts_phone = array('i', [])    
    while True:
       print("Hello! what would u like to do?")
       print("1.add contacts")
       print("2.delete contacts")
       print("3.search contacts")
       print("4.update contacts")
       print("5.exit")

       c=input("pls enter ur choice")

       if c == '1':
           n = int(input("How many contacts do you want to add? "))
           for i in range(n):
              task = input(f"Enter task {len(contacts_names) + 1}: ")
              contacts_names.append(task)
              contacts_phone.append(len(contacts_names))
           print("contacts added.")

       if c=='2':
           

#Consider the text file, “Std.txt”, with the details of students like SRN,
# NAME, SEMESTER, SECTION AND AVG_MARKS. Read the file, “Std.txt”
# and display the details of all the students of 4th Semester “A” Section who
# have scored more than 75%. 

#A “CAR” has the attributes COMPANY_NAME, MODEL, COLOR,
#MANUFACUTING_YEAR and PRICE. A Class is required to be created for
#“CAR” to store the above attributes and perform the following
#operations:
#Get the details of “CAR” object from user and store into Array of objects ------->call the function in the method
#Display the details of “CAR” object based on “COMPANY”, “MODEL” and
# “PRICE”. 

####This is how the program has to be written and called @Vishaka.

###to ask baba to help me understand this code:
##using for loop
#n=[2,4,1,3]
#for i in range(0,len(n)):
   # for j in range(i,len(n)):
         
         #if n[i] < n[j]:
           #  Temp = n[i]
           #  n[i]=n[j]
           #  n[j] = Temp
    #print(n[i])

##using while loop
#a=input("enter a number")
#b=input("enter another number")
#while a>b:
   # print(a)
    #break

##how to write without hard coding?
a=[2,4,3,1]
i=a[0]
j=a[1]
k=a[2]
l=a[3]
while i<j:
    print(i,j)
    break
while k>i:
    print(i,k)
    break
while j>k:
    print(i,k,j)
    break
while l<i:
    print(l,i,k,j)
    break

def get_account_details(name,pin,bal):
        name = input("enter name of account holder")
        pin = int(input("enter pin num"))
        bal = float(input("enter balance amt"))
        accounts = account(name,pin,bal)
        return accounts
print("\nEnter user details")
account_holder = input("Enter account holder: ")
account_number = float(input("Enter account number: "))
balance = float(input("Enter balance: "))
get_account_details(account_holder,account_number,balance)
           

##account details
## based on the input: shld get stored and get the output:
class account:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def dis(self):
        print(f"acccount holder:{self.account_holder}, account number:{self.account_number},balance: {self.balance}")


from array import array

def main():
    accountdetails= []                
    Account= array('i', [])   
    num = int(input("Enter number of accounts to input: "))
    for i in range(num):
         print(f"\nEnter user details for account {i + 1}:")
         name = input("enter name of account holder: ")
         pin = int(input("enter pin num: "))
         bal = float(input("enter balance amt: "))
         accounts = account(name,pin,bal)
         accountdetails.append(accounts)
         #Account.append(len(accountdetails)) 
    return accountdetails
main()

class ss:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        #self.account_number = account_number
        #self.balance = balance

def name():
    name = input("enter name of account holder: ")
    accountt = ss(name)
    return accountt
class w:
    def __init__(self,account_number):
        self.account_number = account_number

def pin():
    pin = int(input("enter pin num: "))
    accounts = w(pin)
    return accounts
class j:
    def __init__(self,balance):
        self.balance = balance
def bal():
    bal = float(input("enter balance amt: "))
    accounts = j(bal)
    return accounts


  #program for lcm 
# Logic:
# Determine the larger of the two numbers.
# Start checking multiples of the larger number, incrementing until a number is found that is divisible by both input numbers.

   
def fun():
     a = int(input("enter num1:"))
     b = int(input("enter num2:"))
     c = max(a,b)
     d = min(a,b)
     for i in range(c,a*b+1 ,c):
        if i % d == 0:
         return i 

print(fun())

a = int(input("enter num1:"))
b = int(input("enter num2:"))
c = max(a,b)
d = min(a,b)
for i in range(c,a*b-1 ,c):
        if i % c == 0:
         print (i)
    
##to understand

#same program in while
a=[1,2,3,4]
j=a[0]
#k=a[1]
while i in a:
      j=i
      print(j)
      break
