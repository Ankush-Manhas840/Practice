arr=[0,2]
i=0
j=i+1

while(i<len(arr)-1 and j<len(arr)):
  if arr[i]!=0:
    i+=1
  elif arr[j]==0:
    j+=1
  elif arr[j]!=0:
    arr[i]=arr[j]
    arr[j]=0




print(arr)
