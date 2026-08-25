arr=[-1,0,1,2,-1,-4]
k=3

for i in range(len(arr)-1):
  for j in range(i+1,0,-1):
    if arr[j]<arr[j-1]:
      temp=arr[j-1]
      arr[j-1]=arr[j]
      arr[j]=temp

result=[]

for k in range(0,len(arr)):
  left=k+1
  right=len(arr)-1
  while(left<right):
    if(arr[k]+arr[left]+arr[right]==0):
      result.append([arr[k],arr[left],arr[right]])
      left+=1
    elif(arr[k]+arr[left]+arr[right]>0):
      right-=1
    else:
      left+=1



print(result)
