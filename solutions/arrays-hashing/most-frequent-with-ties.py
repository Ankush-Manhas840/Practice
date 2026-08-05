freq=[7,7,1,1,34,34,34,34,343,43,43,434,34,3,4,55,65,65,75,757,7,7,7]
hashmap=dict()
keymax=0
freq_max=dict()
for x in freq:

  hashmap[x]=hashmap.get(x,0)+1
  if freq_max.get(keymax,0)<hashmap.get(x):
    keymax=x
    freq_max.clear()
    freq_max[keymax]=hashmap.get(keymax)
  elif hashmap.get(x)==freq_max.get(keymax):
    freq_max[x]=hashmap.get(x)




print(freq_max)
