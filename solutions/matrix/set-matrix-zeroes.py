arr=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
row=-1
col=-1
checker=[]
#print(len(arr[0]))
for i in range(len(arr)):
  for j in range(len(arr[0])):
    if(arr[i][j]==0):
      row=i
      col=j
      checker.append([row,col])



for z in range(len(checker)):
  r=checker[z][0]
  c=checker[z][1]

  for t in range(len(arr[0])):
    arr[r][t]=0

  for y in range(len(arr)):
    arr[y][c]=0


print(arr)
