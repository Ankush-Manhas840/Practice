hashmap=dict()
arr=[1,23,43,4,34,23,1,232,3,24,2,31,21]
result=[]
for x in range(len(arr)):
  if arr[x] not in hashmap:
    result.append(arr[x])
    hashmap[arr[x]]=hashmap.get(arr[x],0)+1
print(result)
