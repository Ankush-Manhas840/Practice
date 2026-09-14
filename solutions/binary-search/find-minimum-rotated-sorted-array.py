class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini=float("inf")
        start=0
        end=len(nums)-1
        while(start<=end):
            mid=(start+end)//2
            if(nums[mid]<mini):
                mini=nums[mid]
            if(nums[start]<=nums[mid]):
                mini=min(nums[start],mini)
                start=mid+1
            else:
                end=mid-1

        return mini
