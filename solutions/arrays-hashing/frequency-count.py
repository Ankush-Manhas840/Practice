freq=[1,1,1,1,1,1,1,1,322,235,23,23,23,232,3,5,4,4,4,4,4]
result={}
for x in freq:
  if x in result:
    result[x]+=1
  else:
    result[x]=1

print(result)



from collections import Counter
freq=[1,1,1,1,1,1,1,1,322,235,23,23,23,232,3,5,4,4,4,4,4]
hash_map=dict()
for x in freq:
  hash_map[x]=hash_map.get(x,0)+1

print(hash_map)
