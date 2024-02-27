#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        if n == 1:
            lis=[1]
            return lis
        else:
            a = 1
            b = 1
            li=[]
            c=a+b
            li.append(a)
            li.append(b)
            for i in range(2,n):
                li.append(c)
                a=b
                b=c
                c=a+b
            return li

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends