arr=[1,2,4,7]
target=2
low=0
high=len(arr)-1
while(low<=high):
  mid=(low+high)//2
  if(arr[mid]==target):
    low=mid
    break
  if(arr[mid]<target):
    low=mid+1
  elif(arr[mid]>target):
    high=mid-1


print(low)
