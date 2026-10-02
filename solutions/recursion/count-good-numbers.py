class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        odd=n//2
        mod=10**9+7
        even=(n+1)//2
        ans=pow(5,even,mod)*pow(4,odd,mod)
        
        return ans%mod
