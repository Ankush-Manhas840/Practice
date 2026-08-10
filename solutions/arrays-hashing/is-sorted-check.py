arr=[1,2,3,4,5,5]
flag=True
for i in range(len(arr)-1):
  if arr[i]>arr[i+1]:
    print("Not sorted")
    flag=False
    break
if flag:
  print("Sorted")
