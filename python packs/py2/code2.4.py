#  <Cleofus Balaranjith>
#  <10/12/23>
#  AP Computer Science Principles, Period <4>
#2.4
def login():
        print('since you have a login')
        user = input('Enter the usename: ')
        if user in usernames:
                passw = input('Enter the password: ')
                index_of_pwd = usernames.index(user)
                if passw == passwords[index_of_pwd]:
                        print('LOGIN SUCESS')
                else:
                        print('Login unsuccessful')
        else:
                print('wrong username')

usernames = ['admin', 'guest', 'test', 'member']
passwords = ['W', '1234er', 'test1', 'member']

entering = int(input(' Enter 0 for new user or enter 1 for existing (0 or 1): '))
if entering == 0:
               new_user = input('Enter a new usename: ')
               usernames.append(new_user)
               new_pass = input('Enter a new password: ')
               passwords.append(new_pass)
               login()
        
else:
        login()
                        
