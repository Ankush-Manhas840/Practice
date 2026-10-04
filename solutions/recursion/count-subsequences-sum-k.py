def checker(i,sum,arr,k):
    if(i==len(arr)):
        return 1 if sum==k else 0
    if(sum>k):
        return 0

    return checker(i+1,sum,arr,k)+checker(i+1,sum+arr[i],arr,k)


class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):
        return checker(0,0,nums,k)
