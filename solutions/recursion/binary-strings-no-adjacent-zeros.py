class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]

        def checker(curr):
            if(len(curr)==n):
                result.append(curr)
                return

            checker(curr+'1')
            if(curr=="" or curr[-1]=='1'):
                checker(curr+'0')
        checker("")
        return result
