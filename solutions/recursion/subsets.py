class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]

        def subber(i,nums,curr):
            if(i==len(nums)):
                result.append(curr)
                return

            subber(i+1,nums,curr)
            subber(i+1,nums,curr+[nums[i]])

        subber(0,nums,[])
        return result
