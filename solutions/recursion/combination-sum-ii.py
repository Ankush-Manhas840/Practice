class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]

        def checker(i,sum,curr):
            if(sum==target):
                if curr not in result:
                   result.append(curr)
                return

            if(i==len(candidates) or sum>target):
                return 

            j=i+1
            while(j<len(candidates)):
                if(candidates[j]!=candidates[i]):
                    break
                else:
                    j+=1

            j=j-i

            checker(i+j,sum,curr)
            checker(i+1,sum+candidates[i],curr+[candidates[i]])

        
        candidates.sort()
        checker(0,0,[])
        return result
