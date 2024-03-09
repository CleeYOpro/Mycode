#User function Template for python3
class Solution:

	def fascinating(self,n):
	    # code here
	    a= n*2
	    q = n*3
	    strr = str(n)+str(a)+str(q)
	    strr=''.join(sorted(strr))
	    if strr == '123456789':
	        return True
	    else:
	        return False
	    
#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        ob = Solution()
        ans = ob.fascinating(n)
        if ans:
            print("Fascinating")
        else:
            print("Not Fascinating")
        tc -= 1

# } Driver Code Ends