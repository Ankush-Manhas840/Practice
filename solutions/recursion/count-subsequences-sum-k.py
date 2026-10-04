def checker(i,sum,arr,k):
    if(sum==k):
        
        return 1
    if(i==len(arr) or sum>k):
        return 0

   return checker(i+1,sum,arr,k)+checker(i+1,sum+arr[i],arr,k)
    


class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):
        #your code goes here
        return checker(0,0,arr,k)
