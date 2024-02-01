#<Cleofus Balaranjith>
#<9/29/2023>
#AP CSP, Period <4>

#1.5
'''
a = int(input("Enter an integer: "))#separate varables for each no.
b = int(input("Enter an integer: "))
c = int(input("Enter an integer: "))
d = int(input("Enter an integer: "))
e = int(input("Enter an integer: "))
f = int(input("Enter an integer: "))

mylist=[a,b,c,d,e,f]#list full of variable names given
'''
mylist=[1,12,7,6,325,4]
#a
print("Number of items in list are", len(mylist))
#b
print("The fifth item in the list is", mylist[4])
#c
print("The last three items in the list are", mylist[3:])
#d
print(mylist[3:], "Are all the items in the list except the first three.")
#e
mylist.sort(reverse=True)
print(mylist,"is the list in reverse order.")
mylist.sort(reverse=True)
#f
print("The sum of all the values in the list is", sum(mylist)) 
#g
if 0 in mylist:
        print("The first zero is at index", mylist.index(0))
else:
        print("There are no zeros in this list")
#h
del mylist[0]
print(mylist)
#i
mylist[3]=4301
print(mylist)
#j
mylist.append(-228)
print(mylist)
