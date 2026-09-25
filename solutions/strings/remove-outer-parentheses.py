class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        str=''
        counter=0
        for ch in s:
            if ch=="(":


                if(counter>=1):
                    str+='('
                counter+=1

            elif ch==")":
                if(counter>1):
                    str+=')'

                counter-=1

        return str
