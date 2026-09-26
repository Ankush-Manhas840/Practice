class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0

        for i in range(len(s)):
            hashmap=dict()
            hashmap[s[i]]=hashmap.get(s[i],0)+1
            for j in range(i+1,len(s)):
                hashmap[s[j]]=hashmap.get(s[j],0)+1

                max_count=max(hashmap,key=hashmap.get)
                min_count=min(hashmap,key=hashmap.get)
                sum+=(hashmap.get(max_count)-hashmap.get(min_count))
        return sum
