class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        start=1
        count=0
        while(start>0):

            if(start not in arr):
                count+=1
            if(count==k):
                return start
            start+=1
