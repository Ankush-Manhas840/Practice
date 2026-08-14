arr=[1,1,1,0,1,1,1,1,1]
ma=0
checker=0
for i in range(len(arr)-1):

  if(arr[i]==arr[i+1]):
    checker+=1
  else:
    ma=max(ma,checker)
    checker=0

ma=max(ma,checker)
print(ma+1)
