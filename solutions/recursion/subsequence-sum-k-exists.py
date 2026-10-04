def checker(i,sum,arr,k):
    if(sum==k):
        return True 
    if(i==len(arr) or sum>k):
        return False
    return checker(i+1,sum,arr,k) or checker(i+1,sum+arr[i],arr,k)
    
        


class Solution:
    def checkSubsequenceSum(self, arr, k):
        # code here
        sum=0
        y=checker(0,sum,arr,k)
        return y
