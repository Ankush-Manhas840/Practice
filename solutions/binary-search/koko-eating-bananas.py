class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low=1
        high=max(piles)
        total_time=h
        result=0

        while(low<=high):
            mid=(low+high)//2
            time_taken=0
            test=piles[:]

            for x in range(len(piles)):
               time_taken += piles[x] // mid
               if piles[x] % mid != 0:
                   time_taken += 1

            if(time_taken<=h):
                result=mid
                high=mid-1



            else:
                low=mid+1


        return result
