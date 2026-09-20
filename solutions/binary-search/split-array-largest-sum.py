class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low=max(nums)
        high=sum(nums)
        ans=float("inf")
        while(low<=high):
            mid=(low+high)//2
            total=nums[0]
            result=[]
            for i in range(1,len(nums)):
                if(total+nums[i]<=mid):
                    total+=nums[i]
                else:
                    result.append(total)
                    total=nums[i]
            result.append(total)
            if(len(result)<=k):
                ans=max(result)
                high=mid-1
            else:
                low=mid+1


        return ans
