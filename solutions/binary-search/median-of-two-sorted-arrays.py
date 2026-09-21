class Solution:
    def medianOf2(self, a, b):
        # code here
        a_finger=0
        b_finger=0
        merge_length=len(a)+len(b)
        prev=-1
        curr=-1
        count=0
        numb=merge_length//2


        while(count<=numb):
            prev=curr

            if(a_finger>=len(a)):          # NEW: a has run out
                count+=1
                curr=b[b_finger]
                b_finger+=1
            elif(b_finger>=len(b)):        # NEW: b has run out
                count+=1
                curr=a[a_finger]
                a_finger+=1
            elif(a[a_finger]<b[b_finger]): # your old first `if`, now an `elif`
                count+=1
                curr=a[a_finger]
                a_finger+=1
            elif(a[a_finger]>b[b_finger]): # your existing branch
                count+=1
                curr=b[b_finger]
                b_finger+=1
            else:                          # equal: take ONE, not both
                count+=2

                curr=a[a_finger]
                prev=curr

                a_finger+=1
                b_finger+=1


        if(merge_length%2==0):
            return(prev+curr)/2
        else:
            return curr
