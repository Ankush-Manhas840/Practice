arr = [2, 3, 7, 11]
k = 11
sum=0
leng=0
left=0
right=0
while(right!=len(arr)):
  sum+=arr[right]
  while(sum>k):
    sum-=arr[left]
    left+=1

  if(sum==k):
    leng=max(leng,right-left+1)

  right+=1


print(leng)
