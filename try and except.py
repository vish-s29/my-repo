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