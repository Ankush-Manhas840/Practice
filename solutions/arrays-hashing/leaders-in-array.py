arr = [10, 22, 12, 3, 0, 6]

result=[]
result.append(arr[-1])
for x in range(len(arr)-2,-1,-1):
  if(arr[x]>arr[x+1]):

    for y in range(len(result)):
      flag=False
      if arr[x]>result[y]:
        flag=True

    if flag:
      result.append(arr[x])


result.reverse()
print(result)
