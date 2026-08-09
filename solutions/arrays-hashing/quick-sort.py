def partition(arr,left,right):
  piv=arr[left]
  start=left
  left+=1
  while(left<right):
    while(arr[left]<piv):
      left+=1
    while(arr[right]>piv):
      right-=1

    if left <right:
      temp=arr[left]
      arr[left]=arr[right]
      arr[right]=temp

  temp=arr[start]
  arr[start]=arr[right]
  arr[right]=temp
  return right


def quicksort(arr,left,right):
  if left>=right:
    return
  p=partition(arr,left,right)
  quicksort(arr,left,p-1)
  quicksort(arr,p+1,right)




partition([5,3,8,1,9,2], 0, 5)
quicksort([9, 9, 5, 3, 8, 1], 2, 5)
arr = [5,3,8,1,9,2]
quicksort(arr, 0, len(arr)-1)
print(arr)
