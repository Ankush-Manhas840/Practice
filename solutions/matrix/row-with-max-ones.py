class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        idx=-1
        count=-1
        for i in range(len(mat)):
            count1=0
            for j in range(len(mat[0])):
                if(mat[i][j]==1):
                    count1+=1
            if (count1>count):
                count=count1
                idx=i


        return[idx,count]
