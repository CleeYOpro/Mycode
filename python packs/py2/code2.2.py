#  <Cleofus Balaranjith>
#  <10/12/23>
#  AP Computer Science Principles, Period <4>
#2.2
import random
friends = ['Demian','Brian','Dev','Soham','Prince']
print(friends)

for i in range(10):
      print(random.choice(friends))
#As shown in the code's output, you can print the same element multiple times using random.
#The chances are equal however when something is random, however, it doesn't always look like that.
#Python uses idexes of my list and picks a random index/number.
#This too isn't truly random because to generate the 'random' index, python must use an algorithm to generate a sequence of numbers
