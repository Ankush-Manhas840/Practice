class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        low=0
        high=max(arr)

        arr.sort()
        distance=float("-inf")
        while(low<=high):
            mid=(low+high)//2
            result=[]
            checker=arr[0]
            result.append(checker)
            for i in range(1,len(arr)):
                if(arr[i]-checker)>=mid:
                    checker=arr[i]
                    result.append(arr[i])



            if(len(result)>=k):
                distance=max(distance,mid)
                low=mid+1
            else:
                high=mid-1



        return distance
