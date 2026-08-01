def rev(arr,front,rear):
  if(front >=rear):
    return arr
  else:
    arr[front],arr[rear]=arr[rear],arr[front]
    rev(arr,front+1,rear-1)
arr=[1,34,4353,2323,42234]
rev(arr,0,len(arr)-1)
print(arr)
