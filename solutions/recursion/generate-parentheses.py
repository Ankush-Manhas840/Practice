def bracket_maker(open,close,curr,n,result):
    if(open<n):

        bracket_maker(open+1,close,curr+'(',n,result)
    if(close<open):

        bracket_maker(open,close+1,curr+')',n,result)


    if(open==n and close==n):
        result.append(curr)
        return




class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        bracket_maker(0,0,"",n,result)

        return result
