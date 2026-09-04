idx=-1
arr=[3, 4, 13, 13, 13, 20, 40]
target=13
low=0
high=len(arr)-1
while(low<=high):
  mid=(low+high)//2
  if(arr[mid]==target):
    idx=max(idx,mid)
    low=mid+1
  if(arr[mid]<target):
    low=mid+1

  elif(arr[mid]>target):
    high=mid-1

print(idx)
