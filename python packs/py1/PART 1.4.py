#<Cleofus Balaranjith>
#<9/29/2023>
#AP CSP, Period <4>

#1.4
print('#1.4')
print('\n')
#a)
drinkingwater1=('Accomplishing worldwide guarantee of safe drinking water, sanitation, and hygiene is crucial due to the growing problem of water scarcity, conflicts, and climate change. This goal the significant challenges posed by water pollution and bad sanitation globally. To achieve this, a 6-fold increase in global progress on drinking water, 5-fold increase in sanitation, and 8-fold increase in hygiene is needed.')
drinkingwater2=('One interesting piece of work being done here is the UN 2023 Climate confrence. It happened on March 22-24. They talk about how water is important in every aspect of life. Understanding water and managing it inclusively can lead to a more sustainable world.')
print(drinkingwater1,drinkingwater2)
print('\n')
#(b)
#1
char=len(drinkingwater1+drinkingwater2)
print('The length of the string is',char ,'characters.')
print('\n')
#2
print('The eighth character of the string is',drinkingwater1[7])
print('\n')
#3
print('The last character of the string is', drinkingwater2[-1])
print('\n')
#4
print('The first seven characters of the string are', drinkingwater1[:7])
print('\n')
#5
print('The last nine characters of the string are', drinkingwater2[-9:])
print('\n')
#6
print('The done string backwards is-->', (drinkingwater1+drinkingwater2)[::-1])
print('\n')
#7
print((drinkingwater1+drinkingwater2)[:(char-12)], 'is every character of the string except the last 12.')
print('\n')
#8
print((drinkingwater1+drinkingwater2)[::4], 'is every 4th chracter of the string')
print('\n')
#9
print((drinkingwater1+drinkingwater2)[20:-20], 'is every character of the string except the first 20 and the last 20 characters.')



