class Solution:
    def findKRotation(self, arr):
        # code here
        start=0
        end=len(arr)-1
        mini=float("inf")
        idx=-1
        while(start<=end):
            mid=(start+end)//2
            if(arr[mid]<mini):
                mini=arr[mid]
                idx=mid

            if(arr[start]<=arr[mid]):
                if(arr[start]<mini):
                    mini=arr[start]
                    idx=start
                start=mid+1
            else:
                end=mid-1



        return idx
