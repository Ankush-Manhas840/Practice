class Solution:
    def nthRoot(self, n, m):
       # code here
       low=0
       pre=-1
       high=m
       while(low<=high):
           mid=(low+high)//2
           val=mid**n
           if(val==m):
               pre=mid
               return pre

           if (val<m):
               low=mid+1
           else:
              high=mid-1



       return pre
