#User function Template for python3

class Solution:
    def IsPerfect(self,arr,n):
        a= 0
        b= n-1
        while a < b:
            
            if arr[b]!=arr[a]:
                return False
            a+=1
            b-=1
            
        return True
            
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    if(ob.IsPerfect(arr,n)):
        print("PERFECT")
    else:
        print("NOT PERFECT")
    
# } Driver Code Ends