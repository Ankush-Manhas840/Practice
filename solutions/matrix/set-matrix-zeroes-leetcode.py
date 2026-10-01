class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        work=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]==0):
                    #column work
                    work.append([i,j])


        for o in work:
            r=o[0]
            c=o[1]
            for k in range(len(matrix)):
                        matrix[k][c]=0
                    #row work
            for l in range(len(matrix[0])):
                        matrix[r][l]=0
