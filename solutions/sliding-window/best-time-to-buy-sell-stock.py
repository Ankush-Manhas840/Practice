arr=[7,6,4,3,1]
profit=0
small=float("inf")

for x in range(len(arr)):
  if (arr[x]<small):
    small=arr[x]
  elif arr[x]>small:
    profit=max(profit,arr[x]-small)




print(profit)
