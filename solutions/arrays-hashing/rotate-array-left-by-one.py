arr=[1,2,3,4,5]
k=1
element=arr[0]
for i in range(len(arr)-1):
  arr[i]=arr[i+k]

arr[len(arr)-k]=element
print(arr)
