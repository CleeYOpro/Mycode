#User function Template for python3

class Solution:
    def countCamelCase (self,s):
        # your code here
        u=0
        for i in s:
            if i.isupper():
                u+=1
        return u


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print (ob.countCamelCase (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends