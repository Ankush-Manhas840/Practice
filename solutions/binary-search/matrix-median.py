import math
class Solution:
    def median(self, mat):
        # code here
        low = float("inf")
        high = float("-inf")
        for i in range(len(mat)):
            if mat[i][0] < low:
                low = mat[i][0]

            if mat[i][len(mat[0]) - 1] > high:
                high = mat[i][len(mat[0]) - 1]

        total_len = len(mat) * len(mat[0])
        mid_len = math.ceil(total_len / 2)


        while low <= high:
            mid = (low + high) // 2
            count = 0

            for i in range(len(mat)):
                l = 0
                h = len(mat[0]) - 1
                while l <= h:
                    m = (l + h) // 2
                    if mat[i][m] <= mid:

                        l = m + 1
                    elif (mat[i][m]>mid):
                          h = m - 1
                count+=l

            if count < (mid_len ):
                low=mid+1
            else:
                high=mid-1

        return low
