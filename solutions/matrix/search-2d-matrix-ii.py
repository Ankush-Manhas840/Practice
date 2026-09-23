class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row=0
        col=len(matrix[0])-1
        while(row<len(matrix) and col>-1):
             if(matrix[row][col]==target):
               return True
             if(matrix[row][col]>target):
                 col-=1
             elif(matrix[row][col]<target):
                 row+=1


        else:
            return False
