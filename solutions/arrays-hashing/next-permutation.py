arr=[3,2,1]
piviot=-1
small=float('inf')
smallidx=-1
for x in range(len(arr)-2,-1,-1):

  if(arr[x]<arr[x+1]):
    piviot=x


    break


idx=-1
for y in range(len(arr)-1,piviot,-1):
  if( arr[piviot]<arr[y]):
    idx=y
    break

if(piviot!=-1):

  temp=arr[piviot]
  arr[piviot]=arr[idx]
  arr[idx]=temp

start=piviot+1
end=len(arr)-1
while(start<end):
  temp=arr[start]
  arr[start]=arr[end]
  arr[end]=temp
  end-=1
  start+=1


print(arr)
