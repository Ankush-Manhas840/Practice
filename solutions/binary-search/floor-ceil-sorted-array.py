arr=[3, 4, 4, 7, 8, 10]
target=2
low=0
high=len(arr)-1
while(low<=high):
  mid=(low+high)//2
  if(arr[mid]==target):
    low=mid
    high=mid
    break
  if(arr[mid]<target):
    low=mid+1
  elif(arr[mid]>target):
    high=mid-1
if high < 0:
  print(-1, arr[low])
elif low >= len(arr):
  print(arr[high], -1)
else:
  print(arr[high], arr[low])
