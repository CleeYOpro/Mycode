#  <Cleofus Balaranjith>
#  <10/12/23>
#  AP Computer Science Principles, Period <4> 
#2.1

import random
right_num = 0
wrong_num = 0
num1=(random.randint(1, 100))
num2=(random.randint(1, 100))
q1=int(input(f'What is {num1} * {num2}: '))
q2=int(input(f'What is {num2} - {num1}: '))
q3=int(input(f'What is {num1} + {num2}: '))
q4=int(input(f'What is {num1} / {num2}: '))
q5=int(input(f'What is the remainder of {num2} divided by {num1}: '))

if q1==num1*num2: 
       print('q1 right')
       right_num += 1
else:
       print('q1 wrong')
       wrong_num += 1
if q2==num2-num1:
    print('q2 right')
    right_num += 1
else:
       print('q2 wrong')
       wrong_num += 1
if q3==num1+num2:
    print('q3 right')
    right_num += 1
else:
       print('q3 wrong')
       wrong_num += 1
if q4==num1/num2:
    print('q4 right')
    right_num += 1
else:
       print('q4 wrong')
       wrong_num += 1
if q5==num2%num1:
    print('q5 right')
    right_num += 1
else:
       print('q5 wrong')
       wrong_num += 1
print('you got', right_num,' right and', wrong_num,' wrong')

