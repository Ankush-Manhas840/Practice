class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        integer=1
        s=s.lstrip()
        if(len(s)<1  ):
            return 0
        j=0
        i=0
        if(s[0]=='-'):
            integer=-1
            j=1
            i=1
        elif(s[0]=='+'):
            j=1
            i=1


        x=0
        while(i<len(s)):
            if('0'<=s[i] and s[i]<='9'):
                x=x*10+int(s[i])
                i+=1
            else:
                break
        if(j!=i):
            integer=integer*x
        elif(j==i):
            integer=0
        y=-2147483648
        z=2147483647
        if(integer<y):
            return y

        elif(integer>z):
            return z


        return integer
