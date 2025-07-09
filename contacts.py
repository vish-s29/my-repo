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