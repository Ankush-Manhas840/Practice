arr=[4, 5, 6, 7, 0, 1, 2]
low=0
target=88
high=len(arr)-1
flag=True
while(low<=high):

  mid=(low+high)//2
  if arr[low]<=target<=arr[mid]:
     if(arr[mid]==target ):
      print(mid)
      flag=False
      break

     elif (arr[mid]>arr[low] ):
        high=mid-1

     elif(arr[mid]>target):
      high=mid-1
     elif(arr[mid]<target):
      low=mid+1

  else:
    if(arr[mid]==target):
      print(mid)
      flag=False
      break

    elif(arr[mid]>arr[high]):
       low=mid+1

    elif(arr[mid]>target):
      high=mid-1
    elif(arr[mid]<target):
      low=mid+1

if flag:
  print("Not available")
