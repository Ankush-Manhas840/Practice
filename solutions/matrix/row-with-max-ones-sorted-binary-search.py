class Solution:
    def rowWithMax1s(self, arr: list[list[int]]) -> int:
        # code here
        idx=-1
        count=-1
        for i in range(len(arr)):
            low=0
            high=len(arr[i])-1
            while(low<=high):
                mid=(low+high)//2
                if(arr[i][mid]==1):
                    if(count<(len(arr[0])-mid)):
                        idx=i
                        count=len(arr[0])-mid

                    high=mid-1
                else:
                    low=mid+1

        return idx
