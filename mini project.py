import random 
def oddeven(n):
    if b%2==0:
        return "Even"
    else:
        return "Odd"

def positive(n):
    if n>0:
        return "Positive"
    if n==0:
        return "Zero"
    else:
        return "Negative"
def prime(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s=s+1
        else:
            s=s+0
    if s==2:
        return "Prime"
    else:
        return "Composite"
a=int(input("Enter the Starting of Range: "))
b=int(input("Enter the ending of Range: "))
n= random.randint(a,b+1)
print(n,"is a",oddeven(n),"number")
print(n,"is a",positive(n),"number")
print(n,"is a",prime(n),"number")
