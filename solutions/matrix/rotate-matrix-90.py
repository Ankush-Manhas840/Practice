arr= [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]

for r in arr:
    print(r)
for row in range(len(arr)):
  for col in range(len(arr[0])):
    if row<col:
      temp=arr[row][col]
      arr[row][col]=arr[col][row]
      arr[col][row]=temp

for z in range(len(arr)):

    start=0
    end=len(arr[z])-1
    while(start<end):
      temp=arr[z][start]
      arr[z][start]=arr[z][end]
      arr[z][end]=temp

      start+=1
      end-=1

print()
for r in arr:
    print(r)
