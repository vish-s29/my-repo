#calculator test question
def main():
    print("hi welcome!\n What would u like to calculate")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    choose=input("enter from the given options")
    
    if choose=='1':
        print(addi())
    elif choose=='2':
        print(sub())
    elif choose=='3':
        print(mult())
    elif choose=='4':
        print(div())
    else:
        print(ext())
    
def addi():
    a=int(input("enter num1: "))
    b=int(input("enter num2: "))
    return("the addition of two numbers is",a+b)

def sub():
    a=int(input("enter num1: "))
    b=int(input("enter num2: "))
    return("the subtraction of two numbers is",a-b)

def mult():
    a=int(input("enter num1: "))
    b=int(input("enter num2: "))
    return("the multiplication of two numbers is",a*b)

def div():
    a=int(input("enter num1: "))
    b=int(input("enter num2: "))
    return("the division of two numbers is",a/b)

def ext():
    return("Thankyou!visit again!")

main()

# calculator 
def grp(a,b):
   choice = input("enter desired option")
   if choice== "1":
      return ("addition is",a+b)
   elif choice== "2":
      return ("subtraction is",a-b)
   elif choice=="3":
      return("multiplication is ",a*b)
   else:
      return ("avg is ",(a+b)/2)
#y=grp(2,3)
#print(y)


def main():
   a=int(input("enter number1 to calculate"))
   b=int(input("enter number2 to calculate"))
   #c=input("choose the desired operation  ")
   print("1.add")
   print("2.sub")
   print("3.multiplication")
   print("4.avg")
   d = grp(a,b)
   print(d)
main()
    

    def qe(a,b,c):
    #x=input("a*x**2+b*x+c")
    d = (b**2)-(4*a*c)
    roots1 = (-b+d**(1/2))/(2*a)
    roots2 = (-b-d**(1/2))/(2*a)
    return (roots1,roots2)
c=qe(1,5,6)
print(c)

#out of 1 to 20 count total number of 9s ## advanced so not required now
def fun(b,c):
   #i=0
   n=(b,c)
   for n in range(1,21):
      
      if c==9:
        print("total number of 9s=",n)
      else:
         print("none")

#for adding the digits with error handling
try:
    x = int(input("enter a number"))
    y=x//100                       
    print (y)                    
    store = x%100 
    print(store)                
    z=store//10                  
    print(z)
    a = x%10                      
    print(a)
    print(a+z+y)

except ValueError:
    print("invalid:plz enter an integer")

except 


#print("hello")

# calculator program 
# adding subtrcting multiplying nd div 
a=int(input("enter number1 to calculate"))
b=int(input("enter number2 to calculate"))
c=input("choose the desired operation  ")
if c== "add":
   print("addition is",a+b)
elif c== "sub":
    print("subtraction is",a-b)

#elif ("multiply"):
   # print("multiplying",a*b)

#else:
    #print("division is",a%b)
    for i in range(11):
        print(f" hello world,{x * i}")

    
def vish():

 x=int(input("enter a number"))
 def sub():
    if x>=0:
       print("x is positive")
    else:
       print("input is invalid")
       
sub()
vish()


def check(num1,num2):
    add=num1+num2
    return add
check(10,20)
print(check(10,20))

def click(num1,num2):
    if num1>num2:
        return "greater"
y=click(3,1)
print(y)

#for multiplying by defining the function and executing after the function
def click(num):
    c = ""
    for i in range(11):
        #c += f"{num} * {i} = {num * i}\n"
    #return c
       c += f"{num * i}\n"
    return(c)
    
y=click(2)
print(y)

#def check(num1,num2):
    #if num1>num2:
        #return "greater"
#y=check(1,2)
#print(y)

#wap to find the power of any number 
def power(a):
    c=a**2
    return c
d=power(4)
print(d)

#wap for finding sqrt
def sqrt(a):
    c = a ** (1/2)
    return c 
d=sqrt(9)
print(d)

#wap to find the prime number
def prime(a):
    if a == 1:
        return "neither prime nor comp"
    elif a % a == 1:
        return "prime"
    else:
        return "comp"
    
c=prime(5)
print(c)


#wap for finding sqrt
def sqrt(a):
    c = a ** (1/2)
    return c
sqrt(9)

#main block
#def main():
   # x = int(input("enter a number"))
    #b = sqrt(x)
    #print ("sqrt of number is",b)
#main()
# print= to print anything immdtly
# return = to store in function sqrt and use it anywhere else 

def sqrt():
    i = ""
    for i in range(11):
        i = 0
        i=i+1
    return i 
sqrt()
print()




#main block
#def main():
    #x = int(input("enter a number"))
    #b = sqrt({i})
    #print ("sqrt of number from 0 to 10 is",b)
#main()

#wap to write the roots of qe
e = pow((1*x**2 +2*x +4))
x=0
d = (2) ** (2) - (4 * 1 * 4)
roots1 = [-2 + d ** (1/2)]/  [1 * 2]
roots2 = [-2 - d ** (1/2)]/  [1 * 2]
print("the roots are :",roots1 , roots2)

