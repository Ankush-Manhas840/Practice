class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        result=0

        for ch in s:
            if ch=='(':
                count+=1


            elif ch==')':
                result=max(result,count)
                count-=1


        return result
