arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,4,5,11,12]
hashmap=dict()
for i in range(len(arr1)):
  hashmap[arr1[i]]=hashmap.get(arr1[i],0)+1

for i in range(len(arr2)):
  hashmap[arr2[i]]=hashmap.get(arr2[i],0)+1

result=list(hashmap.keys())
print(result)
