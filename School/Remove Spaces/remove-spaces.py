#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        new = ''
        for i in s:
            if i == " ":
                pass
            else:
                new+=i
        return new
    #{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends