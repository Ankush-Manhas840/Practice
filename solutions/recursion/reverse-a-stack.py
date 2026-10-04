class Solution:
    def reverseStack(self, st):
        # code here
        sy=[]
        while(len(st)!=0):
            x=st.pop()
            sy.append(x)
            
        st.extend(sy)
           
        return sy
