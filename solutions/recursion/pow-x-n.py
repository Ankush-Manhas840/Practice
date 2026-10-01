def checker(x,n):
    if(n==0):
        return 1
    if n < 0:
      return 1 / checker(x, -n)
    ans=checker(x,n//2)
    if(n%2==0):
        return ans*ans
    else:
        return ans*ans*x


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return checker(x,n)
