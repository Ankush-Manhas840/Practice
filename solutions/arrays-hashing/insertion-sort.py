arr=[12,3434,2323,121232324,5343,5,1,2,4,33]

for x in range(1,len(arr)):
  for y in range(x,0,-1):
    if(arr[y]<arr[y-1]):
      temp=arr[y]
      arr[y]=arr[y-1]
      arr[y-1]=temp
    else:
      break

print(arr)
