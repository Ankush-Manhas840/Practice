class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = max(weights)
        high = 0
        for i in weights:
            high += i
        result = float("inf")
        while low <= high:
            mid = (low + high) // 2
            sum = 0
            day_checker = 0
            for i in range(len(weights)):
                if sum + weights[i] <= mid:
                    sum += weights[i]
                elif sum + weights[i] > mid:
                    day_checker += 1
                    sum = 0
                    sum += weights[i]
            day_checker += 1

            if day_checker > days:
                low = mid + 1
            elif day_checker <= days:
                result = min(result, mid)
                high = mid - 1

        return result
