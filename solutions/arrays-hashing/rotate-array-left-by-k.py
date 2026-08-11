arr=["a","b","c","d","e"]
k=3
k=k%len(arr)
element=arr[0:k]
for i in range(len(arr)-k):
  arr[i]=arr[i+k]

for x in range(k):
  arr[len(arr)-k+x]=element[x]

print(arr)
arr=[1,2,3,4,5,6,7,8,9]
k=10
k=k%len(arr)
element =arr[k*-1:]
for i in range(len(arr)-1,k-1,-1):
  arr[i]=arr[i-k]

arr[0:k]=element
print(arr)
