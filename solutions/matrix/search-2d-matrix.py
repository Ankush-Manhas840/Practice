class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        low=0
        high=len(matrix)-1
        while(low<=high):
            mid=(low+high)//2
            if(matrix[mid][0]>target):
                high=mid-1
            elif(matrix[mid][len(matrix[0])-1]<target):
                low=mid+1

            else:
                l=0
                h=len(matrix[0])-1
                while(l<=h):
                    m=(l+h)//2
                    if(matrix[mid][m]==target):
                        return True
                    if(matrix[mid][m]<target):
                        l=m+1
                    else:
                        h=m-1
                return False
        return False
