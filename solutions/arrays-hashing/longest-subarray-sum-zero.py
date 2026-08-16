arr=[9, -3, 3, -1, 6, -5]
hashmap=dict()
length=0
sum=0
hashmap[sum]=-1
for x in range(len(arr)):
  sum+=arr[x]
  if sum in hashmap:
    length=max(length,x-hashmap[sum])
  else:

   hashmap[sum]=x

print(length)
