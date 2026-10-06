class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        def subber(i,nums,curr):
            if(i==len(nums)):
                if curr not in result:

                     result.append(curr)
                return

            j=i+1
            while(j<len(nums)):
              if(nums[j]!=nums[i]):
                    break
              else:
                    j+=1

            subber(j,nums,curr)
            subber(i+1,nums,curr+[nums[i]])

        nums.sort()

        subber(0,nums,[])
        return result
