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
    

