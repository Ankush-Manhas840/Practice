arr=[1,1,2]
i=1
j=i
uniq=1
while(j<len(arr)):
  if  arr[i-1]!=arr[j]:
    arr[i]=arr[j]
    uniq+=1
    i+=1
  j+=1

arr[:uniq]
