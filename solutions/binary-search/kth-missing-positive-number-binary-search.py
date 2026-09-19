class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            check=arr[mid]-(mid+1)

            if(k>check):
                low=mid+1
            else:
                high=mid-1


        still_miss=arr[high]-(high+1)
        k-=still_miss
        return arr[high]+k
