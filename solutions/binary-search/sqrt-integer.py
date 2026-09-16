class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low=0
        high=x
        prev=0
        while(low<=high):
            mid=(high+low)//2
            if( mid*mid<=x):
                prev=mid
                low=mid+1

            else:
                high=mid-1



        return prev
