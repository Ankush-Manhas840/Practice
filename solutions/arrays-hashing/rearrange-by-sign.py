arr=[1,2,3,-1,-2,-3]

i=0
while(i!=len(arr)-2):
  j=i
  while(arr[j]>0):
    j+=1

  y=arr[j]
  for x in range(i+1,j+1):
    arr[j]=arr[j-1]
    j-=1

  arr[i+1]=y

  i+=1
  if(arr[i]<0):
    i+=1

print(arr)
