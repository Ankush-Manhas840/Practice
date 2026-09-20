class Solution:
    def findPages(self, arr, k):
        # code here
        low=max(arr)
        high=sum(arr)
        ans=-1
        if(len(arr)<k):
            return ans

        while(low<=high):
            mid=(low+high)//2
            result=[]
            total=arr[0]
            for i in range(1,len(arr)):
                if(total+arr[i])<=mid:
                    total=total+arr[i]
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
