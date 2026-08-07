arr=[1,2,3,4,5,6]
flag=True
for x in range(len(arr)):
  for y in range(len(arr)):
    if y==len(arr)-1:
      break
    if arr[y]>arr[y+1]:
      flag=False
      temp=arr[y]
      arr[y]=arr[y+1]
      arr[y+1]=temp
  if flag:
    break


print(arr)
