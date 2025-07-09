def main():
   while True:
      print("choose the desired opration:")
      print("1.add")
      print("2. sub")
      print("3.multiply")
      print("4.divide")
      print("5.quit if you do not want to calculate")
      x=("choose from the above options!")
      if x=='1':
       print(addition())
      elif x == '2':
       print(subt())
      elif x == '3':
       print(mult())
      elif x== '4':
        print(div())
      elif x== '5':
        print(ext())
        break

a=int(input("enter number1:"))
b=int(input("enter number2:"))

def addition():
    if "1":
      return("addition is :",a+b)

def subt():
    if "2":
     return ("sub is:",a-b)

def mult():
    if "3":
     return("multiplication is:",a*b)

def div():
    if "4":
     return("division is:",a/b)

def ext():
   return ("thankyou!")
main()

# largest and smallest number--------------->to check this program
def largestandsmallest(n):
   
   store=[]
   largest=[0]
   smallest = [0]

   store.append()
   if n>largest:
      largest = n
   if n<smallest:
       smallest = n
   return largest,smallest
   
def main():
   x=input("enter a number")
   x=x.split(",")
   x=[int(i)for i in x]
   print(x)
main()


#parsing factorial for tuples 10numbers and their factorial
def fact(n):
   if n<0:
      return ("it is not defined")
   if n==0 :
      return("it is 1")
   
   store =[]

   f=1
   for i in range(1,n+1):
      store.append(i)
      f=f*i
      i=i+1
   return f

def main():
   x=input("enter a number")
   x=x.split(",")
   x=tuple(int(i)for i in x)
   for i in x:
      print("the factorial is",fact(i))
main()

def largestandsmallest(num):
   
   largest=num[0]
   smallest = num[0]

   
   for n in num:
      if n>largest:
         largest = n
         if n<smallest:
            smallest = n
   return largest,smallest
   
def main():
   x=input("enter a number")
   x=x.split(",")
   x=[int(i)for i in x]
   x=largestandsmallest(x)
   print(x)
main()