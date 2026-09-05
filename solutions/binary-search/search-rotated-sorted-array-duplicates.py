arr=[7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
low=0
high=len(arr)-1
target=8
flag=True
while(low<=high):
  mid=(low+high)//2
  if arr[mid] == target:
    # found
    print("True")
    flag=False
    break
  elif arr[low] <= arr[mid]:          # left half is sorted
    if arr[low] <= target <= arr[mid]:
        high = mid - 1
    else:
        low = mid + 1
  else:                                # right half is sorted
    if arr[mid] <= target <= arr[high]:
        low = mid + 1
    else:
        high = mid - 1

if flag:
  print("False")
