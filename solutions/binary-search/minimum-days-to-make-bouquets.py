class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """

        low=1
        high=max(bloomDay)
        result=float("inf")
        total_flower=m*k
        if(total_flower>len(bloomDay)):
            return -1
        while(low<=high):
            mid=(low+high)//2
            boque=0
            streak=0
            for i in range(len(bloomDay)):
                if(bloomDay[i]<=mid):
                    streak+=1
                else:
                    streak=0
                if(streak==k):
                    boque+=1
                    streak=0

            if(boque>=m):
                result=min(result,mid)
                high=mid-1

            else:
                low=mid+1
        return result
