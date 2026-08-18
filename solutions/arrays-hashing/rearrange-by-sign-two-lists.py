arr = [3, 1, -2, -5, 2, -4]
list1=[]
list_nev=[]
result=[]
for i in range(len(arr)):
  if(arr[i]>0):
    list1.append(arr[i])
  else:
    list_nev.append(arr[i])

left=0
right=0

for x in range(len(arr)):
  if x%2==0:
    result.append(list1[left])
    left+=1

  else:
    result.append(list_nev[right])
    right+=1


print(result)
print(list1)
print(list_nev)
