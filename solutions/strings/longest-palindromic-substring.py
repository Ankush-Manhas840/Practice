class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lon=""
        for i in range(len(s)):

            mid=i
            left=mid-1
            right=mid+1

            while(left>-1 and right <len(s)):
                 if(s[left]==s[right]):
                     left-=1
                     right+=1
                 else:
                     break

            cand=s[left+1:right]
            if(len(lon)<len(cand)):
                lon=cand
            left=i
            right=i+1

            while(left>-1 and right <len(s) ):
                if(s[left]==s[right]):
                     left-=1
                     right+=1
                else:
                     break
            cand1=s[left+1:right]
            if(len(lon)<len(cand1)):
                lon=cand1


        return lon
