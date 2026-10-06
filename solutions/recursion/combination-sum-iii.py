class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]
        arr=[]
        for i in range(1,10):
            arr.append(i)
        def checker(i,sum,curr):

            if(len(curr)==k):
              if(sum==n):
                    result.append(curr)
              return
            if(i==len(arr)):
                return

            if(sum>n):
                return

            checker(i+1,sum,curr)
            checker(i+1,sum+arr[i],curr+[arr[i]])

        checker(0,0,[])
        return result
