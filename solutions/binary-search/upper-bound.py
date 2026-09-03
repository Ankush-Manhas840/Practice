arr=[1,2,2,3]
x=2
result=len(arr)
low=0
high=len(arr)-1
while(low<=high):
  mid=(low+high)//2
  if arr[mid]>x:
    result=mid
    high=mid-1

  else:
    low=mid+1


print(result)
