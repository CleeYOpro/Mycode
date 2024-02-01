#  <Cleofus Balaranjith>
#  <10/12/23>
#  AP Computer Science Principles, Period <4>
#Bonus 1
#This piece of code asks the user for an IP address, checks if it starts with "10." or "192.168.",
#and then prints a message based on whether it's a local IP address or not. 
user_ip = input("Give me an IP address: ")
if user_ip.startswith("10.") or user_ip.startswith("192.168."):
    print("Local IP address")
else:
    print("Not local IP")

