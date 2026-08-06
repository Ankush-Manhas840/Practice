arr=[1,2,3]
for x in range(len(arr)-1):
  smallest=arr[x]
  xa=x
  for y in range(x,len(arr)):
    if smallest>arr[y]:
      xa=y
      smallest=arr[y]
  arr[x],arr[xa]=arr[xa],arr[x]
print(arr)
