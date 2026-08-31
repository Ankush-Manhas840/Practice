arr=[2,3,0,0]
brr=[2,5]

k=len(arr)-1
i=(len(arr)-len(brr))-1
j=len(brr)-1
while (k!=-1 and j!=-1):

  if(i<0 and j>=0):
    temp=arr[k]
    arr[k]=brr[j]
    brr[j]=temp
    k-=1
    j-=1

  elif(arr[i]>=brr[j]):
    temp=arr[i]
    arr[i]=arr[k]
    arr[k]=temp
    k-=1
    i-=1
  elif(arr[i]<brr[j]):
    temp=brr[j]
    brr[j]=arr[k]
    arr[k]=temp
    k-=1
    j-=1

print(arr)
