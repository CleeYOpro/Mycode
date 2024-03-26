
from typing import List


class Solution:
    def swapKth(self, n : int, k : int, arr : List[int]) -> None:
        # code here
        last = arr[-k]
        beg = arr[k-1]
        arr[k-1]=last
        arr[-k]=beg
        return arr



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        obj.swapKth(n, k, arr)
        IntArray().Print(arr)

# } Driver Code Ends