#wap to write the roots of qe
x=""
e = ("a*x**2 +b*x +c")
a=("enter value 1")
b=("enter value 2")
c=("enter value 3")
d = "(b) ** (2) - (4 * a * c)"
roots1 = (-b + d ** (1/2))/  (a * 2)
#roots2 = (-b - d ** (1/2))/  (a * 2)
print("the roots are :",roots1)



#wap for finding simple interest 
p = int(input("enter a number 1"))
r = int(input("enter a number 2"))
t = int(input("enter a number 3"))
SI = (p*t*r)/100
print(SI)

#wap for cube root of number
a=int(input("enter a number"))
b = a ** (1/3)
print(b)

#wap to write the roots of qe
x=""
e = ("a*x**2 +b*x +c")
a=int(input("enter value 1"))
b=int(input("enter value 2"))
c=int(input("enter value 3"))
d = (b) ** (2) - (4 * a * c)
roots1 = int(input(-b + d ** (1/2))/  (a * 2))
roots2 = int(input(-b - d ** (1/2))/  (a * 2))
print("the roots are :",roots1 , roots2)

n=int(input("enter a number:"))
f=1
for i in range(1,n+1):
    f=f*i
    print(f)


    #wap to generate a random number
#x = int(input("enter a number"))
# wap to find factorial [tc]
#x=int(input("enter a number"))
#n=x
#y= (n*(n-1)*(n-2)*(n-3)) 
#y = []  
#for i in range(1,n+1):
   #n=n*1
   #if x==0:
       # print("fact is 1")
#else:
       # print("factorial is ",n)

#for i in range(10):
    #fact=fact*1

    #print("factorial is ")
#1+4+9+.....n**2

#wap for finding simple interest 
#p = int(input("enter a number 1"))
#r = int(input("enter a number 2"))
#t = int(input("enter a number 3"))
#SI = (p*t*r)/100
#print(SI)
    

def si(p,r,t):
    y = (p*t*r)/100
    return y

def main():
    q = int(input("enter a number 1:"))
    s = int(input("enter a number 2:"))
    z = int(input("enter a number 3:"))
    interest = si(p,r,t)
    print(f"SI is :{interest}")
    
main()


def fact(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    return f
y=fact()
print(y)

#write a program to find the roots of qe
def qe(a,b,c):
    x=""
    e = ("a*x**2 +b*x +c")
    d = (b) ** (2) - (4 * a * c)
    roots1 = qe((-b + d ** (1/2))/  (a * 2))
    roots2 = qe((-b - d** (1/2))/  (a * 2))

def main():
    g=int(input("enter value 1:"))
    h=int(input("enter value 2:"))
    j=int(input("enter value 3:"))

main()
#roots2 = int(input(-b - d ** (1/2))/  (a * 2))
#print("the roots are :",roots1 , roots2)


# calculator 
def grp(a,b):
   choice = input("enter desired option")
   if choice== "1":
      return ("addition is",a+b)
   elif choice== "2":
      return ("subtraction is",a-b)
   elif choice=="3":
      return("multiplication is ",a*b)
   else:
      return ("avg is ",(a+b)/2)
#y=grp(2,3)
#print(y)


def main():
   a=int(input("enter number1 to calculate"))
   b=int(input("enter number2 to calculate"))
   #c=input("choose the desired operation  ")
   print("1.add")
   print("2.sub")
   print("3.multiplication")
   print("4.avg")
   d = grp(a,b)
   print(d)
main()
    

#out of 5 students the student who got highest marks:
#a = input("enter a num1:")
#c= a.split()
#b=input("enter a num2:")
#d=b.split()
#c=input("Enter the marks3 and name3:")
#d=input("Enter the marks4 and name4:")
#e=input("Enter the marks5 and name5:")
#words= a.split()
dict={
    #"name1":"smitha",
    #"marks1":"30",
    #"name2":"chithra",
    #"marks2":"40",
    #"name3":"suchitha",
    #"marks3":"46"
}

for i in dict:
    if i in dict:
        c=dict[a]>dict[b]
        
    else:
        c=dict[b]>dict[a]

print(max(dict))


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
                z=("the remaining contacts after deleting is:",contacts)
                print(z)
                
        print("do you want to delete all the contacts from the contact list?")
        print("1.yes or 2.no")
        d= input("choose the desired option")
        if d=='1':
           print(contacts.clear(d))
        elif d=='2':
           print ("not required")


           contacts={}
print("do you want to delete all the contacts from the contact list?")
print("1.yes or 2.no")
d=input("choose the desired option")

if d=='1':
    print(contacts.clear())
    z=("the remaining contacts after deleting is:",contacts)
    print(z)

elif d=='2':
    print ("not required")
    


def max_min(list):
   # list=[]
    a=max(list)
    print("the maximum number from the given array is",a)
    b=min(list)
    print("the minimum number from the given array is",b)
    print(type(list))
max_min([1,2,3,4])

#print number in ascending and descending order
#in ascending order in list[tc]
#cube sum of n numbers
def cubdesum(n):
    return sum(i**3)for i in range(1,n+1))
        
