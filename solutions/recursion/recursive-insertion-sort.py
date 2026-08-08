def rec_ins(x,arr):
  if x==len(arr):
    return arr
  for y in range(x,0,-1):
    if(arr[y]<arr[y-1]):
      temp=arr[y]
      arr[y]=arr[y-1]
      arr[y-1]=temp

  x+=1
  return rec_ins(x,arr)





arr=[4,3,1,2,0]
rec_ins(0,arr)
print(rec_ins(0, [4,3,1,2,0]))
print(rec_ins(0, []))
print(rec_ins(0, [7]))
print(rec_ins(0, [5,4,3,2,1]))
