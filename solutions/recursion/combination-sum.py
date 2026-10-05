class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]

        def checker(i,sum,curr):
            if(sum==target):
                result.append(curr)
                return

            if(i==len(candidates) or sum>target):
                return
            checker(i,sum+candidates[i],curr+[candidates[i]])
            checker(i+1,sum,curr)

        checker(0,0,[])

        return result
