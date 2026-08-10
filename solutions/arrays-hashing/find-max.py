max=float('-inf')

arr=[1,2,34,3,232,312,3,2,2,43,2,31,21]
for i in range(len(arr)):
  if(arr[i]>max):
    max=arr[i]

print(max)
