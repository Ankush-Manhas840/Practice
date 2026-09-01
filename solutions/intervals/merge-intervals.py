arr=[[8,10],[1,3],[2,6]]
arr.sort()
ans=[]
for i in range(len(arr)):
  if len(ans)==0 or ans[-1][1]<=arr[i][0]:
    ans.append(arr[i])
  else:
    start=min(ans[-1][0],arr[i][0])
    end=max(ans[-1][1],arr[i][1])
    ans[-1]=[start,end]


print(ans)
