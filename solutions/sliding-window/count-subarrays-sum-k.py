arr=[3, 1, 2, 4]
sum=0
k=6
i=0
count=0
j=0
while(j<len(arr) or sum>=k):
   if sum>k:
    sum-=arr[i]
    i+=1
   if sum==k:
    count+=1
    sum-=arr[i]
    i+=1

   if(sum<k and j<len(arr)):
     sum+=arr[j]
     j+=1







print(count)
