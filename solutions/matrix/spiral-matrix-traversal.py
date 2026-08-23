arr= [[1,2,3],[4,5,6],[7,8,9]]
top=0
left=0
right=len(arr[0])-1
bottom=len(arr)-1

while(top<=bottom and left<=right):

 for i in range(left,right+1):
   print(arr[top][i])
 top+=1
 for j in range(top,bottom+1):
   print(arr[j][right])


 if top<=bottom:

  for z in range(right-1,left-1,-1):
    print(arr[bottom][z])
  bottom-=1

 if left<right:
  for k in range(bottom,top-1,-1):
    print(arr[k][left])

 left+=1
 right-=1
