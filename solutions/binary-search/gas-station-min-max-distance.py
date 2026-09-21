import math
class Solution:
    def minMaxDist(self, stations, k):
        # Code here
        low=0
        high=max(stations)
        diff=[]
        ans=0
        for i in range(1,len(stations)):
            diff.append(stations[i]-stations[i-1])

        while(high-low)>0.000001:
            count=0
            mid=(low+high)/2.00
            for j in diff:
                peice=math.ceil(j/mid)
                count+=(peice-1)

            if(count<=k):
                ans=mid
                high=mid
            else:
                low=mid


        return ans
