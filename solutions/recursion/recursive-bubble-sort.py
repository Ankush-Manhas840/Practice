def rec_bubble(arr):

  flag=True
  for y in range(len(arr)-1):
    if arr[y]>arr[y+1]:
      temp=arr[y]
      arr[y]=arr[y+1]
      flag=False
      arr[y+1]=temp

  if flag:

    return arr
  else:

   return rec_bubble(arr)


print(rec_bubble( [3,2,55,0,1]))
print(rec_bubble( []))
print(rec_bubble( [7]))
print(rec_bubble( [5,4,3,2,1]))
