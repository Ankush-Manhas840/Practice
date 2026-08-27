arr=[1,2,3,4]
target=9
result=[]
sum=0

for q in range(len(arr)):
  min=float("inf")
  idx=-1
  for b in range(q,len(arr)):
    if(min>arr[b]):
      idx=b
      min=arr[b]

  temp=arr[q]
  arr[q]=arr[idx]
  arr[idx]=temp

for i in range(len(arr)):
  for j in range(i+1,len(arr)):
    a=j+1
    b=len(arr)-1
    while(a<b):
      if(arr[i]+arr[j]+arr[a]+arr[b]==target):
        if [arr[i],arr[j],arr[a],arr[b]] not in result:
          result.append([arr[i],arr[j],arr[a],arr[b]])
        a+=1
      elif(arr[i]+arr[j]+arr[a]+arr[b]>target):
        b-=1
      elif(arr[i]+arr[j]+arr[a]+arr[b]<target):
        a+=1


print(result)
