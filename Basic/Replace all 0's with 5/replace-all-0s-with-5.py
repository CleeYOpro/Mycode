# Function should return an integer value
def convertFive(n):
    h=''
    for i in str(n):
        if i == '0':
            h+='5'
        else:
            h+=i
    return int(h)
        


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
# } Driver Code Ends