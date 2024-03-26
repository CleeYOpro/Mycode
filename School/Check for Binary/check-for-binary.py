# Return true if str is binary, else false
def isBinary(str):
    #code here
    bina = [1,0]
    for i in str:
        if int(i) not in bina:
            return 0
    return 1
#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        if isBinary(str):
            print (1)
        else:
            print (0)
# } Driver Code Ends