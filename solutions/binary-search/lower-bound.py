arr=[1,6,7,8,88]
x=5
result=len(arr)
low=0
high=len(arr)-1
while(low<=high):
  mid=(low+high)//2
  if arr[mid]>=x:
    result=mid
    high=mid-1

  else:
    low=mid+1


print(result)
