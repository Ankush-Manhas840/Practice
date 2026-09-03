arr=[1,2,3,4,5,6]
low=0
high=len(arr)-1
target=5

while(low<high):
  mid=(low+high)//2
  if(arr[mid]==target):
    print(mid)
    break
  elif arr[mid]>target:
    high=mid-1
  else:
    low=mid+1
