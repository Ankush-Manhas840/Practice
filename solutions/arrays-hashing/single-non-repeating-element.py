hashmap=dict()
arr=[1,2,4,1,2]
result=0
for i in range(len(arr)):
  hashmap[arr[i]]=hashmap.get(arr[i],0)+1


for x in hashmap:
  if hashmap.get(x)==1:
    result=x


print(result)
