def val(stt):
        if stt=='I':
            return 1
        elif stt=='V':
            return 5
        elif stt=='X':
            return 10
        elif stt=='L':
            return 50
        elif stt=='C':
            return 100
        elif stt=='D':
            return 500
        elif stt=='M':
            return 1000
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=0
        result=0
        for ch in s:
            prev=x
            x=val(ch)
            if(prev<x):
                result=result-prev
            else:
                result+=prev

        result+=x
        return result
