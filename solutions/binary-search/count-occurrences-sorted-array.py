arr=[2, 2, 3, 3, 3, 3, 4]

target=3
low=0
high=len(arr)-1
bigIdx=0
smallIdx=float("inf")
#left search
while(low<=high):
  mid=(low+high)//2
  if(arr[mid]==target):
    high=mid-1
    smallIdx=min(smallIdx,mid)

  elif(arr[mid]<target):
    low=mid+1
  elif (arr[mid]>target):
    high=mid-1


low=0
high=len(arr)-1

while(low<=high):
  mid=(low+high)//2
  if(arr[mid]==target):
    low=mid+1
    bigIdx=max(bigIdx,mid)

  elif(arr[mid]<target):
    low=mid+1
  elif (arr[mid]>target):
    high=mid-1

if smallIdx==float("inf"):
  print("Not in the array")

else:
  occur=bigIdx-smallIdx+1
  print(occur)
