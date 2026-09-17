class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        low=1
        high=max(nums)
        result=0
        while(low<=high):
            mid=(low+high)//2
            sum=0
            for i in nums:
                sum+=(i + mid - 1) // mid
            if(sum<=threshold):
                result=mid
                high=mid-1
            else:

                low=mid+1


        return result
