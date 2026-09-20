class Solution:
    def minTime (self, arr, k):
        # code here
        low=max(arr)
        high=sum(arr)
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            result=[]
            total=arr[0]
            for i in range(1,len(arr)):
                if(total+arr[i]<=mid):
                    total+=arr[i]
                else:
                    result.append(total)
                    total=arr[i]
            result.append(total)

            if(len(result)<=k):
                ans=mid
                high=mid-1
            else:
                low=mid+1

        return ans
