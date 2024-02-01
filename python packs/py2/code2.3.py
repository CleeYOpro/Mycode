#  <Cleofus Balaranjith>
#  <10/12/23>
#  AP Computer Science Principles, Period <4>
#2.3
#a

import random

luck = (random.randint(0, 1))#forgot abt random.choice
heads_tails = input('pick a side, Heads or Tails: ')
if luck == 0:
        if heads_tails == 'Heads':
                print('You win! Heads!')
        else:
                print('Bad luck! Tails')
else:
        if heads_tails== 'Tails':
                print('You win! Tails')
        else:
                print('Bad luck! Heads')


#b
rand_num = (random.randint(1, 5))
print(rand_num)
u1 = int(input('guess a number between 1-5: '))
if rand_num == u1:
        print('Well done')
else:
        if rand_num < u1:
                print('too high pick lower')
        else:
                print('too low pick higher')
        u2 = int(input('guess another number between 1-5: '))
        if rand_num == u2:
                print('Correct')
        else:
                print('You loose')
                print(' the number was', rand_num)

