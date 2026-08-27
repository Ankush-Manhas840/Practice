arr=[6, -2, 2, -8, 1, 7, 4, -10]
length=-1
i=0
j=0
sum=0
hashmap=dict()
hashmap[0]=-1
while(j<len(arr)):
  sum+=arr[j]
  if sum not in hashmap.keys():
    hashmap[sum]=j
  else:
    length=max(length,j-hashmap.get(sum))

  j+=1



print(length)
