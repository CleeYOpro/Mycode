#format{}
#default
'''
print("my name is {},my age is{}".format("sam",11))
#format using index
print("my name is {1},my age is{0}".format(11,"sam"))
#format using keyword
print("my name is {name},my age is{age}".format(age=11,name="sam"))


n=input("enter your name:")
a=eval(input("enter your age:")) 
print("My name is {name} and I am {age} years old".format(name=n,age=a))


#import
import math
print(dir(math))
print(math.sqrt(100))
print(math.pi*2)

#renaming a module
import math as m
print(m.sqrt(200))
#using from''''''

print(sqrt(300))
#importing particular function from the module
#from math import pi

import math

from math import *
print("sqare root anything!")
sq=eval(input("enter the number u want to take the square root from:"))

print(sqrt(sq))
'''
#decison making
#simple if
'''syntax:
if condition:
    stmt
n=int(input("Enter n number:"))
if n>0:
    print(n,"is a positive number")
print("end")




#if...else
syntax:
if condition:
    stmt
else:
    stmt
n=int(input("Enter n number:"))
if n>=0:
    print(n,"is a positive number")
else:
    print(n,"Negative number")
print("End")

#elif
n=int(input("Enter n number:"))
if n>0:
    print(n,"Positive Number")
elif n==0:
    print("Zero")
elif n==10:
    print("Ten")
elif n==5:
    print("Five")
    
else:
    print(n,"Negative number")
print("End")

#nested if
n=int(input("Enter n number:"))
if n>0:
    if n==5:
        print("Five")
    elif n==10:
        print("Ten")
    else:
        print(n,"positive Number")
else:
    print("Negative number")




a=float(input("enter ur age for voting:"))
if a>=18:
    print("Great! you can vote for the comming election")
else:
    print("Sorry but you cannot vote")'''

'''
s=float(input("Percent you got on the Exam:"))
if s>100:
    print ("Not a grade")

elif s==100:
    print ("Amazing you got Perfect score, A+")
elif s>=90:
    print("Wow U got an A!")
elif s>=85:
    print("Nice U got a B+")
elif s>=80:
    print("U got a B")
elif s>=75:
    print("U got a C+")
elif s>=70:
    print("U got a C")
elif s>=65:
    print("U got a C-")
elif s>=60:
    print("U got a D+")
elif s>=50:
    print("U got a D")
else:
    print("U failed")

n=int(input("Enter mark:"))
if n>=80 and n<=100:
    print("A Grade")
elif 
    
n=float(input("give any number greater than 0:"))

if n%2==0:
        print("even")
else:
    print("odd")


#looping statement
#while
n=50
while n<100:
    print("hello")
    n=n+2
else:
    print("inside Else")
print("Finished")


#for
for i in range(11):
    print("hai")
x="hai"
for i in range(50,100+1):
    print("*")

for i in range(10):
    a=float(input("enter ur age for voting:"))
    if a>=18:
        print("Great! you can vote for the comming election")
    else:
        print("Sorry but you cannot vote")
n=1
while n<10:
    a=float(input("enter ur age for voting:"))
    if a>=18:
        print("Great! you can vote for the comming election")
    else:
        print("Sorry but you cannot vote")
    n=n+5
print("Exited")
a=25
b=30
c=10

for i in {1,2,3,4,5,6,7}:
    if i==5:
        #break
        #continue
        pass
    print(i)
    
n="aeiouAEIOU"   
while True:
    a=input("enter a alphabet")
    if a in n:
        print("its a vowel")
        break
    print(a,"not a vowel,try again!")
   
#n=[1,2,2,4,556,2,4,6,2]

n=int(input("Enter no of elements:"))
n1=1
n2=2
print("the sum is",n1)
print("the sum is",n2)


for val in range(n):
    s=n1+n2
    print("the sum is", s)
     n1=n2
    n2=s

for val in "thcbniovwe":
    if val=="i":
        continue
    print(val)
'''

n=int(input("give a number: "))
if n>=0:
      print("positive")
else:
    print("negative")


