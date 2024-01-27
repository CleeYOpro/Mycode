#<Cleofus Balaranjith>
#<9/29/2023>
#AP CSP, Period <4>

#1.3
#(a)
user_number = eval(input("Enter a # with lots of decimals: "))#ask for input
result = user_number * 5#multiply
product = round(result, 2)# Round the result
print('The product of multiplying', user_number, 'by 5 is', product)

#(b)
us_num1=eval(input('Give a number over 100 but less than 1000: '))

if 100 < us_num1 <1000: #to check if they gave correct numbers
        us_num2=eval(input('give number under 10: '))
        if us_num2 <10: # for second number
                ans = int(us_num1 / us_num2)
                print('The',us_num2,'goes into',us_num1,ans,'times')
        else:
                print('incorrect number. Try again')
else:
        print('incorrect number. Try again')

#(c)
firstname=input('Type your 1st name in lowercase: ')
lastname=input('Type your last name in uppercase: ')
fullname= (firstname + " " + lastname).title()
print('Your full name is', fullname)
