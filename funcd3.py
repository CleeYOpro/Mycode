#function
'''syntax
def function_name():
    stmt
#no return type no argument
def add():
    a=10
    b=20
    print(a+b)



add()
add()
add()
add()
#argument with no return type
def sub(a,b):
    print(a-b)
x=int(input("Enter A:"))
y=int(input("Enter B:"))
sub(x,y)
sub(99,10)
    

#argument with return type
def mul(a,b):
    return a*b
print(mul(2,3)+100)



def sub(a,b):
    print(a-b)
    
s=sub(100,10)
print(s+3)


#no argument with return type
def div():
    #this function is used to divide two values
    a=int(input("Enter num1:"))
    b=int(input("Enter num2:"))
    return a/b
print(div()*200)
print(div.__doc__)

#scope and lifetime of variable
def demo():
    a=100
    print(a)
a=200
print(a)


name="sam"


def hello(name,age):
    print("My name is",name,"My age is",age)
a=input("Enter u r name:")
b=input("Enter u r  age:")
hello(a,b).

print("PYCALCULATOR")
def add(val1,val2):
    print("Equals to: ", val1+val2)
    #this function is used to add two values
def sub(val1,val2):
    print("Equals to: ", val1-val2)
    #this function is used to minus two values
def mult(val1,val2):
    print("Equals to: ", val1*val2)
    #this function is used to multiply two values
def div(val1,val2):
    print("Equals to: ", val1/val2)
    #this function is used to divide two values

x=int(input("enter your 1st value: "))
o=input("enter the operation you want to use: + - / *:  ")
y=int(input("enter your 2nd value: "))

if o=="+":
    add(x,y)
elif o=="-":
    sub(x,y)
elif o=="*":
    mult(x,y)
elif o=="/":
    div(x,y)
else:
    print("sorry but that is not an operation")

x=1
n=3

def patt():
    print(x, x+1, x+2)
for i in range(3):
    patt()


x='*'
n=3

def patt():
    print(n*x)
for i in range(n):
    patt()



n=2
x=1
def patt():
    print(x, x, x)
for i in range(n):
    patt()
    x=x+1


def patt(n):
    if n==0:
        return
    else:
        patt(n-1)
        print('*'*n)
n=3
patt(n)

n=int(input("enter number of rows:"))
for i in range(n+1,0,-1):
    for j in range(0,i-1):
        print("*")
    print()

for i in range(4):
    for j in range(i):
        print(i,end='')
    print()

#lambda function or anonymus function
a=lambda x,y,z:x*2+y+z
print(a(3,3,22))




#variab;e length argument
#1.Default argument


def show(a,b=1):
    print(a+b)
show(j,n)

#arbitary argument *

def demo(*name):
    for i in name:
        print("hello",i)
demo("sam","raj","ram")
    
#keyword argument
def display(name,age):
    print("my name is",name,"my age is ",age)
display(age=21,name="sam")


def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
num=4
print('The factorial value of given number', num, 'is', factorial(num))


def hi(*names):
    for name in names:
        print('hi', name)
hi('Peter', 'james', 'ram', 'vishnu')

#filter()
y=range(50)
x=tuple(filter(lambda a:(a%2!=0),y))
#map
p=range(40)
q=list(map(lambda a:(a*a),p))
print(q)
'''

n=eval(input("first number: "))
o=eval(input("second number: "))

if n>o:
    print(n, "is greater")
elif n<o:
    print(o, "is greater")
else:
    print("both are equal")


