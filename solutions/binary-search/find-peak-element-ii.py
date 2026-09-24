class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        low=0
        high=len(mat[0])-1
        max=0
        while(low<=high):
            max1=0
            r=-1
            c=-1
            mid=(low+high)//2
            for i in range(len(mat)):
                if(mat[i][mid]>max1):
                    max1=mat[i][mid]
                    r=i
                    c=mid

            if(0<=c-1<len(mat[0]) and mat[r][c-1]>max1):
                high=mid-1
            elif(0<=c+1<len(mat[0]) and mat[r][c+1]>max1):
                low=mid+1
            else:
                return [r,c]
